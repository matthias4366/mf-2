import requests
import pprint
import json

# API Key for tailoredmealplans@gmail.com
API_KEY = 'yucJ7dnpJ85gj5bFGg0RK463TZqb9gu2Gy4vvCDd'

params = {'api_key': API_KEY}
data = {'generalSearchInput': 'chia'}
response = requests.post(
    r'https://api.nal.usda.gov/fdc/v1/search',
    params=params,
    json=data
)

with open('api_response_learn.txt', 'w') as outfile:
    json.dump(response.json(), outfile , indent=4, sort_keys=True)

pprint.pprint(response.json())
