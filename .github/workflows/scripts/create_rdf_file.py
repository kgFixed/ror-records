import json
from pathlib import Path
import tempfile
from sema.subyt import Subyt
import logging

# Only shows errors
logging.getLogger("sema.subyt").setLevel(logging.ERROR) 

def json_to_individual_rdf(json_path, template_path, output_dir):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    with open(json_path, encoding='utf-8') as f:
        data = json.load(f)
        organizations = [data] if isinstance(data, dict) else data
        
        for org in organizations:
            ror_id = org['id'].split('/')[-1]
            
            with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as tmp:
                json.dump({"sets": {"qres": [org]}}, tmp, ensure_ascii=False, indent=2)
                tmp_path = tmp.name
            
            try:
                Subyt(
                    template_name=str(Path(template_path).name),
                    template_folder=str(Path(template_path).parent),
                    extra_sources={"qres": str(Path(tmp_path).resolve())},
                    sink=str(Path(output_dir) / f"{ror_id}.ttl"),
                    overwrite_sink=True,
                    conditional=False
                ).process()
                
                # expected_ttl = Path(output_dir) / f"{ror_id}.ttl"
                # if expected_ttl.exists():
                #     print(f"🎉 SUCCÈS: Fichier TTL généré: {expected_ttl}")
                #     print(f"   Taille: {expected_ttl.stat().st_size} bytes")
                #     # Afficher un aperçu du contenu
                #     content = expected_ttl.read_text()[:200] + "..." if expected_ttl.stat().st_size > 200 else expected_ttl.read_text()
                #     print(f"   Aperçu: {content}")
                # else:
                #     print(f"❌ ÉCHEC: Fichier TTL non généré: {expected_ttl}")
            
            finally:
                Path(tmp_path).unlink()
                print("Pas validé")

# Example of use for 2.1
# json_to_individual_rdf( 
#     json_path= Path(__file__).parent.parent / "ror_releases/v1.6/023rffy11.json",
#     template_path= Path(__file__).parent.parent / "template/template_2_1.ttl",
#     output_dir= Path(__file__).parent.parent / "to_push"
# )

# Example of use for 1.0
# json_to_individual_rdf( 
#     json_path= Path(__file__).parent.parent / "ror_releases/v1.6/023rffy11.json",
#     template_path= Path(__file__).parent.parent / "template/template_1_0.ttl",
#     output_dir= Path(__file__).parent.parent / "to_push"
# )








