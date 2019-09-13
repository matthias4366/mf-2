"""
The original source for the data for the ingredients is in a list of python
dictionaries. In order to be able to load the data into the django app with
a python script, the list of dictionaries is converted into JSON.
"""

# noinspection PyUnresolvedReferences
from initial_tolerable_upper_intake import \
    tolerable_upper_intake_initial
import json

import sys
sys.path.insert(0, '/projectmf/fixtures/')

# Adapt the python list of dictionaries of the ingredients so it produces the
# correct JSON with the model name, pk and the fields.
formatted_tolerable_upper_intake_dict_list = []

for k in range(len(tolerable_upper_intake_initial)):

    formatted_tolerable_upper_intake_dict_k = tolerable_upper_intake_initial[k]
    formatted_tolerable_upper_intake_dict_k['author'] = 1

    formatted_dict_k = {
        'model': 'measuredfood.tolerableupperintake',
        'pk': k+1,
        'fields': formatted_tolerable_upper_intake_dict_k
    }

    formatted_tolerable_upper_intake_dict_list.append(formatted_dict_k)

with open(
        '/home/matthias/1_local_code/'
        'mf-2/projectmf/fixtures/tolerable_upper_intake_initial_data.json',
        'w', encoding='utf-8'
) as f:
    json.dump(
        formatted_tolerable_upper_intake_dict_list, f, ensure_ascii=False,
        indent=4
    )
