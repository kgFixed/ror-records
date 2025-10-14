#!/usr/bin/env python3

from pathlib import Path
from sema.subyt import Subyt

def list_specific_release(release_name):
    release_path = Path(release_name)
    if not release_path.exists():
        print(f"❌ Le dossier {release_name} n'existe pas")
        return
    
    json_files = list(release_path.glob("*.json"))
    
    if not json_files:
        print(f"❌ Aucun fichier JSON trouvé dans {release_name}")
        return
    
    print(f"📁 RELEASE: {release_name}")
    print(f"📊 {len(json_files)} fichiers trouvés")
    print("-" * 40)
    
    for json_file in sorted(json_files):
        file_size = json_file.stat().st_size
        print(f"📄 {json_file.name} ({file_size} bytes)")

if __name__ == "__main__":
    # Vous pouvez changer le nom de la release ici
    list_specific_release("v1.56")
