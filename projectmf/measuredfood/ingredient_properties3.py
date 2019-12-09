# Some nutrient names describe section titles and can thus be ignored.

# The unit names from FoodData Central are used,
# see Foundation_api_food_details_endpoint_response.txt for example.

# In the FoodData Central database from the USDA, the data are formatted a
# certain way. They must be transformed so they fit into the measuredfood
# database. The mapping dictionary says which id in the USDA database
# corresponds to which key word in the measuredfood database.

# A list of nutrient names has been compiled from the documentations
# 2015_2016_FNDDS_Doc.pdf, Foundation+Foods+Documentation_FINAL+3-21-19.pdf and
# sr28_doc.pdf. The nutrient names from the documentation have been included
# as comments, so Sandor Clegane has a to-do list of all the nutrients. For
# each nutrient, the id_nutrient_usda_api,
# the nutrient_name_usda_api and the unit_nutrient_usda_api need to
# be found in the JSON data returned by the FoodData Central API.

ALL_NUTRIENTS_AND_DEFAULT_UNITS = [
    # Proximates  (from documentation)

    # water (moisture) (from documentation)
    {
        'id_nutrient_usda_api': '1051',
        'nutrient_name_usda_api': 'Water',
        'nutrient_name_measuredfood': 'water',
        'unit_nutrient_usda_api': 'g',
    },
    # protein (from documentation - all commented nutrients are from the
    # documentation)
    {
        'id_nutrient_usda_api': '1003',
        'nutrient_name_usda_api': 'Protein',
        'nutrient_name_measuredfood': 'protein',
        'unit_nutrient_usda_api': 'g',
    },
    # total lipid (fat)
    {
        'id_nutrient_usda_api': '1004',
        'nutrient_name_usda_api': 'Total lipid (fat)',
        'nutrient_name_measuredfood': 'fat_total',
        'unit_nutrient_usda_api': 'g',
    },

    # total carbohydrate (Section title, not nutrient in its own right.)
    # Carbohydrate by difference (contains fiber)
    {
        'id_nutrient_usda_api': '1005',
        'nutrient_name_usda_api': 'Carbohydrate, by difference',
        'nutrient_name_measuredfood':
            'carbohydrate_by_difference_including_fiber',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': False,
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },
    # ash
    {
        'id_nutrient_usda_api': '1007',
        'nutrient_name_usda_api': 'Ash',
        'nutrient_name_measuredfood': 'ash',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },
    # alcohol
    {
        'id_nutrient_usda_api': '1018',
        'nutrient_name_usda_api': 'Alcohol, ethyl',
        'nutrient_name_measuredfood': 'alcohol',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },
    # Sugars, total NLEA
    {
        'id_nutrient_usda_api': '2000',
        'nutrient_name_usda_api': 'Sugars, total including NLEA',
        'nutrient_name_measuredfood': 'sugars_total',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    # Food Energy - expressed in kcal and in kJ.
    # (Digestive and urinary losses are deducted.)
    {
        'id_nutrient_usda_api': '1008',
        'nutrient_name_usda_api': 'Energy',
        'nutrient_name_measuredfood': 'energy_kcal',
        'unit_nutrient_usda_api': 'kcal',
    },
    {
        'id_nutrient_usda_api': '1062',
        'nutrient_name_usda_api': 'Energy',
        'nutrient_name_measuredfood': 'energy_kilojoule',
        'unit_nutrient_usda_api': 'kJ',
    },

    # Fiber
    {
        'id_nutrient_usda_api': '1079',
        'nutrient_name_usda_api': 'Fiber, total dietary',
        'nutrient_name_measuredfood': 'fiber_total_dietary',
        'unit_nutrient_usda_api': 'g ',
    },
    # Starch
    {
        'id_nutrient_usda_api': '1009',
        'nutrient_name_usda_api': 'Starch',
        'nutrient_name_measuredfood': 'starch',
        'unit_nutrient_usda_api': 'g',
    },

    # Vitamins

    # ascorbic acid
    {
        'id_nutrient_usda_api': '1162',
        'nutrient_name_usda_api': 'Vitamin C, total ascorbic acid',
        'nutrient_name_measuredfood': 'vitamin_c',
        'unit_nutrient_usda_api': 'mg',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },
    # thiamin
    {
        'id_nutrient_usda_api': '1165',
        'nutrient_name_usda_api': 'Thiamin',
        'nutrient_name_measuredfood': 'thiamin',
        'unit_nutrient_usda_api': 'mg',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },
    # riboflavin
    {
        'id_nutrient_usda_api': '1166',
        'nutrient_name_usda_api': 'Riboflavin',
        'nutrient_name_measuredfood': 'riboflavin',
        'unit_nutrient_usda_api': '',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },
    #  niacin,
    {
        'id_nutrient_usda_api': '1167',
        'nutrient_name_usda_api': 'Niacin',
        'nutrient_name_measuredfood': 'niacin',
        'unit_nutrient_usda_api': 'mg',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },
    # pantothenic acid,
    {
        'id_nutrient_usda_api': '1170',
        'nutrient_name_usda_api': 'Pantothenic acid',
        'nutrient_name_measuredfood': 'pantothenic_acid',
        'unit_nutrient_usda_api': 'mg',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },
    # vitamin B 6
    {
        'id_nutrient_usda_api': '1175',
        'nutrient_name_usda_api': 'Vitamin B-6',
        'nutrient_name_measuredfood': 'vitamin_b6',
        'unit_nutrient_usda_api': 'mg',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },
    #  vitamin B 12
    {
        'id_nutrient_usda_api': '1178',
        'nutrient_name_usda_api': 'Vitamin B-12',
        'nutrient_name_measuredfood': 'vitamin_b12',
        'unit_nutrient_usda_api': '\u00b5g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },
    {
        'id_nutrient_usda_api': '1246',
        'nutrient_name_usda_api': 'Vitamin B-12, added',
        'nutrient_name_measuredfood': 'vitamin_b12_added',
        'unit_nutrient_usda_api': '\u00b5g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },
    # folate
    {
        'id_nutrient_usda_api': '1177',
        'nutrient_name_usda_api': 'Folate, total',
        'nutrient_name_measuredfood': 'folate_total',
        'unit_nutrient_usda_api': '\u00b5g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },
    # choline
    {
        'id_nutrient_usda_api': '1180',
        'nutrient_name_usda_api': 'Choline, total',
        'nutrient_name_measuredfood': 'choline_total',
        'unit_nutrient_usda_api': 'mg',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },
    # vitamin A
    {
        'id_nutrient_usda_api': '1106',
        'nutrient_name_usda_api': 'Vitamin A, RAE',
        'nutrient_name_measuredfood': 'vitamin_a_rae',
        'unit_nutrient_usda_api': '\u00b5g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },
    # vitamin D
    {
        'id_nutrient_usda_api': '1114',
        'nutrient_name_usda_api': 'Vitamin D (D2 + D3)',
        'nutrient_name_measuredfood': 'vitamin_d_d2_and_d3',
        'unit_nutrient_usda_api': '\u00b5g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },
    {
        'id_nutrient_usda_api': '1110',
        'nutrient_name_usda_api': 'Vitamin D',
        'nutrient_name_measuredfood': 'vitamin_d_iu',
        'unit_nutrient_usda_api': 'IU',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },
    # vitamin E
    {
        'id_nutrient_usda_api': '1109',
        'nutrient_name_usda_api': 'Vitamin E (alpha-tocopherol)',
        'nutrient_name_measuredfood': 'vitamin_e_alpha_tocopherol',
        'unit_nutrient_usda_api': 'mg',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },
    {
        'id_nutrient_usda_api': '1242',
        'nutrient_name_usda_api': 'Vitamin E, added',
        'nutrient_name_measuredfood': 'vitamin_e_added',
        'unit_nutrient_usda_api': 'mg',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },
    # vitamin K
    {
        'id_nutrient_usda_api': '1185',
        'nutrient_name_usda_api': 'Vitamin K (phylloquinone)',
        'nutrient_name_measuredfood': 'vitamin_k_phylloquinone',
        'unit_nutrient_usda_api': '\u00b5g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    # Minerals

    # boron
    {
        'id_nutrient_usda_api': '1137',
        'nutrient_name_usda_api': 'Boron, B',
        'nutrient_name_measuredfood': 'boron',
        'unit_nutrient_usda_api': '\u00b5g',
    },
    # calcium
    {
        'id_nutrient_usda_api': '1087',
        'nutrient_name_usda_api': 'Calcium, Ca',
        'nutrient_name_measuredfood': 'calcium',
        'unit_nutrient_usda_api': 'mg',
    },

    # cobalt
    {
        'id_nutrient_usda_api': '1097',
        'nutrient_name_usda_api': 'Cobalt, Co',
        'nutrient_name_measuredfood': 'cobalt',
        'unit_nutrient_usda_api': '\u00b5g',
    },
    # copper
    {
        'id_nutrient_usda_api': '1098',
        'nutrient_name_usda_api': 'Copper, Cu',
        'nutrient_name_measuredfood': 'copper',
        'unit_nutrient_usda_api': 'mg',
    },
    # fluoride
    {
        'id_nutrient_usda_api': '1099',
        'nutrient_name_usda_api': 'Fluoride, F',
        'nutrient_name_measuredfood': 'fluoride',
        'unit_nutrient_usda_api': '\u00b5g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },
    # iron
    {
        'id_nutrient_usda_api': '1089',
        'nutrient_name_usda_api': 'Iron, Fe',
        'nutrient_name_measuredfood': 'iron',
        'unit_nutrient_usda_api': 'mg',
    },
    # magnesium
    {
        'id_nutrient_usda_api': '1090',
        'nutrient_name_usda_api': 'Magnesium, Mg',
        'nutrient_name_measuredfood': 'magnesium',
        'unit_nutrient_usda_api': 'mg',
    },
    # manganese
    {
        'id_nutrient_usda_api': '1101',
        'nutrient_name_usda_api': 'Manganese, Mn',
        'nutrient_name_measuredfood': 'manganese',
        'unit_nutrient_usda_api': 'mg',
    },
    # molybdenum
    {
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': 'Molybdenum, Mo',
        'nutrient_name_measuredfood': 'molybdenum',
        'unit_nutrient_usda_api': '\u00b5g',
    },
    # nickel
    {
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': 'Nickel, Ni',
        'nutrient_name_measuredfood': 'nickel',
        'unit_nutrient_usda_api': '\u00b5g',
    },
    # phosphorus
    {
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': 'Phosphorus, P',
        'nutrient_name_measuredfood': 'phosphorus',
        'unit_nutrient_usda_api': 'mg',
    },
    # potassium
    {
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': 'Potassium, K',
        'nutrient_name_measuredfood': 'potassium',
        'unit_nutrient_usda_api': 'mg',
    },
    # selenium
    # sodium
    # sulfur
    {
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': 'Sulfur, S',
        'nutrient_name_measuredfood': 'sulfur',
        'unit_nutrient_usda_api': 'mg',
    },
    # zinc
    {
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': 'Zinc, Zn',
        'nutrient_name_measuredfood': 'zinc',
        'unit_nutrient_usda_api': 'mg',
    },


    # Lipids

    # Fatty acid
    # Saturated fatty acids
    # 4:0
    # 6:0
    # 8:0
    # 10:0
    # 12:0
    # 13:0
    # 14:0
    # 15:0
    # 16:0
    # 17:0
    # 18:0
    # 20:0
    # 22:0
    # 24:0
    # Monounsaturated fatty acids
    # 14:1
    # 15:1
    # 16:1 undifferentiated
    # 16:1 cis*
    # 17:1
    # 18:1 undifferentiated
    # 18:1 cis*
    # 20:1
    # 22:1 undifferentiated
    # 22:1 cis*
    # 24:1 cis
    # Polyunsaturated fatty acids
    # 18:2 undifferentiated
    # 18:2 i (mixed isomers)
    # 18:2 n-6 cis, cis*
    # 18:2 conjugated linoleic acid
    # 18:3 undifferentiated
    # 18:3 n-3 cis, cis, cis*
    # 18:3 n-6 cis, cis, cis
    # 18:3 i (mixed isomers)
    # 18:4
    # 20:2 n-6 cis, cis
    # 20:3 undifferentiated

    # Fatty acid
    # 20:3 n-3
    # 20:3 n-6
    # 20:4 undifferentiated
    # 20:4 n-6*
    # 20:5 n-3
    # 21:5
    # 22:4
    # 22:5 n-3
    # 22:6 n-3

    # Trans fatty acids
    # Fatty acids, total trans-monoenoic
    # 16:1 trans
    # 18:1 trans
    # 22:1 trans
    # Fatty acids, total trans-polyenoic
    # 18:2 trans not further defined
    # 18:2 trans, trans



















]

# The displayed_in_list_of_percentages is a True or False value, determining
# whether the nutrient shows up in the list of percentages of daily targets.
# Placeholder properties a and b were added, since it is likely that new
# properties will be desired and it is cumbersome to paste them into every
# dictionary individually. If they are not needed, they can be deleted in the
# end.

template_ingredient_property = [
    {
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': '',
        'nutrient_name_measuredfood': '',
        'unit_nutrient_usda_api': '',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },
]

