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
# as keyword value entries in the dictionaries, so Sandor Clegane has a to-do
# list of
# all the nutrients. For
# each nutrient, the id_nutrient_usda_api,
# the nutrient_name_usda_api and the unit_nutrient_usda_api need to
# be found in the JSON data returned by the FoodData Central API.

ALL_NUTRIENTS_AND_DEFAULT_UNITS = [

    # Proximates  (SECTION, not nutrient) (from documentation)

    {
        'nutrient_name_documentation': 'water (moisture)',
        'id_nutrient_usda_api': '1051',
        'nutrient_name_usda_api': 'Water',
        'nutrient_name_measuredfood': 'water',
        'unit_nutrient_usda_api': 'g',
    },

    {
        'nutrient_name_documentation': 'protein',
        'id_nutrient_usda_api': '1003',
        'nutrient_name_usda_api': 'Protein',
        'nutrient_name_measuredfood': 'protein',
        'unit_nutrient_usda_api': 'g',
    },

    {
        'nutrient_name_documentation': 'total lipid (fat)',
        'id_nutrient_usda_api': '1004',
        'nutrient_name_usda_api': 'Total lipid (fat)',
        'nutrient_name_measuredfood': 'fat_total',
        'unit_nutrient_usda_api': 'g',
    },

    # total carbohydrate (Section title, not nutrient in its own right.)

    # contains fiber
    {
        'nutrient_name_documentation': 'Carbohydrate by difference',
        'id_nutrient_usda_api': '1005',
        'nutrient_name_usda_api': 'Carbohydrate, by difference',
        'nutrient_name_measuredfood':
            'carbohydrate_by_difference_including_fiber',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': False,
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': 'ash',
        'id_nutrient_usda_api': '1007',
        'nutrient_name_usda_api': 'Ash',
        'nutrient_name_measuredfood': 'ash',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': 'alcohol',
        'id_nutrient_usda_api': '1018',
        'nutrient_name_usda_api': 'Alcohol, ethyl',
        'nutrient_name_measuredfood': 'alcohol',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': 'Sugars, total NLEA',
        'id_nutrient_usda_api': '2000',
        'nutrient_name_usda_api': 'Sugars, total including NLEA',
        'nutrient_name_measuredfood': 'sugars_total',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation':
            'Food Energy - expressed in kcal. '
            'Digestive and urinary losses are deducted.',
        'id_nutrient_usda_api': '1008',
        'nutrient_name_usda_api': 'Energy',
        'nutrient_name_measuredfood': 'energy_kcal',
        'unit_nutrient_usda_api': 'kcal',
    },
    {
        'nutrient_name_documentation':
            'Food Energy - expressed in kJ'
            'Digestive and urinary losses are deducted.',
        'id_nutrient_usda_api': '1062',
        'nutrient_name_usda_api': 'Energy',
        'nutrient_name_measuredfood': 'energy_kilojoule',
        'unit_nutrient_usda_api': 'kJ',
    },

    {
        'nutrient_name_documentation': 'Fiber',
        'id_nutrient_usda_api': '1079',
        'nutrient_name_usda_api': 'Fiber, total dietary',
        'nutrient_name_measuredfood': 'fiber_total_dietary',
        'unit_nutrient_usda_api': 'g ',
    },

    {
        'nutrient_name_documentation': 'Starch',
        'id_nutrient_usda_api': '1009',
        'nutrient_name_usda_api': 'Starch',
        'nutrient_name_measuredfood': 'starch',
        'unit_nutrient_usda_api': 'g',
    },

    # Vitamins (section title, not nutrient)

    {
        'nutrient_name_documentation': 'ascorbic acid',
        'id_nutrient_usda_api': '1162',
        'nutrient_name_usda_api': 'Vitamin C, total ascorbic acid',
        'nutrient_name_measuredfood': 'vitamin_c',
        'unit_nutrient_usda_api': 'mg',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': 'thiamin',
        'id_nutrient_usda_api': '1165',
        'nutrient_name_usda_api': 'Thiamin',
        'nutrient_name_measuredfood': 'thiamin',
        'unit_nutrient_usda_api': 'mg',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': 'riboflavin',
        'id_nutrient_usda_api': '1166',
        'nutrient_name_usda_api': 'Riboflavin',
        'nutrient_name_measuredfood': 'riboflavin',
        'unit_nutrient_usda_api': '',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': 'niacin',
        'id_nutrient_usda_api': '1167',
        'nutrient_name_usda_api': 'Niacin',
        'nutrient_name_measuredfood': 'niacin',
        'unit_nutrient_usda_api': 'mg',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': 'pantothenic acid',
        'id_nutrient_usda_api': '1170',
        'nutrient_name_usda_api': 'Pantothenic acid',
        'nutrient_name_measuredfood': 'pantothenic_acid',
        'unit_nutrient_usda_api': 'mg',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': 'vitamin B 6',
        'id_nutrient_usda_api': '1175',
        'nutrient_name_usda_api': 'Vitamin B-6',
        'nutrient_name_measuredfood': 'vitamin_b6',
        'unit_nutrient_usda_api': 'mg',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': 'vitamin B 12',
        'id_nutrient_usda_api': '1178',
        'nutrient_name_usda_api': 'Vitamin B-12',
        'nutrient_name_measuredfood': 'vitamin_b12',
        'unit_nutrient_usda_api': '\u00b5g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '',
        'id_nutrient_usda_api': '1246',
        'nutrient_name_usda_api': 'Vitamin B-12, added',
        'nutrient_name_measuredfood': 'vitamin_b12_added',
        'unit_nutrient_usda_api': '\u00b5g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': 'folate',
        'id_nutrient_usda_api': '1177',
        'nutrient_name_usda_api': 'Folate, total',
        'nutrient_name_measuredfood': 'folate_total',
        'unit_nutrient_usda_api': '\u00b5g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': 'choline',
        'id_nutrient_usda_api': '1180',
        'nutrient_name_usda_api': 'Choline, total',
        'nutrient_name_measuredfood': 'choline_total',
        'unit_nutrient_usda_api': 'mg',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': 'vitamin A',
        'id_nutrient_usda_api': '1106',
        'nutrient_name_usda_api': 'Vitamin A, RAE',
        'nutrient_name_measuredfood': 'vitamin_a_rae',
        'unit_nutrient_usda_api': '\u00b5g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': 'vitamin D \u00b5g',
        'id_nutrient_usda_api': '1114',
        'nutrient_name_usda_api': 'Vitamin D (D2 + D3)',
        'nutrient_name_measuredfood': 'vitamin_d_d2_and_d3',
        'unit_nutrient_usda_api': '\u00b5g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': 'vitamin D IU',
        'id_nutrient_usda_api': '1110',
        'nutrient_name_usda_api': 'Vitamin D',
        'nutrient_name_measuredfood': 'vitamin_d_iu',
        'unit_nutrient_usda_api': 'IU',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': 'vitamin E',
        'id_nutrient_usda_api': '1109',
        'nutrient_name_usda_api': 'Vitamin E (alpha-tocopherol)',
        'nutrient_name_measuredfood': 'vitamin_e_alpha_tocopherol',
        'unit_nutrient_usda_api': 'mg',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },
    {
        'nutrient_name_documentation': 'vitamin E added',
        'id_nutrient_usda_api': '1242',
        'nutrient_name_usda_api': 'Vitamin E, added',
        'nutrient_name_measuredfood': 'vitamin_e_added',
        'unit_nutrient_usda_api': 'mg',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': 'vitamin K',
        'id_nutrient_usda_api': '1185',
        'nutrient_name_usda_api': 'Vitamin K (phylloquinone)',
        'nutrient_name_measuredfood': 'vitamin_k_phylloquinone',
        'unit_nutrient_usda_api': '\u00b5g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    # Minerals (section title, not nutrient)

    {
        'nutrient_name_documentation': 'boron',
        'id_nutrient_usda_api': '1137',
        'nutrient_name_usda_api': 'Boron, B',
        'nutrient_name_measuredfood': 'boron',
        'unit_nutrient_usda_api': '\u00b5g',
    },

    {
        'nutrient_name_documentation': 'calcium',
        'id_nutrient_usda_api': '1087',
        'nutrient_name_usda_api': 'Calcium, Ca',
        'nutrient_name_measuredfood': 'calcium',
        'unit_nutrient_usda_api': 'mg',
    },

    {
        'nutrient_name_documentation': 'cobalt',
        'id_nutrient_usda_api': '1097',
        'nutrient_name_usda_api': 'Cobalt, Co',
        'nutrient_name_measuredfood': 'cobalt',
        'unit_nutrient_usda_api': '\u00b5g',
    },

    {
        'nutrient_name_documentation': 'copper',
        'id_nutrient_usda_api': '1098',
        'nutrient_name_usda_api': 'Copper, Cu',
        'nutrient_name_measuredfood': 'copper',
        'unit_nutrient_usda_api': 'mg',
    },

    {
        'nutrient_name_documentation': 'fluoride',
        'id_nutrient_usda_api': '1099',
        'nutrient_name_usda_api': 'Fluoride, F',
        'nutrient_name_measuredfood': 'fluoride',
        'unit_nutrient_usda_api': '\u00b5g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': 'iron',
        'id_nutrient_usda_api': '1089',
        'nutrient_name_usda_api': 'Iron, Fe',
        'nutrient_name_measuredfood': 'iron',
        'unit_nutrient_usda_api': 'mg',
    },

    {
        'nutrient_name_documentation': 'magnesium',
        'id_nutrient_usda_api': '1090',
        'nutrient_name_usda_api': 'Magnesium, Mg',
        'nutrient_name_measuredfood': 'magnesium',
        'unit_nutrient_usda_api': 'mg',
    },

    {
        'nutrient_name_documentation': 'manganese',
        'id_nutrient_usda_api': '1101',
        'nutrient_name_usda_api': 'Manganese, Mn',
        'nutrient_name_measuredfood': 'manganese',
        'unit_nutrient_usda_api': 'mg',
    },

    {
        'nutrient_name_documentation': 'molybdenum',
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': 'Molybdenum, Mo',
        'nutrient_name_measuredfood': 'molybdenum',
        'unit_nutrient_usda_api': '\u00b5g',
    },

    {
        'nutrient_name_documentation': 'nickel',
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': 'Nickel, Ni',
        'nutrient_name_measuredfood': 'nickel',
        'unit_nutrient_usda_api': '\u00b5g',
    },

    {
        'nutrient_name_documentation': 'phosphorus',
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': 'Phosphorus, P',
        'nutrient_name_measuredfood': 'phosphorus',
        'unit_nutrient_usda_api': 'mg',
    },

    {
        'nutrient_name_documentation': 'potassium',
        'id_nutrient_usda_api': '1092',
        'nutrient_name_usda_api': 'Potassium, K',
        'nutrient_name_measuredfood': 'potassium',
        'unit_nutrient_usda_api': 'mg',
    },

    {
        'nutrient_name_documentation': 'selenium',
        'id_nutrient_usda_api': '1103',
        'nutrient_name_usda_api': 'Selenium, Se',
        'nutrient_name_measuredfood': 'selenium',
        'unit_nutrient_usda_api': '\u00b5g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': 'sodium',
        'id_nutrient_usda_api': '1093',
        'nutrient_name_usda_api': 'Sodium, Na',
        'nutrient_name_measuredfood': 'sodium',
        'unit_nutrient_usda_api': 'mg',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': 'sulfur',
        'id_nutrient_usda_api': '1094',
        'nutrient_name_usda_api': 'Sulfur, S',
        'nutrient_name_measuredfood': 'sulfur',
        'unit_nutrient_usda_api': 'mg',
    },

    {
        'nutrient_name_documentation': 'zinc',
        'id_nutrient_usda_api': '1095',
        'nutrient_name_usda_api': 'Zinc, Zn',
        'nutrient_name_measuredfood': 'zinc',
        'unit_nutrient_usda_api': 'mg',
    },


    # Lipids (section title not nutrient)

    {
        'nutrient_name_documentation': 'Saturated fatty acids',
        'id_nutrient_usda_api': '1258',
        'nutrient_name_usda_api': 'Fatty acids, total saturated',
        'nutrient_name_measuredfood': 'fatty_acids_total_saturated',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '4:0',
        'id_nutrient_usda_api': '1259',
        'nutrient_name_usda_api': '4:0',
        'nutrient_name_measuredfood': 'fatty_acid_4_0',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '6:0',
        'id_nutrient_usda_api': '1260',
        'nutrient_name_usda_api': '6:0',
        'nutrient_name_measuredfood': 'fatty_acid_6_0',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': ' 8:0',
        'id_nutrient_usda_api': '1261',
        'nutrient_name_usda_api': '8:0',
        'nutrient_name_measuredfood': 'fatty_acid_8_0',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '10:0',
        'id_nutrient_usda_api': '1262',
        'nutrient_name_usda_api': '10:0',
        'nutrient_name_measuredfood': 'fatty_acid_10_0',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '12:0',
        'id_nutrient_usda_api': '1263',
        'nutrient_name_usda_api': '12:0',
        'nutrient_name_measuredfood': 'fatty_acid_12_0',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '13:0',
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': '',
        'nutrient_name_measuredfood': '',
        'unit_nutrient_usda_api': '',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '14:0',
        'id_nutrient_usda_api': '1264',
        'nutrient_name_usda_api': '14:0',
        'nutrient_name_measuredfood': 'fatty_acid_14_0',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '15:0',
        'id_nutrient_usda_api': '1299',
        'nutrient_name_usda_api': '15:0',
        'nutrient_name_measuredfood': 'fatty_acid_15_0',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '16:0',
        'id_nutrient_usda_api': '1265',
        'nutrient_name_usda_api': '16:0',
        'nutrient_name_measuredfood': 'fatty_acid_16_0',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '17:0',
        'id_nutrient_usda_api': '1300',
        'nutrient_name_usda_api': '17:0',
        'nutrient_name_measuredfood': 'fatty_acid_17_0',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '18:0',
        'id_nutrient_usda_api': '1266',
        'nutrient_name_usda_api': '18:0',
        'nutrient_name_measuredfood': 'fatty_acid_18_0',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '20:0',
        'id_nutrient_usda_api': '1267',
        'nutrient_name_usda_api': '20:0',
        'nutrient_name_measuredfood': 'fatty_acid_20_0',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '22:0',
        'id_nutrient_usda_api': '1273',
        'nutrient_name_usda_api': '22:0',
        'nutrient_name_measuredfood': 'fatty_acid_22_0',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    # not included in canola oil.
    {
        'nutrient_name_documentation': '24:0',
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': '24:0',
        'nutrient_name_measuredfood': 'fatty_acid_24_0',
        'unit_nutrient_usda_api': '',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': 'Monounsaturated fatty acids',
        'id_nutrient_usda_api': '1292',
        'nutrient_name_usda_api': 'Fatty acids, total monounsaturated',
        'nutrient_name_measuredfood': 'fatty_acids_total_monounsaturated',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '14:1',
        'id_nutrient_usda_api': '1274',
        'nutrient_name_usda_api': '14:1',
        'nutrient_name_measuredfood': 'fatty_acid_14_1',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '15:1',
        'id_nutrient_usda_api': '1333',
        'nutrient_name_usda_api': '15:1',
        'nutrient_name_measuredfood': 'fatty_acid_15_1',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '16:1 undifferentiated',
        'id_nutrient_usda_api': '1275',
        'nutrient_name_usda_api': '16:1',
        'nutrient_name_measuredfood': 'fatty_acid_16_1',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    # # not included in canola oil.
    {
        'nutrient_name_documentation': '16:1 cis*',
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': '',
        'nutrient_name_measuredfood': '',
        'unit_nutrient_usda_api': '',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '17:1',
        'id_nutrient_usda_api': '1323',
        'nutrient_name_usda_api': '17:1',
        'nutrient_name_measuredfood': 'fatty_acid_17_1',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '18:1 undifferentiated',
        'id_nutrient_usda_api': '1268',
        'nutrient_name_usda_api': '18:1',
        'nutrient_name_measuredfood': 'fatty_acid_18_1',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '18:1 cis*',
        'id_nutrient_usda_api': '1315',
        'nutrient_name_usda_api': '18:1 c',
        'nutrient_name_measuredfood': 'fatty_acid_18_1_c',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '20:1',
        'id_nutrient_usda_api': '1277',
        'nutrient_name_usda_api': '20:1',
        'nutrient_name_measuredfood': 'fatty_acid_20_1',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '22:1 undifferentiated',
        'id_nutrient_usda_api': '1279',
        'nutrient_name_usda_api': '22:1',
        'nutrient_name_measuredfood': 'fatty_acid_22_1',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    # # not in canola oil.
    {
        'nutrient_name_documentation': '22:1 cis*',
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': '',
        'nutrient_name_measuredfood': '',
        'unit_nutrient_usda_api': '',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    # # not in canola oil
    {
        'nutrient_name_documentation': '24:1 cis',
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': '24:1',
        'nutrient_name_measuredfood': 'fatty_acid_24_1',
        'unit_nutrient_usda_api': '',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': 'Polyunsaturated fatty acids',
        'id_nutrient_usda_api': '1293',
        'nutrient_name_usda_api': 'Fatty acids, total polyunsaturated',
        'nutrient_name_measuredfood': 'fatty_acids_total_polyunsaturated',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '18:2 undifferentiated',
        'id_nutrient_usda_api': '1269',
        'nutrient_name_usda_api': '18:2',
        'nutrient_name_measuredfood': 'fatty_acid_18_2',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    # not in canola oil
    {
        'nutrient_name_documentation': '18:2 i (mixed isomers)',
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': '',
        'nutrient_name_measuredfood': '',
        'unit_nutrient_usda_api': '',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '18:2 n-6 cis, cis*',
        'id_nutrient_usda_api': '1316',
        'nutrient_name_usda_api': '18:2 n-6 c,c',
        'nutrient_name_measuredfood': 'fatty_acid_n_6_c_c',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    # not in canola oil.
    {
        'nutrient_name_documentation': '18:2 conjugated linoleic acid',
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': '',
        'nutrient_name_measuredfood': '',
        'unit_nutrient_usda_api': '',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '18:3 undifferentiated',
        'id_nutrient_usda_api': '1270',
        'nutrient_name_usda_api': '18:3',
        'nutrient_name_measuredfood': 'fatty_acid_18_3',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '18:3 n-3 cis, cis, cis*',
        'id_nutrient_usda_api': '1404',
        'nutrient_name_usda_api': '18:3 n-3 c,c,c (ALA)',
        'nutrient_name_measuredfood': 'fatty_acid_n_3_c_c_c_ALA',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '18:3 n-6 cis, cis, cis',
        'id_nutrient_usda_api': '1321',
        'nutrient_name_usda_api': '18:3 n-6 c,c,c',
        'nutrient_name_measuredfood': 'fatty_acid_18_3_c_c_c',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    # not found in canola oil.
    {
        'nutrient_name_documentation': '18:3 i (mixed isomers)',
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': '',
        'nutrient_name_measuredfood': '',
        'unit_nutrient_usda_api': '',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '18:4',
        'id_nutrient_usda_api': '1276',
        'nutrient_name_usda_api': '18:4',
        'nutrient_name_measuredfood': 'fatty_acid_18_4',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '20:2 n-6 cis, cis',
        'id_nutrient_usda_api': '1313',
        'nutrient_name_usda_api': '20:2 n-6 c,c',
        'nutrient_name_measuredfood': 'fatty_acid_20_2_n_6_c_c',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '20:3 undifferentiated',
        'id_nutrient_usda_api': '1325',
        'nutrient_name_usda_api': '20:3',
        'nutrient_name_measuredfood': 'fatty_acid_20_3',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    # not found in canola oil.
    {
        'nutrient_name_documentation': '20:3 n-3',
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': '',
        'nutrient_name_measuredfood': '',
        'unit_nutrient_usda_api': '',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    # not found in canola oil.
    {
        'nutrient_name_documentation': '20:3 n-6',
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': '',
        'nutrient_name_measuredfood': '',
        'unit_nutrient_usda_api': '',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '20:4 undifferentiated',
        'id_nutrient_usda_api': '1271',
        'nutrient_name_usda_api': '20:4',
        'nutrient_name_measuredfood': 'fatty_acid_20_4',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    # not found in canola oil.
    {
        'nutrient_name_documentation': '20:4 n-6*',
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': '',
        'nutrient_name_measuredfood': '',
        'unit_nutrient_usda_api': '',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '20:5 n-3',
        'id_nutrient_usda_api': '1278',
        'nutrient_name_usda_api': '20:5 n-3 (EPA)',
        'nutrient_name_measuredfood': 'fatty_acid_20_5_n_3_EPA',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    # not found in canola oil.
    {
        'nutrient_name_documentation': '21:5',
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': '',
        'nutrient_name_measuredfood': '',
        'unit_nutrient_usda_api': '',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    # not found in canola oil
    {
        'nutrient_name_documentation': '22:4',
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': '',
        'nutrient_name_measuredfood': '',
        'unit_nutrient_usda_api': '',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '22:5 n-3',
        'id_nutrient_usda_api': '1280',
        'nutrient_name_usda_api': '22:5 n-3 (DPA)',
        'nutrient_name_measuredfood': 'fatty_acid_22_5_n_3_DPA',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '22:6 n-3',
        'id_nutrient_usda_api': '1272',
        'nutrient_name_usda_api': '22:6 n-3 (DHA)',
        'nutrient_name_measuredfood': 'fatty_acid_22_6_n_3_DHA',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': 'Fatty acids, total trans',
        'id_nutrient_usda_api': '1257',
        'nutrient_name_usda_api': 'Fatty acids, total trans',
        'nutrient_name_measuredfood': 'fatty_acids_total_trans',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': 'Fatty acids, total trans-monoenoic',
        'id_nutrient_usda_api': '1329',
        'nutrient_name_usda_api': 'Fatty acids, total trans-monoenoic',
        'nutrient_name_measuredfood': 'fatty_acids_total_trans-monoenoic',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    # not in canola oil.
    {
        'nutrient_name_documentation': '16:1 trans',
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': '',
        'nutrient_name_measuredfood': '',
        'unit_nutrient_usda_api': '',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '18:1 trans',
        'id_nutrient_usda_api': '1304',
        'nutrient_name_usda_api': '18:1 t',
        'nutrient_name_measuredfood': 'fatty_acid_18_1_t',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    # not in canola.
    {
        'nutrient_name_documentation': '22:1 trans',
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': '',
        'nutrient_name_measuredfood': '',
        'unit_nutrient_usda_api': '',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': 'Fatty acids, total trans-polyenoic',
        'id_nutrient_usda_api': '1331',
        'nutrient_name_usda_api': 'Fatty acids, total trans-polyenoic',
        'nutrient_name_measuredfood': 'fatty_acids_total_trans-polyenoic',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    # not in canola.
    {
        'nutrient_name_documentation': '18:2 trans not further defined',
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': '',
        'nutrient_name_measuredfood': '',
        'unit_nutrient_usda_api': '',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },

    {
        'nutrient_name_documentation': '18:2 trans, trans',
        'id_nutrient_usda_api': '1310',
        'nutrient_name_usda_api': '18:2 t,t',
        'nutrient_name_measuredfood': 'fatty_acid_18_2_t_t',
        'unit_nutrient_usda_api': 'g',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },
]

# The displayed_in_list_of_percentages is a True or False value, determining
# whether the nutrient shows up in the list of percentages of daily targets.
# Placeholder properties a and b were added, since it is likely that new
# properties will be desired and it is cumbersome to paste them into every
# dictionary individually. If they are not needed, they can be deleted in the
# end.

template_ingredient_property = [
    {
        'nutrient_name_documentation': '',
        'id_nutrient_usda_api': '',
        'nutrient_name_usda_api': '',
        'nutrient_name_measuredfood': '',
        'unit_nutrient_usda_api': '',
        'displayed_in_list_of_percentages': '',
        'placeholder_property_a': '',
        'placeholder_property_b': '',
    },
]
