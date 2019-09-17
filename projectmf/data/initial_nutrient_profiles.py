# The template does not yet contain any units. The default units are used.

template_nutrient_profile = [
    # {
    #     'name': None,
    #     'calories': None,  # 'default_unit': 'kcal'
    #     'carbohydrates': None,  # 'default_unit': 'gram'
    #     'fat': None,  # 'default_unit': 'gram'
    #     'protein': None,  # 'default_unit': 'gram'
    #     'linoleic_acid': None,  # 'default_unit': 'gram'
    #     'alpha_linoleic_acid': None,  # 'default_unit': 'gram'
    #     # Vitamin A unit conversion:
    #     # Vitamin A: 1 IU is the biological equivalent of 0.3 mcg retinol,
    #     # or of 0.6 mcg beta-carotene
    #     # Source: https://dietarysupplementdatabase.usda.nih.gov/
    #     # ingredient_calculator/help.php
    #     # => * 0.3
    #     'vitamin_a': None,  # 'default_unit': 'microgram'.
    #     'vitamin_c': None,  # 'default_unit': 'milligram'
    #     'vitamin_d': None,  # 'default_unit': 'microgram'
    #     'vitamin_e': None,  # 'default_unit': 'milligram'
    #     'vitamin_k': None,  # 'default_unit': 'microgram'
    #     'thiamin': None,  # 'default_unit': 'milligram'
    #     'riboflavin': None,  # 'default_unit': 'milligram'
    #     'niacin': None,  # 'default_unit': 'milligram'
    #     'vitamin_b6': None,  # 'default_unit': 'milligram'
    #     'folate': None,  # 'default_unit': 'microgram'
    #     'vitamin_b12': None,  # 'default_unit': 'microgram'
    #     'pantothenic_acid': None,  # 'default_unit': 'milligram'
    #     'biotin': None,  # 'default_unit': 'microgram'
    #     'choline': None,  # 'default_unit': 'milligram'
    #     'calcium': None,  # 'default_unit': 'milligram'
    #     'chromium': None,  # 'default_unit': 'microgram'
    #     'copper': None,  # 'default_unit': 'microgram'
    #     'iodine': None,  # 'default_unit': 'microgram'
    #     'iron': None,  # 'default_unit': 'milligram'
    #     'magnesium': None,  # 'default_unit': 'milligram'
    #     'manganese': None,  # 'default_unit': 'milligram'
    #     'molybdenum': None,  # 'default_unit': 'microgram'
    #     'phosphorus': None,  # 'default_unit': 'milligram'
    #     'selenium': None,  # 'default_unit': 'microgram'
    #     'zinc': None,  # 'default_unit': 'milligram'
    #     'potassium': None,  # 'default_unit': 'gram'
    #     'sodium': None,  # 'default_unit': 'gram'
    #     'chloride': None,  # 'default_unit': 'gram'

    # # Maximum amounts (i.e. tolerable upper intake)
    #     'max_calories': None,  # 'default_unit': 'kcal'
    #     'max_carbohydrates': None,  # 'default_unit': 'gram'
    #     'max_fat': None,  # 'default_unit': 'gram'
    #     'max_protein': None,  # 'default_unit': 'gram'
    #     'max_linoleic_acid': None,  # 'default_unit': 'gram'
    #     'max_alpha_linoleic_acid': None,  # 'default_unit': 'gram'
    #     # Vitamin A unit conversion:
    #     # Vitamin A: 1 IU is the biological equivalent of 0.3 mcg retinol,
    #     # or of 0.6 mcg beta-carotene
    #     # Source: https://dietarysupplementdatabase.usda.nih.gov/
    #     # ingredient_calculator/help.php
    #     # => * 0.3
    #     'max_vitamin_a': None,  # 'default_unit': 'microgram'.
    #     'max_vitamin_c': None,  # 'default_unit': 'milligram'
    #     'max_vitamin_d': None,  # 'default_unit': 'microgram'
    #     'max_vitamin_e': None,  # 'default_unit': 'milligram'
    #     'max_vitamin_k': None,  # 'default_unit': 'microgram'
    #     'max_thiamin': None,  # 'default_unit': 'milligram'
    #     'max_riboflavin': None,  # 'default_unit': 'milligram'
    #     'max_niacin': None,  # 'default_unit': 'milligram'
    #     'max_vitamin_b6': None,  # 'default_unit': 'milligram'
    #     'max_folate': None,  # 'default_unit': 'microgram'
    #     'max_vitamin_b12': None,  # 'default_unit': 'microgram'
    #     'max_pantothenic_acid': None,  # 'default_unit': 'milligram'
    #     'max_biotin': None,  # 'default_unit': 'microgram'
    #     'max_choline': None,  # 'default_unit': 'milligram'
    #     'max_calcium': None,  # 'default_unit': 'milligram'
    #     'max_chromium': None,  # 'default_unit': 'microgram'
    #     'max_copper': None,  # 'default_unit': 'microgram'
    #     'max_iodine': None,  # 'default_unit': 'microgram'
    #     'max_iron': None,  # 'default_unit': 'milligram'
    #     'max_magnesium': None,  # 'default_unit': 'milligram'
    #     'max_manganese': None,  # 'default_unit': 'milligram'
    #     'max_molybdenum': None,  # 'default_unit': 'microgram'
    #     'max_phosphorus': None,  # 'default_unit': 'milligram'
    #     'max_selenium': None,  # 'default_unit': 'microgram'
    #     'max_zinc': None,  # 'default_unit': 'milligram'
    #     'max_potassium': None,  # 'default_unit': 'gram'
    #     'max_sodium': None,  # 'default_unit': 'gram'
    #     'max_chloride': None,  # 'default_unit': 'gram'
    # },
]

