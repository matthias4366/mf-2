import pandas as pd
import json
from transform_unit_name_csv_to_unit_name_api import \
    transform_unit_name_csv_to_unit_name_api

"""
The USDA was so kind as to provide a full list of all the nutrients,
with their ids and their units. It is most efficient to create a dictionary 
from that list and store it in "ingredient_properties4.py".
"""

df = pd.read_csv(
    '/home/matthias/1_local_code/mf-2/projectmf/data/nutrient.csv'
)

NUTRIENT_DICT_LIST_ID_NAME_UNIT = []

for index, row in df.iterrows():
    # print(row['id'], row['name'], row['unit_name'])
    id_nutrient_usda_api = row['id']
    nutrient_name_usda_api = row['name']
    unit_nutrient_usda_csv = row['unit_name']
    unit_nutrient_usda_api = \
        transform_unit_name_csv_to_unit_name_api(
            unit_nutrient_usda_csv
        )
    display_in_ingredient_form = row['display_in_ingredient_form']

    nutrient_dict_as_string = \
        {
            'id_nutrient_usda_api': id_nutrient_usda_api,
            'nutrient_name_usda_api': nutrient_name_usda_api,
            'unit_nutrient_usda_csv': unit_nutrient_usda_csv,
            'unit_nutrient_usda_api': unit_nutrient_usda_api,
            'display_in_ingredient_form': display_in_ingredient_form,
        }

    NUTRIENT_DICT_LIST_ID_NAME_UNIT.append(
        nutrient_dict_as_string
    )

# Write to json file.

with open('nutrient_dict_list.json', 'w') as fp:
    json.dump(NUTRIENT_DICT_LIST_ID_NAME_UNIT, fp, indent=4)
