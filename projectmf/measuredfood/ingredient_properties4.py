import json

with open('data/nutrient_dict_list.json', 'r') as fp:
    ALL_NUTRIENTS_AND_DEFAULT_UNITS = json.load(fp)
