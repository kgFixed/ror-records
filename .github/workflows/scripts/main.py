from template_to_try import process_from_url
from json_to_ttl import get_json_raw_urls

if __name__ == "__main__":

  # variables
  release_name = "v1.56" 
  output_dir = ".github/output/"
  
  urls = get_json_raw_urls(release_name) 
  process_from_url(urls, output_dir)
