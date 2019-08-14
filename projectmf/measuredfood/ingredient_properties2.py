import copy

"""
ingredient_properties_2 is the revised version of ingredient_properties.
The fields of the ingredients containing for example nutrient properties such
as vitamins are rewritten.

This time, the nutrients are taken from the National Institute of Health.
Source:
https://ods.od.nih.gov/Health_Information/Dietary_Reference_Intakes.aspx
"""

CALORIES = [
    'calories'
]

MACRONUTRIENTS = [
    # Matthias Schulz called it carbohydrates instead of carbohydrate
    # because that is what he is used to.
    'carbohydrates',
    'fat',
    'protein',
]

ESSENTIAL_FATS = [
    'linoleic_acid',
    'alpha_linoleic_acid',
]

VITAMINS = [
    'vitamin_a',
    'vitamin_c',
    'vitamin_d',
    'vitamin_e',
    'vitamin_k',
    'thiamin',
    'riboflavin',
    'niacin',
    'vitamin_b6',
    'folate',
    'vitamin_b12',
    'pantothenic_acid',
    'biotin',
    'choline',
]

VITAMINS_AND_DEFAULT_UNITS = [
    {'name': 'vitamin_a',
     'default_unit': 'microgram'},
    {'name': 'vitamin_c',
     'default_unit': 'milligram'},
    {'name': 'vitamin_d',
     'default_unit': 'international units'},
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
    {'name': 'coppper',
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

INGREDIENT_FIELDS_LINKS = [
    'buy_here_link',
    'source_nutritional_information_link'
]

# Some things are ignored for now.
# IGNORED = [
#     'total_water'
# ]
# FIBER = [
#     'total_fiber',
# ]
