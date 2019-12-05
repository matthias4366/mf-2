from ingredient_properties3 import ALL_NUTRIENTS_AND_DEFAULT_UNITS

"""
This code is a total hack.
It produces the code for the get_from_food_data_central view in 
views/rawingredient3.py. Within that view, it produces the code for the 
arguments for the creation of a Rawingredient3 object, i.e.
rawingredient3 = 
RawIngredient3(
[ This part is produced by this code. ]
)
"""

with open('code_for_creation_of_rawingredient3_object.txt', 'w') as outfile:
    for nutrient_dict in ALL_NUTRIENTS_AND_DEFAULT_UNITS:
        if nutrient_dict['name_measuredfood'] is not 'ignore':
            str_to_write = \
                nutrient_dict['name_measuredfood'] + \
                '=' \
                + 'response_json[\'' \
                + nutrient_dict['name_usda'] \
                + '\']' \
                + ',\n'
            outfile.write(str_to_write)

print('something')
