import pandas as pd
import json
from transform_unit_name_csv_to_unit_name_api import \
    transform_unit_name_csv_to_unit_name_api
import sys
sys.path.append("..")
sys.path.append("...")
sys.path.append("....")
from measuredfood.utils.rawingredient3\
    .transform_nutrient_name_usda_to_measuredfood import \
    transform_nutrient_name_usda_to_measuredfood

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
    is_displayed = row['is_displayed']

    nutrient_name_measuredfood = \
        transform_nutrient_name_usda_to_measuredfood(
            nutrient_name_usda_api,
            id_nutrient_usda_api,
        )

    nutrient_dict_as_string = \
        {
            # In the USDA database, each nutrient is identified by a unique id.
            'id_nutrient_usda_api': id_nutrient_usda_api,
            # In the USDA database, each nutrient has a name. This name is
            # not unique, as the nutrients are identified by their unique
            # ids. For example, there is "Energy" twice: once with the unit
            # 'kcal', once with the unit 'kJ'.
            'nutrient_name_usda_api': nutrient_name_usda_api,
            # In the nutrient.csv file, each nutrient has a unit. However,
            # it is not in a pretty format, such as 'G' for 'gram'.
            'unit_nutrient_usda_csv': unit_nutrient_usda_csv,
            # The unit from the nutrients.csv file in the ugly format is
            # taken and the corresponding unit in a prettier format is found
            # and saved here.
            'unit_nutrient_usda_api': unit_nutrient_usda_api,
            # There are too many nutrients to display them all. This boolean
            # value decides whether a nutrient is displayed.
            'is_displayed': is_displayed,
            # The name under which the nutrient is stored in the measuredfood
            # database. It has to contain the id from the USDA database,
            # as that ensures uniqueness.
            'nutrient_name_measuredfood': nutrient_name_measuredfood,
        }

    NUTRIENT_DICT_LIST_ID_NAME_UNIT.append(
        nutrient_dict_as_string
    )

# Write to json file in this same folder:
with open('nutrient_dict_list.json', 'w') as fp:
    json.dump(NUTRIENT_DICT_LIST_ID_NAME_UNIT, fp, indent=4)

