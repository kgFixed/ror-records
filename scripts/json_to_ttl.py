#!/usr/bin/env python3

from pathlib import Path
import requests

# renvoie la liste des urls pour une release
def get_json_raw_url(release_name):
    """Retourne uniquement les URLs raw des fichiers JSON"""
    
    release_path = Path(release_name)
    if not release_path.exists():
        return []
    
    json_files = list(release_path.glob("*.json"))
    urls = []
    
    for json_file in sorted(json_files):
        raw_url = f"https://raw.githubusercontent.com/kgFixed/ror-records/main/{release_name}/{json_file.name}"
        urls.append(raw_url)
    
    return urls

# cherche dernière release
def get_json_raw_urls():
    url = f"https://api.github.com/repos/ror-community/ror-updates/releases/latest"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Erreur lors de la récupération des données: {response.status_code}")
        return []
    data = response.json()
    tag_name_latest = data.get("tag_name", [])
    urls = get_json_raw_url(tag_name_latest)

    return urls

# if __name__ == "__main__":
#     release_name = "v1.56"  # Changez la version ici
    
#     urls = get_json_raw_urls(release_name)
    
#     if urls:
#         print(f"🔗 URLs des fichiers JSON pour {release_name}:")
#         # for url in urls:
#         print(urls)
#         # print(f"\n📊 Total: {len(urls)} URLs")
#     else:
#         print(f"❌ Aucun fichier trouvé dans {release_name}")
