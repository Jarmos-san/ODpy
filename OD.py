import configparser, os, json
import requests

config = configparser.ConfigParser()
config.read('config.ini')

app_id = config.get('SECRET', 'ID')
app_key = config.get('SECRET', 'KEY')

language = "en-gb"
word_id = "Apple"
 
url = f"https://od-api.oxforddictionaries.com:443/api/v2/entries/{language}/{word_id.lower()}"
 
r = requests.get(url, headers={"app_id": app_id, "app_key": app_key}) 
print(r.text)
