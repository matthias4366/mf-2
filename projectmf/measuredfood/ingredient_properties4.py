import sys
sys.path.append('..')
sys.path.append('...')
sys.path.append('....')
sys.path.append('.....')
sys.path.append('......')

import json

import pathlib

path_to_data = pathlib.Path(__file__).parent.absolute().joinpath('data')
print('path_to_data')
print(path_to_data)
sys.path.append(path_to_data)
print('sys.path')
print(sys.path)

cur_path = pathlib.Path(__file__).parent.absolute()
print(cur_path)
file_path_ = cur_path / 'data' / 'nutrient_dict_list.json'
print('file_path_')
print(file_path_)

print('str(file_path_)')
print(str(file_path_))
#
# print('sys.path')
# print(sys.path)

with open('data.nutrient_dict_list.json', 'r') as fp:
# with open(str(file_path_), 'r') as fp:
    ALL_NUTRIENTS_AND_DEFAULT_UNITS = json.load(fp)

INGREDIENT_FIELDS_LINKS = [
    'buy_here_link',
    'source_nutritional_information_link'
]
