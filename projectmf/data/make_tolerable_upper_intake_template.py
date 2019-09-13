import pprint

VITAMINS_AND_DEFAULT_UNITS = [
    {'name': 'vitamin_a',
     'default_unit': 'microgram'},
    {'name': 'vitamin_c',
     'default_unit': 'milligram'},
    {'name': 'vitamin_d',
     'default_unit': 'microgram'},
    {'name': 'vitamin_e',
     'default_unit': 'milligram'},
    {'name': 'vitamin_k',
     'default_unit': 'microgram'},
    {'name': 'thiamin',
     'default_unit': 'milligram'},
    {'name': 'riboflavin',
     'default_unit': 'milligram'},
    {'name': 'niacin',
     'default_unit': 'milligram'},
    {'name': 'vitamin_b6',
     'default_unit': 'milligram'},
    {'name': 'folate',
     'default_unit': 'microgram'},
    {'name': 'vitamin_b12',
     'default_unit': 'microgram'},
    {'name': 'pantothenic_acid',
     'default_unit': 'milligram'},
    {'name': 'biotin',
     'default_unit': 'microgram'},
    {'name': 'choline',
     'default_unit': 'milligram'},
]

ELEMENTS_AND_DEFAULT_UNITS = [
    {'name': 'calcium',
     'default_unit': 'milligram'},
    {'name': 'chromium',
     'default_unit': 'microgram'},
    {'name': 'copper',
     'default_unit': 'microgram'},
    {'name': 'fluoride',
     'default_unit': 'milligram'},
    {'name': 'iodine',
     'default_unit': 'microgram'},
    {'name': 'iron',
     'default_unit': 'milligram'},
    {'name': 'magnesium',
     'default_unit': 'milligram'},
    {'name': 'manganese',
     'default_unit': 'milligram'},
    {'name': 'molybdenum',
     'default_unit': 'microgram'},
    {'name': 'phosphorus',
     'default_unit': 'milligram'},
    {'name': 'selenium',
     'default_unit': 'microgram'},
    {'name': 'zinc',
     'default_unit': 'milligram'},
    {'name': 'potassium',
     'default_unit': 'gram'},
    {'name': 'sodium',
     'default_unit': 'gram'},
    {'name': 'chloride',
     'default_unit': 'gram'},
]

template_dict = {
    'name': None
}

for nutrient_dict in VITAMINS_AND_DEFAULT_UNITS:

    field_name_to_add = nutrient_dict['name']+'_tolerable_upper_intake'
    dict_ = {field_name_to_add: None}
    template_dict.update(dict_)

    field_name_unit = nutrient_dict['name']+'_unit'
    dict_ = {field_name_unit: nutrient_dict['default_unit']}
    template_dict.update(dict_)

for nutrient_dict in ELEMENTS_AND_DEFAULT_UNITS:

    field_name_to_add = nutrient_dict['name']+'_tolerable_upper_intake'
    dict_ = {field_name_to_add: None}
    template_dict.update(dict_)

    field_name_unit = nutrient_dict['name']+'_unit'
    dict_ = {field_name_unit: nutrient_dict['default_unit']}
    template_dict.update(dict_)

print('template_dict')
print(template_dict)
