# Trying something different to import the data ingredient dictionaries
# use importlib

# import the ingredient dictionaries
import sys
sys.path.append(r'/home/matthias/1_local_code/mf-2/projectmf/data')
from data.ingredients_data import ingredient_dict_list


# import json
#
#
# def make_json_from_ingredient_dict(ingredient_dict_):
#     pass
#
# # From https://realpython.com/python-json/
# # Writing a minimal example just to get something to work:
# data_ = {
#     "president": {
#         "name": "Zaphod Beeblebrox",
#         "species": "Betelgeusian"
#     }
# }
#
# with open("data_file.json", "w") as write_file:
#     json.dump(data_, write_file)
