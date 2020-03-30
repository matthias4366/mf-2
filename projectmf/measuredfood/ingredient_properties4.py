import json

from pathlib import Path

path_to_json_file = Path.cwd().parent.joinpath('data').joinpath(
    'nutrient_dict_list.json')

with open(path_to_json_file, 'r') as fp:
    ALL_NUTRIENTS_AND_DEFAULT_UNITS = json.load(fp)

INGREDIENT_FIELDS_LINKS = [
    'buy_here_link',
    'source_nutritional_information_link'
]
