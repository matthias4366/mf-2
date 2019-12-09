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

# With the food central app, different databases can be searched:
# "Foundation", "Survey (FNDDS)", "Branded" and "SR Legacy".
# The question is: are the JSON files from all of these databases in the same
# format?
# To test this, an example food from each database was taken.
# The search term "beans" was used in each case and the first listed result
# was used.
food_central_id_different_databases = {
    'Foundation': "335912",
    'Survey (FNDDS)': "339277",
    "Branded": "548596",
    "SR Legacy": "169885",
    # Beverages, fruit-flavored drink, powder,
    # with high vitamin C with other added vitamins, low calorie
    "Drink with added vitamins": "167707",
    "Beverages, DANNON, water, bottled, non-carbonated, with Fluoride":
        "173658",
    "PURIFIED WATER contains Molybdenum": "517684",
}

for database, FDC_ID in food_central_id_different_databases.items():

    url_food_details = r'https://api.nal.usda.gov/fdc/v1/'\
           + FDC_ID \
           + r'?api_key='\
           + str(API_KEY)

    print(url_food_details)

    response = requests.get(
        url_food_details,
    )

    file_name_to_save_JSON = database + \
        '_api_food_details_endpoint_response.txt'

    with open(file_name_to_save_JSON, 'w') as outfile:
        json.dump(response.json(), outfile, indent=4, sort_keys=True)
