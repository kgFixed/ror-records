import requests
from pathlib import Path
from detect_version_json import detect_ror_version
from create_rdf_file import json_to_individual_rdf
import tempfile
import json

def process_ror_file(json_path, output_dir):
    version = detect_ror_version(json_path)
    # print(json_path)
    # print(output_dir)
    templates_to_try = []
    
    if version is None:
        templates_to_try = [
            "template_1_0.ttl",
            "template_2_0.ttl",
            "template_2_1.ttl"
        ]
    else:
        templates_to_try = [f"template_{version}.ttl"]
    
    for template_name in templates_to_try:
        # path_used_template = f".github/workflows/template/{template_name}"
        path_used_template = Path("template") / template_name
        # print(path_used_template)
        
        try:
            json_to_individual_rdf(
                json_path=json_path,
                template_path=path_used_template,
                output_dir=output_dir
            )
            return
            
        except Exception as e:
            print(f"Template failure {template_name}: {str(e)}")
            continue
    
    raise ValueError(f"No valid template found for the file: {json_path}")

def process_from_url(json_url, output_dir):
    """Process single URL or list of URLs"""
    
    # Créer le dossier de sortie
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Convertir en liste si c'est une seule URL
    urls = [json_url] if isinstance(json_url, str) else json_url
    
    for url in urls:
        print(f"📥 Traitement de l'URL: {url}")
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            json_data = response.json()
            
            # Créer un nom de fichier temporaire unique pour chaque URL
            temp_filename = f"temp_ror_data_{hash(url) % 10000}.json"
            temp_path = Path(output_dir) / temp_filename
            
            with open(temp_path, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, ensure_ascii=False, indent=2)
            
            print(f"✅ Fichier temporaire créé: {temp_path}")
            process_ror_file(temp_path, output_dir)
            
        except Exception as e:
            print(f"❌ Erreur avec l'URL {url}: {e}")
            continue  # Continue avec l'URL suivante en cas d'erreur
            
        finally:
            # Nettoyer le fichier temporaire pour cette URL
            if 'temp_path' in locals() and temp_path.exists():
                temp_path.unlink()
                print(f"🧹 Fichier temporaire nettoyé: {temp_path}")

# Example with a json that does not correspond to any version
# process_ror_file(Path(__file__).parent.parent / "ror_releases/v1.6/023rffy11.json", Path(__file__).parent.parent / "test")
















