#!/usr/bin/env python3

from pathlib import Path

def get_json_raw_urls(release_name):
    """Retourne uniquement les URLs raw des fichiers JSON"""
    
    release_path = Path(release_name)
    if not release_path.exists():
        return []
    
    json_files = list(release_path.glob("*.json"))
    urls = []
    
    for json_file in sorted(json_files):
        raw_url = f"https://raw.githubusercontent.com/kgFixed/ror-records/main/{release_name}/{json_file.name}"
        urls.append(raw_url)
    
    return urls[0]

if __name__ == "__main__":
    release_name = "v1.56"  # Changez la version ici
    
    urls = get_json_raw_urls(release_name)
    
    if urls:
        print(f"🔗 URLs des fichiers JSON pour {release_name}:")
        # for url in urls:
        print(urls)
        # print(f"\n📊 Total: {len(urls)} URLs")
    else:
        print(f"❌ Aucun fichier trouvé dans {release_name}")
