# Some nutrient names describe section titles and can thus be ignored.

# The unit names from FoodData Central are used,
# see Foundation_api_food_details_endpoint_response.txt for example.

# In the FoodData Central database from the USDA, the data are formatted a
# certain way. They must be transformed so they fit into the measuredfood
# database. The mapping dictionary says which key word in the USDA database
# corresponds to which key word in the measuredfood database.

ALL_NUTRIENTS_AND_DEFAULT_UNITS = [
    {
        'name_usda': 'Proximates',
        'name_measuredfood': 'ignore',
        'default_unit': 'g',
    },
    {
        'name_usda': 'Water',
        'name_measuredfood': 'water',
        'default_unit': 'g',
    },
    {
        'name_usda': 'Protein',
        'name_measuredfood': 'protein',
        'default_unit': 'g',
    },
    {
        'name_usda': 'Total lipid (fat)',
        'name_measuredfood': 'fat_total',
        'default_unit': 'g',
    },
    {
        'name_usda': 'Carbohydrates',
        'name_measuredfood': 'ignore',
        'default_unit': 'g',
    },
    {
        'name_usda': 'Fiber, total dietary',
        'name_measuredfood': 'fiber_total_dietary',
        'default_unit': 'g ',
    },
    {
        'name_usda': 'Starch',
        'name_measuredfood': 'starch',
        'default_unit': 'g',
    },
    {
        'name_usda': 'Minerals',
        'name_measuredfood': 'ignore',
        'default_unit': 'g',
    },
    {
        'name_usda': 'Calcium, Ca',
        'name_measuredfood': 'calcium',
        'default_unit': 'mg',
    },
    {
        'name_usda': 'Iron, Fe',
        'name_measuredfood': 'iron',
        'default_unit': 'mg',
    },
    {
        'name_usda': 'Magnesium, Mg',
        'name_measuredfood': 'magnesium',
        'default_unit': 'mg',
    },
    {
        'name_usda': 'Phosphorus, P',
        'name_measuredfood': 'phosphorus',
        'default_unit': 'mg',
    },
    {
        'name_usda': 'Potassium, K',
        'name_measuredfood': 'potassium',
        'default_unit': 'mg',
    },
    {
        'name_usda': 'Zinc, Zn',
        'name_measuredfood': 'zinc',
        'default_unit': 'mg',
    },
    {
        'name_usda': 'Copper, Cu',
        'name_measuredfood': 'copper',
        'default_unit': 'mg',
    },
    {
        'name_usda': 'Manganese, Mn',
        'name_measuredfood': 'manganese',
        'default_unit': 'mg',
    },
    {
        'name_usda': 'Sulfur, S',
        'name_measuredfood': 'sulfur',
        'default_unit': 'mg',
    },
    {
        'name_usda': 'Nickel, Ni',
        'name_measuredfood': 'nickel',
        'default_unit': '\u00b5g',
    },
    {
        'name_usda': 'Molybdenum, Mo',
        'name_measuredfood': 'molybdenum',
        'default_unit': '\u00b5g',
    },
    {
        'name_usda': 'Cobal, Co',
        'name_measuredfood': 'cobalt',
        'default_unit': '\u00b5g',
    },
    {
        'name_usda': 'Boron, B',
        'name_measuredfood': 'boron',
        'default_unit': '\u00b5g',
    },
]

template_ingredient_property = [
    {
        'name_usda': '',
        'name_measuredfood': '',
        'default_unit': '',
    },
]

