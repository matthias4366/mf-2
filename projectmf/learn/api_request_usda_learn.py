import requests
import json

"""
In this file, Sandor Clegane is learning how to make requests to the FoodData 
central API. There are two parts: making a request to the food search 
endpoint and making a request to the food details endpoint. 
"""

# API Key for tailoredmealplans@gmail.com
API_KEY = 'yucJ7dnpJ85gj5bFGg0RK463TZqb9gu2Gy4vvCDd'

# Making a request to the food search endpoint.

params = {
    'api_key': API_KEY,
    "pageNumber": "2",
}
data = {'generalSearchInput': 'chia'}
response = requests.post(
    r'https://api.nal.usda.gov/fdc/v1/search',
    params=params,
    json=data
)

with open('api_food_search_endpoint_response.txt', 'w') as outfile:
    json.dump(response.json(), outfile, indent=4, sort_keys=True)

# Making a request to the food details endpoint.

# People would first search for the food that they want to include from the
# USDA database at this website
# https://fdc.nal.usda.gov/fdc-app.html#/?query=beans%20kidney%20raw.

food_central_id_raw_kidney_beans = "173744"

params = {
    'api_key': API_KEY,
    "FoodData Central ID": food_central_id_raw_kidney_beans,
}

url_food_details = r'https://api.nal.usda.gov/fdc/v1/'\
       + food_central_id_raw_kidney_beans \
       + r'?api_key='\
       + str(API_KEY)

print(url_food_details)

response = requests.get(
    url_food_details,
)

with open('api_food_details_endpoint_response.txt', 'w') as outfile:
    json.dump(response.json(), outfile, indent=4, sort_keys=True)
