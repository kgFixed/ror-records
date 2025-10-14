import requests
from pathlib import Path
from detect_version_json import detect_ror_version
from create_rdf_file import json_to_individual_rdf

def process_ror_file(json_path, output_dir):
    version = detect_ror_version(json_path)
    
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
        path_used_template = Path(__file__).parent.parent / f"template/{template_name}"
        
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
    response = requests.get(json_url)
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as tmp:
        tmp.write(response.text)
        temp_path = Path(tmp.name)
        try:
            process_ror_file(temp_path, output_dir)
        finally:
            temp_path.unlink()

# Example with a json that does not correspond to any version
# process_ror_file(Path(__file__).parent.parent / "ror_releases/v1.6/023rffy11.json", Path(__file__).parent.parent / "test")



