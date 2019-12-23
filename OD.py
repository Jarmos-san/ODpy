
import requests
import json

app_id = "1234567"
app_key = "123467890asdfhjk"

language = "en-gb"
word_id = "Apple"

url = f"https://od-api.oxforddictionaries.com:443/api/v2/entries/{language}/{word_id.lower()}"

r = requests.get(url, headers={"app_id": app_id, "app_key": app_key}) 
print(r.text)
