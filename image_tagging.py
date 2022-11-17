import requests
from config import taging_config

def tag(image_url):
    tries =0 
    while(tries < 3):
        try:
            response = requests.get(
                'https://api.imagga.com/v2/tags?image_url=%s' % image_url,
                auth=(taging_config["api_key"], taging_config["api_secret"]))

            flag = False
            print(response.json())
            tags = response.json()["result"]["tags"]
            for res in tags:
                confidence = res["confidence"]
                object_name = res["tag"]["en"]
                if object_name == "vehicle" and confidence > 50:
                    flag = True
                    break
            if flag:
                return tags[0]["tag"]["en"]
            else:
                return None

        except Exception as e:
            print('ERROR')
            print(e)
            tries += 1