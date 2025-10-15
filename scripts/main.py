from template_to_try import process_from_url
from json_to_ttl import get_json_raw_urls

if __name__ == "__main__":

  # variables
  output_dir = "store_ror.org/"
  
  urls = get_json_raw_urls() 
  print(urls)
  # process_from_url(urls, output_dir)
