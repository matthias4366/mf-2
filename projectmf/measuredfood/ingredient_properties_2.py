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
    'carbohydrate',
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

ELEMENTS = [
    'calcium',
    'chromium',
    'coppper',
    'fluoride',
    'iodine',
    'iron',
    'magnesium',
    'manganese',
    'molybdenum',
    'phosphorus',
    'selenium',
    'zinc',
    'potassium',
    'sodium',
    'chloride'
]

FIBER = [
    'total_fiber',
]


# Since users might not want to type in all the nutritional information for
# their ingredients, since they are maybe only interested in macros,
# a short list is provided. This
INGREDIENT_PROPERTIES_SHORT_LIST = [

]

# Some things are ignored for now.
IGNORED = [
    'total_water'
]
