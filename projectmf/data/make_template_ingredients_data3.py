import json
import sys
sys.path.append('..')
sys.path.append('...')
sys.path.append('....')
sys.path.append('.....')
sys.path.append('......')

"""
Since the database is dropped and restored from time to time, Sandor loses 
all of his RawIngredient3 data. Hence, the RawIngredient3 data is stored in 
the ingredients_data3.py file.

This file creates a template for the RawIngredient3 data in the form of a 
list of dictionaries.
"""

with open('nutrient_dict_list.json', 'r') as fp:
    ALL_NUTRIENTS_AND_DEFAULT_UNITS = json.load(fp)

ingredients_to_add_manually = [
    'Barilla sauce (Arrabiata or similar)',
    'Chili powder',
    'Tomato puree, MUTTI',
    'Vitamin D3 Tablette Vitabay 5000 I.E.',
    'Salt, iodized',
    'Magnesium citrate',
    'Potassium citrate',
    'Calcium citrate',
    'Coriander',
    'Maggi',
    'Asian vegetable mix',
    'Water for white rice',
    'Salt for water for white rice',
    'Flaxseed flour',
    'Vit4Ever',
]

ingredient_dict_list = []
for ingredient_name in ingredients_to_add_manually:
    new_dict = {'name': ingredient_name}
    for nutrient in ALL_NUTRIENTS_AND_DEFAULT_UNITS:
        if nutrient['is_displayed']:
            nutrient_name = nutrient['nutrient_name_measuredfood']
            # print('nutrient_name')
            # print(nutrient_name)
            dict_with_nutrient_name_and_empty_value = {nutrient_name: None}
            # print(nutrient_name)
            # print(type(nutrient_name))
            new_dict.update(dict_with_nutrient_name_and_empty_value)
    ingredient_dict_list.append(new_dict)

with open('ingredients_data3_template.json', 'w') as fp:
    json.dump(ingredient_dict_list, fp, indent=4)
