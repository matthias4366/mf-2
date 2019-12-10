import pandas as pd
import json

"""
The USDA was so kind as to provide a full list of all the nutrients,
with their ids and their units. It is most efficient to create a dictionary 
from that list and store it in "ingredient_properties4.py".
"""

df = pd.read_csv(
    '/home/matthias/1_local_code/mf-2/projectmf/data/nutrient.csv'
)

nutrient_dict_list_str = \
    'NUTRIENT_DICT_LIST_ID_NAME_UNIT = ['

for index, row in df.iterrows():
    # print(row['id'], row['name'], row['unit_name'])
    id_nutrient_usda_api = row['id']
    nutrient_name_usda_api = row['name']
    unit_nutrient_usda_csv = row['unit_name']
    unit_nutrient_usda_api = ''

    nutrient_dict_as_string = \
        '{\n' \
        f'    \'id_nutrient_usda_api\': \'{id_nutrient_usda_api}\', \n' \
        f'    \'nutrient_name_usda_api\': \'{nutrient_name_usda_api}\', \n'\
        f'    \'unit_nutrient_usda_csv\': \'{unit_nutrient_usda_csv}\', \n'  \
        f'    \'unit_nutrient_usda_api\': \'{unit_nutrient_usda_api}\', \n'  \
        '},\n'

    nutrient_dict_list_str = nutrient_dict_list_str + nutrient_dict_as_string

nutrient_dict_list_str = nutrient_dict_list_str + ']'

# Write to json file.

with open('nutrient_dict_list.json', 'w') as fp:
    json.dump(nutrient_dict_list_str, fp)
