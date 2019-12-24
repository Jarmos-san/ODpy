import configparser, os, json
import requests

if 'ID' and 'KEY' in os.environ:
    ID = os.environ.get('ID')
    KEY = os.environ.get('KEY')
else:
    config = configparser.ConfigParser()
    config.read('config.ini')

    ID = config.get('SECRET', 'ID')
    KEY = config.get('SECRET', 'KEY')

language = "en-gb"
word_id = "Apple"
  
url = f"https://od-api.oxforddictionaries.com:443/api/v2/entries/{language}/{word_id.lower()}"
  
r = requests.get(url, headers={"app_id": ID, "app_key": KEY})
print(r.text)
