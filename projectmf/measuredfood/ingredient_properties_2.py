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
    'calcium_unit',
    'chromium',
    'chromium_unit',
    'coppper',
    'copper_unit',
    'fluoride',
    'fluoride_unit',
    'iodine',
    'iodine_unit',
    'iron',
    'iron_unit',
    'magnesium',
    'magnesium_unit',
    'manganese',
    'manganese_unit',
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

OTHER = [
    'total_water',
]
