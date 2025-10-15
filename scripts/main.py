from template_to_try import process_from_url
from json_to_ttl import get_json_raw_urls
from pathlib import Path

if __name__ == "__main__":

  # variables
  output_dir = "store_ror.org/"

  urls = get_json_raw_urls() 
  release_name, urls = next(iter(urls.items()))
  process_from_url(urls, Path(output_dir) / release_name)
