import requests
from requests import get
import json


# Print Status of a Website
print(requests.get('https://github.com/RevilionDev/RevilionCode')) # Output <Response [200]> If website is UP

json_web = requests.get('https://raw.githubusercontent.com/RevilionDev/RevilionCode/main/Website/jsonexample.json').json()
print(json_web["RevilionDev"]) # The output will be "Cool!"