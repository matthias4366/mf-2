import json

from pathlib import Path

# Correct path development:
# /home/matthias/1_local_code/mf-2/projectmf/data/nutrient_dict_list.json

path_to_nutrient_dict_list_json = Path(
    __file__).parent.parent.joinpath('data').joinpath('nutrient_dict_list.json')

with open(path_to_nutrient_dict_list_json, 'r') as fp:
    ALL_NUTRIENTS_AND_DEFAULT_UNITS = json.load(fp)

INGREDIENT_FIELDS_LINKS = [
    'buy_here_link',
    'source_nutritional_information_link'
]
