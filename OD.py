import configparser, os, json
import requests

# Checks for availability of the SECRET keys in Environment Variable
if 'ID' and 'KEY' in os.environ:
    ID = os.environ.get('ID')
    KEY = os.environ.get('KEY')
# Assigns SECRET keys from config file if they don't exist in Environment Variables. 
# For security reasons, secret keys from the Environment Variable will be given priority.
else:
    config = configparser.ConfigParser()
    config.read('config.ini')

    ID = config.get('SECRET', 'ID')
    KEY = config.get('SECRET', 'KEY')

language = "en-gb"
word_id = "Apple"
  
urlEntries = f"https://od-api.oxforddictionaries.com:443/api/v2/entries/{language}/{word_id.lower()}"
# urlLemmas = f"https://od-api.oxforddictionaries.com:443/api/v2/lemmas/{language}/{word_id}"
# urlThesaurus = f"https://od-api.oxforddictionaries.com:443/api/v2/thesaurus/{language}/{word_id}"
# urlSentences = f"https://od-api.oxforddictionaries.com:443/api/v2/sentences/{language}/{word_id}"
urlWords = f"https://od-api.oxforddictionaries.com:443/api/v2/words/{language}"

r = requests.get(urlWords, headers={"app_id": ID, "app_key": KEY})
print(r.text)

# if __name__ == "__main__":
#     print(f"Passing Secret Keys with ID: {ID} & Key: {KEY}")
#     print(r.text)
