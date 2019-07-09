"""
The original source for the data for the ingredients is in a list of python
dictionaries. In order to be able to load the data into the django app with
a python script, the list of dictionaries is converted into JSON.
"""

from ingredients_data import ingredient_dict_list
import json

import sys
sys.path.insert(0, '/projectmf/fixtures/')

# Adapt the python list of dictionaries of the ingredients so it produces the
# correct JSON with the model name, pk and the fields.
formatted_ingredient_dict_list = []

# for k in range(len(ingredient_dict_list)):
for k in range(1):
    formatted_dict_k = {
        'model': 'measuredfood.rawingredient',
        'pk': k+1,
        'fields':
                ingredient_dict_list[k]
    }

    formatted_ingredient_dict_list.append(formatted_dict_k)

with open('/home/matthias/1_local_code/mf-2/projectmf/fixtures/data.json', 'w', encoding='utf-8') as f:
    json.dump(formatted_ingredient_dict_list, f, ensure_ascii=False, indent=4)