# The first nutrient profile in nutrient_profile_dict_list is used in the tests.

nutrient_profile_dict_list = [
    # {
    #     'name': 'Maintenance plus vitamins from NIH Males 19-30',
    #     # sources:
    #     # https://www.ncbi.nlm.nih.gov/books/
    #     # NBK56068/
    #     # table/summarytables.t3/?report=objectonly
    #     # https://www.ncbi.nlm.nih.gov/books/
    #     # NBK56068/table/summarytables.t2/?report=objectonly
    #     'calories': 2500,
    #     'fat': 72,
    #     'protein': 164,
    #     # Vitamins
    #     # vitamin a was converted from micrograms based on
    #     # https://www.thecalculatorsite.com/articles/units/convert-ui-to-mcg.php
    #     'vitamin_a': 3000,
    #     'vitamin_c': 90,
    #     # vitamin d unit conversion was done on the same website were the value
    #     # came from
    #     'vitamin_d': 600,
    #     'vitamin_e': 15,
    #     'vitamin_k': 120,
    #     'thiamin': 1.2,
    #     'riboflavin': 1.3,
    #     'niacin': 16,
    #     'vitamin_b6': 1.3,
    #     'folate': 400,
    #     'vitamin_b12': 2.4,
    #     'pantothenic_acid': 5,
    #     # Minerals
    #     'calcium': 1000,
    #     'iron': 8,
    #     'magnesium': 400,
    #     'phosphorus': 700,
    #     'potassium': 4700,
    #     'sodium': 1500,
    #     'zinc': 11,
    #     'copper': 0.900,
    #     'manganese': 2.3,
    #     'selenium': 55,
    #     'biotin': 30,
    #     'choline': 550,
    #     'chloride': 2.3,
    #     'chromium': 35,
    #     'iodine': 150,
    #     'molybdenum': 45,
    # },
    # {
    #     'name': 'Second nutrient profile placeholder',
    # },
    {
        'name': 'Maintenance EU',
        # source:
        #  https://www.efsa.europa.eu/en/interactive-pages/drvs
        'calories': 2500,  # 'default_unit': 'kcal'
        'carbohydrates': None,  # 'default_unit': 'gram'
        'fat': None,  # 'default_unit': 'gram'
        'protein': 164,  # 'default_unit': 'gram'
        # The values for linoleic acid and alpha linoleic acid were given as
        # percentages of total energy intake. I went with values that I had
        # noted in food_numbers_object_oriented that were taken from wikipedia.
        'linoleic_acid': 17,  # 'default_unit': 'gram'
        'alpha_linoleic_acid': 1.6,  # 'default_unit': 'gram'
        # Vitamin A unit conversion:
        # Vitamin A: 1 IU is the biological equivalent of 0.3 mcg retinol,
        # or of 0.6 mcg beta-carotene
        # Source: https://dietarysupplementdatabase.usda.nih.gov/
        # ingredient_calculator/help.php
        # => * 0.3
        'vitamin_a': 750,  # 'default_unit': 'microgram'.
        'vitamin_c': 110,  # 'default_unit': 'milligram'
        'vitamin_d': 15,  # 'default_unit': 'microgram'
        'vitamin_e': 13,  # 'default_unit': 'milligram'
        'vitamin_k': 70,  # 'default_unit': 'microgram'
        # Thiamin intake is dependent on caloric intake. Went with a value on
        # the high side for 3500 kcal.
        'thiamin': 1.5,  # 'default_unit': 'milligram'
        'riboflavin': 1.6,  # 'default_unit': 'milligram'
        # Niacin intake is dependent on caloric intake. Went with a value on
        # the high side for 3500 kcal.
        'niacin': 24,  # 'default_unit': 'milligram'
        'vitamin_b6': 1.7,  # 'default_unit': 'milligram'
        'folate': 330,  # 'default_unit': 'microgram'
        'vitamin_b12': 4,  # 'default_unit': 'microgram'
        'pantothenic_acid': 5,  # 'default_unit': 'milligram'
        'biotin': 40,  # 'default_unit': 'microgram'
        'choline': 400,  # 'default_unit': 'milligram'
        'calcium': 950,  # 'default_unit': 'milligram'
        'chromium': None,  # 'default_unit': 'microgram'
        'copper': 1600,  # 'default_unit': 'microgram'
        'iodine': 150,  # 'default_unit': 'microgram'
        'iron': 11,  # 'default_unit': 'milligram'
        'magnesium': 350,  # 'default_unit': 'milligram'
        'manganese': 3,  # 'default_unit': 'milligram'
        'molybdenum': 65,  # 'default_unit': 'microgram'
        'phosphorus': 550,  # 'default_unit': 'milligram'
        'selenium': 70,  # 'default_unit': 'microgram'
        # Zinc PRI depends on phytate intake! Went with maximum.
        'zinc': 16.3,  # 'default_unit': 'milligram'
        'potassium': 3.500,  # 'default_unit': 'gram'
        'sodium': 2,  # 'default_unit': 'gram'
        'chloride': 3.1,  # 'default_unit': 'gram'

        # Maximum amounts (i.e. tolerable upper intake)
        'max_calories': None,  # 'default_unit': 'kcal'
        'max_carbohydrates': None,  # 'default_unit': 'gram'
        'max_fat': None,  # 'default_unit': 'gram'
        'max_protein': None,  # 'default_unit': 'gram'
        'max_linoleic_acid': None,  # 'default_unit': 'gram'
        'max_alpha_linoleic_acid': None,  # 'default_unit': 'gram'
        # Vitamin A unit conversion:
        # Vitamin A: 1 IU is the biological equivalent of 0.3 mcg retinol,
        # or of 0.6 mcg beta-carotene
        # Source: https://dietarysupplementdatabase.usda.nih.gov/
        # ingredient_calculator/help.php
        # => * 0.3
        'max_vitamin_a': 3000,  # 'default_unit': 'microgram'.
        'max_vitamin_c': None,  # ND  # 'default_unit': 'milligram'
        'max_vitamin_d': 100,  # 'default_unit': 'microgram'
        'max_vitamin_e': 300,  # 'default_unit': 'milligram'
        'max_vitamin_k': None,  # ND  # 'default_unit': 'microgram'
        'max_thiamin': None,  # ND  # 'default_unit': 'milligram'
        'max_riboflavin': None,  # ND  # 'default_unit': 'milligram'
        # The max for Niacin is for Nicotinamide. There is a different TUI for
        # nicotinic acid.
        'max_niacin': 900,  # 'default_unit': 'milligram'
        'max_vitamin_b6': 25,  # 'default_unit': 'milligram'
        'max_folate': 1000,  # 'default_unit': 'microgram'
        'max_vitamin_b12': None,  # ND # 'default_unit': 'microgram'
        'max_pantothenic_acid': None,  # ND  # 'default_unit': 'milligram'
        'max_biotin': None,  # ND  # 'default_unit': 'microgram'
        'max_choline': None,  # ND  # 'default_unit': 'milligram'
        'max_calcium': 2500,  # 'default_unit': 'milligram'
        'max_chromium': None,  # 'default_unit': 'microgram'
        'max_copper': 5000,  # 'default_unit': 'microgram'
        'max_iodine': 600,  # 'default_unit': 'microgram'
        'max_iron': None,  # ND  # 'default_unit': 'milligram'
        'max_magnesium': 250,  # specifically from
        # supplements, that is why it is higher than the amount in the
        # nutrient profile.  # 'default_unit': 'milligram'
        'max_manganese': None,  # ND  # 'default_unit': 'milligram'
        'max_molybdenum': 600,  # 'default_unit': 'microgram'
        'max_phosphorus': None,  # ND  # 'default_unit': 'milligram'
        'max_selenium': 300,  # 'default_unit': 'microgram'
        'max_zinc': 25,  # 'default_unit': 'milligram'
        'max_potassium': None,  # ND  # 'default_unit': 'gram'
        'max_sodium': None,  # 'default_unit': 'gram'
        'max_chloride': None,  # 'default_unit': 'gram'

    },

]
