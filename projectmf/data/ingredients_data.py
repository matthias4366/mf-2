"""
It is desired to test the measured food application. A full recipe creation is
to be performed. For this, ingredients are to be added. The data for the
ingredients is stored centrally in this python file.
"""

# This is the template for an ingredient dictionary.
ingredient_dict_template = {
    'name': None,
    'price': None,
    'reference_amount': None,
    'amount_in_package': None,
    'where_to_buy': None,
    'source_nutritional_information': None,
    'calories_kcal' : None,
    'total_carbohydrates_g' : None,
    'dietary_fiber_g' : None,
    'starch_g' : None,
    'sugars_g' : None,
    'total_fat_g' : None,
    'saturated_fat_g' : None,
    'monounsaturated_fat_g' : None,
    'polyunsaturated_fat_g' : None,
    'total_trans_fatty_acids_g' : None,
    'total_omega_3_fatty_acids_mg' : None,
    'total_omega_6_fatty_acids_mg' : None,
    'protein_g' : None,
    # Vitamins
    'vitamin_a_iu' : None,
    'vitamin_c_mg' : None,
    'vitamin_d_iu' : None,
    'vitamin_e_alpha_tocopherol_mg' : None,
    'vitamin_k_mcg' : None,
    'thiamin_mg' : None,
    'riboflavin_mg' : None,
    'niacin_mg' : None,
    'vitamin_b6_mg' : None,
    'folate_mcg' : None,
    'vitamin_b12_mcg' : None,
    'pantothenic_acid_mg' : None,
    'choline_mg' : None,
    'betaine_mg' : None,
    # Minerals
    'calcium_mg' : None,
    'iron_mg' : None,
    'magnesium_mg' : None,
    'phosphorus_mg' : None,
    'potassium_mg' : None,
    'sodium_mg' : None,
    'zinc_mg' : None,
    'copper_mg' : None,
    'manganese_mg' : None,
    'selenium_mcg' : None,
    'fluoride_mcg' : None,
    # Sterols
    'cholesterol_mg' : None,
    'phytosterols' : None,
    # Other
    'alcohol_g' : None,
    'water_g' : None,
    'ash_g' : None,
    'caffeine_mg' : None,
    'theobromine_mg' : None
}

kidney_beans_raw_dict = {
    'name': 'Kidney Beans, raw',
    'price': 0.35,
    'reference_amount': 100,
    'amount_in_package': 500,
    'where_to_buy': 'https://www.get-grocery.com/en/dal-lentils-beans/112-trs-red-kidney-beans-rajma-1-5017689005092.html',
    'source_nutritional_information': \
        'https://nutritiondata.self.com/facts/legumes-and-legume-products/4301/2',
    'calories_kcal' : 337,
    'total_carbohydrates_g' : 61.3,
    'dietary_fiber_g' : 15.2,
    'starch_g' : 0,
    'sugars_g' : 2.1,
    'total_fat_g' : 1.1,
    'saturated_fat_g' : 0.2,
    'monounsaturated_fat_g' : 0.1,
    'polyunsaturated_fat_g' : 0.6,
    'total_trans_fatty_acids_g' : 0,
    'total_omega_3_fatty_acids_mg' : 358,
    'total_omega_6_fatty_acids_mg' : 228,
    'protein_g' : 22.5,
    # Vitamins
    'vitamin_a_iu' : 0,
    'vitamin_c_mg' : 4.5,
    'vitamin_d_iu' : 0,
    'vitamin_e_alpha_tocopherol_mg' : 0.2,
    'vitamin_k_mcg' : 5.6,
    'thiamin_mg' : 0.6,
    'riboflavin_mg' : 0.2,
    'niacin_mg' : 2.1,
    'vitamin_b6_mg' : 0.4,
    'folate_mcg' : 394,
    'vitamin_b12_mcg' : 0,
    'pantothenic_acid_mg' : 0.8,
    'choline_mg' : 65.9,
    'betaine_mg' : None,
    # Minerals
    'calcium_mg' : 83.0,
    'iron_mg' : 6.7,
    'magnesium_mg' : 138,
    'phosphorus_mg' : 406,
    'potassium_mg' : 1359,
    'sodium_mg' : 12.0,
    'zinc_mg' : 2.8,
    'copper_mg' : 0.7,
    'manganese_mg' : 1.1,
    'selenium_mcg' : 3.2,
    'fluoride_mcg' : 2.2,
    # Sterols
    'cholesterol_mg' : 0,
    'phytosterols' : None,
    # Other
    'alcohol_g' : 0,
    'water_g' : 11.7,
    'ash_g' : 3.4,
    'caffeine_mg' : 0,
    'theobromine_mg' : 0
}

canola_oil_dict = {
    'name': 'Oil, vegetable, canola [low erucic acid rapeseed oil]',
    'price': 0.52,
    'reference_amount': 100,
    'amount_in_package': 750,
    'where_to_buy': 'https://www.getnow.com/Themenwelten/Sommer-Sonne-Salate/Rapso-100-reines-Rapsoel-750ml.html?userInput=raps&ignoreForCache[]=userInput&queryFromSuggest=true&ignoreForCache[]=queryFromSuggest',
    'source_nutritional_information': 'https://nutritiondata.self.com/facts/fats-and-oils/621/2',
    'calories_kcal' : 884,
    'total_carbohydrates_g' : 0,
    'dietary_fiber_g' : 0,
    'starch_g' : 0,
    'sugars_g' : 0,
    'total_fat_g' : 100,
    'saturated_fat_g' : 7.4,
    'monounsaturated_fat_g' : 63.3,
    'polyunsaturated_fat_g' : 28.1,
    'total_trans_fatty_acids_g' : 0.4,
    'total_omega_3_fatty_acids_mg' : 9138,
    'total_omega_6_fatty_acids_mg' : 18645,
    'protein_g' : 0.0,
    # Vitamins
    'vitamin_a_iu' : 0.0,
    'vitamin_c_mg' : 0.0,
    'vitamin_d_iu' : None,
    'vitamin_e_alpha_tocopherol_mg' : 17.5,
    'vitamin_k_mcg' : 71.3,
    'thiamin_mg' : 0.0,
    'riboflavin_mg' : 0.0,
    'niacin_mg' : 0.0,
    'vitamin_b6_mg' : 0.0,
    'folate_mcg' : 0.0,
    'vitamin_b12_mcg' : 0.0,
    'pantothenic_acid_mg' : 0.0,
    'choline_mg' : 0.2,
    'betaine_mg' : 0.0,
    # Minerals
    'calcium_mg' : 0,
    'iron_mg' : 0,
    'magnesium_mg' : 0,
    'phosphorus_mg' : 0,
    'potassium_mg' : 0,
    'sodium_mg' : 0,
    'zinc_mg' : 0,
    'copper_mg' : 0,
    'manganese_mg' : 0,
    'selenium_mcg' : 0,
    'fluoride_mcg' : None,
    # Sterols
    'cholesterol_mg' : 0,
    'phytosterols' : None,
    # Other
    'alcohol_g' : 0,
    'water_g' : 0,
    'ash_g' : 0,
    'caffeine_mg' : 0,
    'theobromine_mg' : 0
}

white_rice_dict = {
    'name': 'Rice, white, long-grain, regular, raw, unenriched',
    'price': 0.13,
    'reference_amount': 100,
    'amount_in_package': 10000,
    'where_to_buy': 'https://www.get-grocery.com/en/rice-noodles/323-tilda-broken-basmati-rice-5011157330402.html',
    'source_nutritional_information': 'https://nutritiondata.self.com/facts/cereal-grains-and-pasta/5812/2',
    'calories_kcal' : 365,
    'total_carbohydrates_g' : 79.9,
    'dietary_fiber_g' : 1.3,
    'starch_g' : None,
    'sugars_g' : 0.1,
    'total_fat_g' : 0.7,
    'saturated_fat_g' : 0.2,
    'monounsaturated_fat_g' : 0.2,
    'polyunsaturated_fat_g' : 0.2,
    'total_trans_fatty_acids_g' : None,
    'total_omega_3_fatty_acids_mg' : 31.0,
    'total_omega_6_fatty_acids_mg' : 146,
    'protein_g' : 7.1,
    # Vitamins
    'vitamin_a_iu' : 0.0,
    'vitamin_c_mg' : 0.0,
    'vitamin_d_iu' : None,
    'vitamin_e_alpha_tocopherol_mg' : 0.1,
    'vitamin_k_mcg' : 0.1,
    'thiamin_mg' : 0.1,
    'riboflavin_mg' : 0.0,
    'niacin_mg' : 1.6,
    'vitamin_b6_mg' : 0.2,
    'folate_mcg' : 8.0,
    'vitamin_b12_mcg' : 0.0,
    'pantothenic_acid_mg' : 1.0,
    'choline_mg' : 5.8,
    'betaine_mg' : None,
    # Minerals
    'calcium_mg' : 28.0,
    'iron_mg' : 0.8,
    'magnesium_mg' : 25.0,
    'phosphorus_mg' : 115,
    'potassium_mg' : 115,
    'sodium_mg' : 5.0,
    'zinc_mg' : 1.1,
    'copper_mg' : 0.2,
    'manganese_mg' : 1.1,
    'selenium_mcg' : 15.1,
    'fluoride_mcg' : None,
    # Sterols
    'cholesterol_mg' : 0,
    'phytosterols' : None,
    # Other
    'alcohol_g' : 0,
    'water_g' : 11.6,
    'ash_g' : 0.6,
    'caffeine_mg' : 0,
    'theobromine_mg' : 0
}

oregano_dict = {
    'name': 'Oregano',
    'price': None,
    'reference_amount': None,
    'amount_in_package': None,
    'where_to_buy': None,
    'source_nutritional_information': None,
    'calories_kcal' : None,
    'total_carbohydrates_g' : None,
    'dietary_fiber_g' : None,
    'starch_g' : None,
    'sugars_g' : None,
    'total_fat_g' : None,
    'saturated_fat_g' : None,
    'monounsaturated_fat_g' : None,
    'polyunsaturated_fat_g' : None,
    'total_trans_fatty_acids_g' : None,
    'total_omega_3_fatty_acids_mg' : None,
    'total_omega_6_fatty_acids_mg' : None,
    'protein_g' : None,
    # Vitamins
    'vitamin_a_iu' : None,
    'vitamin_c_mg' : None,
    'vitamin_d_iu' : None,
    'vitamin_e_alpha_tocopherol_mg' : None,
    'vitamin_k_mcg' : None,
    'thiamin_mg' : None,
    'riboflavin_mg' : None,
    'niacin_mg' : None,
    'vitamin_b6_mg' : None,
    'folate_mcg' : None,
    'vitamin_b12_mcg' : None,
    'pantothenic_acid_mg' : None,
    'choline_mg' : None,
    'betaine_mg' : None,
    # Minerals
    'calcium_mg' : None,
    'iron_mg' : None,
    'magnesium_mg' : None,
    'phosphorus_mg' : None,
    'potassium_mg' : None,
    'sodium_mg' : None,
    'zinc_mg' : None,
    'copper_mg' : None,
    'manganese_mg' : None,
    'selenium_mcg' : None,
    'fluoride_mcg' : None,
    # Sterols
    'cholesterol_mg' : None,
    'phytosterols' : None,
    # Other
    'alcohol_g' : None,
    'water_g' : None,
    'ash_g' : None,
    'caffeine_mg' : None,
    'theobromine_mg' : None
}

chili_powder_dict = {
    'name': 'Chili powder',
    'price': None,
    'reference_amount': None,
    'amount_in_package': None,
    'where_to_buy': None,
    'source_nutritional_information': None,
    'calories_kcal' : None,
    'total_carbohydrates_g' : None,
    'dietary_fiber_g' : None,
    'starch_g' : None,
    'sugars_g' : None,
    'total_fat_g' : None,
    'saturated_fat_g' : None,
    'monounsaturated_fat_g' : None,
    'polyunsaturated_fat_g' : None,
    'total_trans_fatty_acids_g' : None,
    'total_omega_3_fatty_acids_mg' : None,
    'total_omega_6_fatty_acids_mg' : None,
    'protein_g' : None,
    # Vitamins
    'vitamin_a_iu' : None,
    'vitamin_c_mg' : None,
    'vitamin_d_iu' : None,
    'vitamin_e_alpha_tocopherol_mg' : None,
    'vitamin_k_mcg' : None,
    'thiamin_mg' : None,
    'riboflavin_mg' : None,
    'niacin_mg' : None,
    'vitamin_b6_mg' : None,
    'folate_mcg' : None,
    'vitamin_b12_mcg' : None,
    'pantothenic_acid_mg' : None,
    'choline_mg' : None,
    'betaine_mg' : None,
    # Minerals
    'calcium_mg' : None,
    'iron_mg' : None,
    'magnesium_mg' : None,
    'phosphorus_mg' : None,
    'potassium_mg' : None,
    'sodium_mg' : None,
    'zinc_mg' : None,
    'copper_mg' : None,
    'manganese_mg' : None,
    'selenium_mcg' : None,
    'fluoride_mcg' : None,
    # Sterols
    'cholesterol_mg' : None,
    'phytosterols' : None,
    # Other
    'alcohol_g' : None,
    'water_g' : None,
    'ash_g' : None,
    'caffeine_mg' : None,
    'theobromine_mg' : None
}

tomato_puree_dict = {
    'name': 'Tomato puree, MUTTI',
    'price': 0.30,
    'reference_amount': 100,
    'amount_in_package': 750,
    'where_to_buy': 'https://www.getnow.com/Speisekammer/Konserven/Gemuese-Sauerkonserven/Mutti-Passierte-italienische-Tomaten-700g.html?userInput=mutti%20tom&ignoreForCache[]=userInput&queryFromSuggest=true&ignoreForCache[]=queryFromSuggest',
    'source_nutritional_information': 'Tomato products, canned, puree, with salt added',
    'calories_kcal' : 38.0,
    'total_carbohydrates_g' : 9.0,
    'dietary_fiber_g' : 1.9,
    'starch_g' : None,
    'sugars_g' : 4.8,
    'total_fat_g' : 0.2,
    'saturated_fat_g' : 0.0,
    'monounsaturated_fat_g' : 0.0,
    'polyunsaturated_fat_g' : 0.1,
    'total_trans_fatty_acids_g' : None,
    'total_omega_3_fatty_acids_mg' : 4.0,
    'total_omega_6_fatty_acids_mg' : 82.0,
    'protein_g' : 1.7,
    # Vitamins
    'vitamin_a_iu' : 510,
    'vitamin_c_mg' : 10.6,
    'vitamin_d_iu' : None,
    'vitamin_e_alpha_tocopherol_mg' : 2.0,
    'vitamin_k_mcg' : 3.4,
    'thiamin_mg' : 0.0,
    'riboflavin_mg' : 0.1,
    'niacin_mg' : 1.5,
    'vitamin_b6_mg' : 0.1,
    'folate_mcg' : 11.0,
    'vitamin_b12_mcg' : 0.0,
    'pantothenic_acid_mg' : 0.4,
    'choline_mg' : 17.6,
    'betaine_mg' : 0.2,
    # Minerals
    'calcium_mg' : 18.0,
    'iron_mg' : 1.8,
    'magnesium_mg' : 23.0,
    'phosphorus_mg' : 40.0,
    'potassium_mg' : 439,
    'sodium_mg' : 399,
    'zinc_mg' : 0.4,
    'copper_mg' : 0.3,
    'manganese_mg' : 0.2,
    'selenium_mcg' : 0.7,
    'fluoride_mcg' : None,
    # Sterols
    'cholesterol_mg' : 0,
    'phytosterols' : None,
    # Other
    'alcohol_g' : 0,
    'water_g' : 87.9,
    'ash_g' : 1.3,
    'caffeine_mg' : 0,
    'theobromine_mg' : 0
}

beer_alcohol_free_dict = {
    'name': 'Beer, alcohol free',
    'price': 0.21,
    'reference_amount': 100,
    'amount_in_package': 1980,
    'where_to_buy': 'https://www.getnow.com/index.php?cl=details&cnid=269&actcontrol=details&anid=430628601819020001&redirected=1',
    'source_nutritional_information': 'https://www.getnow.com/index.php?cl=details&cnid=269&actcontrol=details&anid=430628601819020001&redirected=1',
    'calories_kcal' : 22.4,
    'total_carbohydrates_g' : 4.8,
    'dietary_fiber_g' : None,
    'starch_g' : None,
    'sugars_g' : 2.1,
    'total_fat_g' : None,
    'saturated_fat_g' : None,
    'monounsaturated_fat_g' : None,
    'polyunsaturated_fat_g' : None,
    'total_trans_fatty_acids_g' : None,
    'total_omega_3_fatty_acids_mg' : None,
    'total_omega_6_fatty_acids_mg' : None,
    'protein_g' : 0.3,
    # Vitamins
    'vitamin_a_iu' : None,
    'vitamin_c_mg' : None,
    'vitamin_d_iu' : None,
    'vitamin_e_alpha_tocopherol_mg' : None,
    'vitamin_k_mcg' : None,
    'thiamin_mg' : None,
    'riboflavin_mg' : None,
    'niacin_mg' : None,
    'vitamin_b6_mg' : None,
    'folate_mcg' : None,
    'vitamin_b12_mcg' : None,
    'pantothenic_acid_mg' : None,
    'choline_mg' : None,
    'betaine_mg' : None,
    # Minerals
    'calcium_mg' : None,
    'iron_mg' : None,
    'magnesium_mg' : None,
    'phosphorus_mg' : None,
    'potassium_mg' : None,
    'sodium_mg' : None,
    'zinc_mg' : None,
    'copper_mg' : None,
    'manganese_mg' : None,
    'selenium_mcg' : None,
    'fluoride_mcg' : None,
    # Sterols
    'cholesterol_mg' : None,
    'phytosterols' : None,
    # Other
    'alcohol_g' : None,
    'water_g' : None,
    'ash_g' : None,
    'caffeine_mg' : None,
    'theobromine_mg' : None
}


mushrooms_dict = {
    'name': 'Mushrooms',
    'price': 0.33,
    'reference_amount': 100,
    'amount_in_package': 450,
    'where_to_buy': 'EDEKA',
    # Mushrooms, white, raw
    'source_nutritional_information': 'https://nutritiondata.self.com/facts/vegetables-and-vegetable-products/2482/2',
    'calories_kcal' : 22,
    'total_carbohydrates_g' : 3.3,
    'dietary_fiber_g' : 1,
    'starch_g' : None,
    'sugars_g' : 1.7,
    'total_fat_g' : 0.3,
    'saturated_fat_g' : None,
    'monounsaturated_fat_g' : None,
    'polyunsaturated_fat_g' : None,
    'total_trans_fatty_acids_g' : None,
    'total_omega_3_fatty_acids_mg' : None,
    'total_omega_6_fatty_acids_mg' : 139,
    'protein_g' : 3.1,
    # Vitamins
    'vitamin_a_iu' : 0,
    'vitamin_c_mg' : 2.1,
    'vitamin_d_iu' : 18.0,
    'vitamin_e_alpha_tocopherol_mg' : 0.0,
    'vitamin_k_mcg' : 0.0,
    'thiamin_mg' : 0.1,
    'riboflavin_mg' : 0.4,
    'niacin_mg' : 3.6,
    'vitamin_b6_mg' : 0.1,
    'folate_mcg' : 16.0,
    'vitamin_b12_mcg' : 0.0,
    'pantothenic_acid_mg' : 1.5,
    'choline_mg' : 17.3,
    'betaine_mg' : 9.4,
    # Minerals
    'calcium_mg' : 3.0,
    'iron_mg' : 0.5,
    'magnesium_mg' : 9.0,
    'phosphorus_mg' : 86.0,
    'potassium_mg' : 318,
    'sodium_mg' : 5.0,
    'zinc_mg' : 0.5,
    'copper_mg' : 0.3,
    'manganese_mg' : 0.0,
    'selenium_mcg' : 9.3,
    'fluoride_mcg' : None,
    # Sterols
    'cholesterol_mg' : 0.0,
    'phytosterols' : None,
    # Other
    'alcohol_g' : None,
    'water_g' : 92.4,
    'ash_g' : 0.9,
    'caffeine_mg' : None,
    'theobromine_mg' : None
}

walnuts_dict = {
    'name': 'Walnuts',
    'price': 1.499,
    'reference_amount': 100,
    'amount_in_package': 1000,
    'where_to_buy': 'https://www.amazon.de/gp/product/B0799MYYNC/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1',
    'source_nutritional_information': 'https://nutritiondata.self.com/facts/nut-and-seed-products/3138/2',
    'calories_kcal' : 654,
    'total_carbohydrates_g' : 13.7,
    'dietary_fiber_g' : 6.7,
    'starch_g' : 0.1,
    'sugars_g' : 2.6,
    'total_fat_g' : 65.2,
    'saturated_fat_g' : 6.1,
    'monounsaturated_fat_g' : 8.9,
    'polyunsaturated_fat_g' : 47.2,
    'total_trans_fatty_acids_g' : None,
    'total_omega_3_fatty_acids_mg' : 9079,
    'total_omega_6_fatty_acids_mg' : 38092,
    'protein_g' : 15.2,
    # Vitamins
    'vitamin_a_iu' : 20.0,
    'vitamin_c_mg' : 1.3,
    'vitamin_d_iu' : None,
    'vitamin_e_alpha_tocopherol_mg' : 0.7,
    'vitamin_k_mcg' : 2.7,
    'thiamin_mg' : 0.3,
    'riboflavin_mg' : 0.2,
    'niacin_mg' : 1.1,
    'vitamin_b6_mg' : 0.5,
    'folate_mcg' : 98.0,
    'vitamin_b12_mcg' : 0.0,
    'pantothenic_acid_mg' : 0.6,
    'choline_mg' : 39.2,
    'betaine_mg' : 0.3,
    # Minerals
    'calcium_mg' : 98.0,
    'iron_mg' : 2.9,
    'magnesium_mg' : 158,
    'phosphorus_mg' : 346,
    'potassium_mg' : 441,
    'sodium_mg' : 2.0,
    'zinc_mg' : 3.1,
    'copper_mg' : 1.6,
    'manganese_mg' : 3.4,
    'selenium_mcg' : 4.9,
    'fluoride_mcg' : None,
    # Sterols
    'cholesterol_mg' : 0.0,
    'phytosterols' : 72.0,
    # Other
    'alcohol_g' : None,
    'water_g' : 4.1,
    'ash_g' : 1.8,
    'caffeine_mg' : None,
    'theobromine_mg' : None
}

whole_grain_pasta_dict = {
    'name': 'Whole wheat pasta',
    'price': 0.38,
    'reference_amount': 100,
    'amount_in_package': 500,
    'where_to_buy': 'https://www.getnow.com/index.php?cl=details&cnid=193&actcontrol=details&anid=430628603914340001&redirected=1',
    # macros from package, micros from nutrition data
    'source_nutritional_information': 'https://nutritiondata.self.com/facts/cereal-grains-and-pasta/5783/2',
    'calories_kcal' : 348,
    'total_carbohydrates_g' : 64,
    'dietary_fiber_g' : None,
    'starch_g' : None,
    'sugars_g' : None,
    'total_fat_g' : 2.5,
    'saturated_fat_g' : None,
    'monounsaturated_fat_g' : None,
    'polyunsaturated_fat_g' : None,
    'total_trans_fatty_acids_g' : None,
    'total_omega_3_fatty_acids_mg' : 27.0,
    'total_omega_6_fatty_acids_mg' : 529,
    'protein_g' : 13,
    # Vitamins
    'vitamin_a_iu' : 0.0,
    'vitamin_c_mg' : 0.0,
    'vitamin_d_iu' : None,
    'vitamin_e_alpha_tocopherol_mg' : None,
    'vitamin_k_mcg' : None,
    'thiamin_mg' : 0.5,
    'riboflavin_mg' : 0.1,
    'niacin_mg' : 5.1,
    'vitamin_b6_mg' : 0.2,
    'folate_mcg' : 57.0,
    'vitamin_b12_mcg' : 0.0,
    'pantothenic_acid_mg' : 1.0,
    'choline_mg' : None,
    'betaine_mg' : None,
    # Minerals
    'calcium_mg' : 40.0,
    'iron_mg' : 3.6,
    'magnesium_mg' : 143,
    'phosphorus_mg' : 258,
    'potassium_mg' : 215,
    'sodium_mg' : 8.0,
    'zinc_mg' : 2.4,
    'copper_mg' : 0.5,
    'manganese_mg' : 3.1,
    'selenium_mcg' : 73.0,
    'fluoride_mcg' : None,
    # Sterols
    'cholesterol_mg' : 0.0,
    'phytosterols' : None,
    # Other
    'alcohol_g' : None,
    'water_g' : 7.3,
    'ash_g' : 1.6,
    'caffeine_mg' : None,
    'theobromine_mg' : None
}

pea_protein_powder_dict = {
    'name': 'Pea protein powder',
    'price': 1.04,
    'reference_amount': 100,
    'amount_in_package': 2500,
    'where_to_buy': 'https://de.myprotein.com/sporternahrung/erbsenprotein-isolat/10530136.html',
    'source_nutritional_information': 'https://de.myprotein.com/sporternahrung/erbsenprotein-isolat/10530136.html',
    'calories_kcal' : 357,
    'total_carbohydrates_g' : 3.0,
    'dietary_fiber_g' : None,
    'starch_g' : None,
    'sugars_g' : None,
    'total_fat_g' : 5.0,
    'saturated_fat_g' : 1.9,
    'monounsaturated_fat_g' : None,
    'polyunsaturated_fat_g' : None,
    'total_trans_fatty_acids_g' : None,
    'total_omega_3_fatty_acids_mg' : None,
    'total_omega_6_fatty_acids_mg' : None,
    'protein_g' : 75,
    # Vitamins
    'vitamin_a_iu' : None,
    'vitamin_c_mg' : None,
    'vitamin_d_iu' : None,
    'vitamin_e_alpha_tocopherol_mg' : None,
    'vitamin_k_mcg' : None,
    'thiamin_mg' : None,
    'riboflavin_mg' : None,
    'niacin_mg' : None,
    'vitamin_b6_mg' : None,
    'folate_mcg' : None,
    'vitamin_b12_mcg' : None,
    'pantothenic_acid_mg' : None,
    'choline_mg' : None,
    'betaine_mg' : None,
    # Minerals
    'calcium_mg' : None,
    'iron_mg' : None,
    'magnesium_mg' : None,
    'phosphorus_mg' : None,
    'potassium_mg' : None,
    'sodium_mg' : 1000,
    'zinc_mg' : None,
    'copper_mg' : None,
    'manganese_mg' : None,
    'selenium_mcg' : None,
    'fluoride_mcg' : None,
    # Sterols
    'cholesterol_mg' : None,
    'phytosterols' : None,
    # Other
    'alcohol_g' : None,
    'water_g' : None,
    'ash_g' : None,
    'caffeine_mg' : None,
    'theobromine_mg' : None
}

barilla_napoletana_dict = {
    'name': 'Napoletana sauce barilla',
    'price': 0.40,
    'reference_amount': 100,
    'amount_in_package': 400,
    'where_to_buy': 'https://www.getnow.com/index.php?cl=details&cnid=999&actcontrol=details&anid=430628601335060001&redirected=1',
    'source_nutritional_information': 'https://www.getnow.com/index.php?cl=details&cnid=999&actcontrol=details&anid=430628601335060001&redirected=1',
    'calories_kcal' : 69,
    'total_carbohydrates_g' : 6.3,
    'dietary_fiber_g' : None,
    'starch_g' : None,
    'sugars_g' : 5.4,
    'total_fat_g' : 4,
    'saturated_fat_g' : 0.5,
    'monounsaturated_fat_g' : None,
    'polyunsaturated_fat_g' : None,
    'total_trans_fatty_acids_g' : None,
    'total_omega_3_fatty_acids_mg' : None,
    'total_omega_6_fatty_acids_mg' : None,
    'protein_g' : 1.4,
    # Vitamins
    'vitamin_a_iu' : None,
    'vitamin_c_mg' : None,
    'vitamin_d_iu' : None,
    'vitamin_e_alpha_tocopherol_mg' : None,
    'vitamin_k_mcg' : None,
    'thiamin_mg' : None,
    'riboflavin_mg' : None,
    'niacin_mg' : None,
    'vitamin_b6_mg' : None,
    'folate_mcg' : None,
    'vitamin_b12_mcg' : None,
    'pantothenic_acid_mg' : None,
    'choline_mg' : None,
    'betaine_mg' : None,
    # Minerals
    'calcium_mg' : None,
    'iron_mg' : None,
    'magnesium_mg' : None,
    'phosphorus_mg' : None,
    'potassium_mg' : None,
    'sodium_mg' : 400,
    'zinc_mg' : None,
    'copper_mg' : None,
    'manganese_mg' : None,
    'selenium_mcg' : None,
    'fluoride_mcg' : None,
    # Sterols
    'cholesterol_mg' : None,
    'phytosterols' : None,
    # Other
    'alcohol_g' : None,
    'water_g' : None,
    'ash_g' : None,
    'caffeine_mg' : None,
    'theobromine_mg' : None
}

barilla_arrabiata_dict = {
    'name': 'Arrabiata sauce barilla',
    'price': 0.40,
    'reference_amount': 100,
    'amount_in_package': 400,
    'where_to_buy': 'https://www.getnow.com/index.php?cl=details&cnid=999&actcontrol=details&anid=430628601335060001&redirected=1',
    'source_nutritional_information': 'https://www.getnow.com/index.php?cl=details&cnid=999&actcontrol=details&anid=430628601335060001&redirected=1',
    'calories_kcal' : 69,
    'total_carbohydrates_g' : 6.3,
    'dietary_fiber_g' : None,
    'starch_g' : None,
    'sugars_g' : 5.4,
    'total_fat_g' : 4,
    'saturated_fat_g' : 0.5,
    'monounsaturated_fat_g' : None,
    'polyunsaturated_fat_g' : None,
    'total_trans_fatty_acids_g' : None,
    'total_omega_3_fatty_acids_mg' : None,
    'total_omega_6_fatty_acids_mg' : None,
    'protein_g' : 1.4,
    # Vitamins
    'vitamin_a_iu' : None,
    'vitamin_c_mg' : None,
    'vitamin_d_iu' : None,
    'vitamin_e_alpha_tocopherol_mg' : None,
    'vitamin_k_mcg' : None,
    'thiamin_mg' : None,
    'riboflavin_mg' : None,
    'niacin_mg' : None,
    'vitamin_b6_mg' : None,
    'folate_mcg' : None,
    'vitamin_b12_mcg' : None,
    'pantothenic_acid_mg' : None,
    'choline_mg' : None,
    'betaine_mg' : None,
    # Minerals
    'calcium_mg' : None,
    'iron_mg' : None,
    'magnesium_mg' : None,
    'phosphorus_mg' : None,
    'potassium_mg' : None,
    'sodium_mg' : 400,
    'zinc_mg' : None,
    'copper_mg' : None,
    'manganese_mg' : None,
    'selenium_mcg' : None,
    'fluoride_mcg' : None,
    # Sterols
    'cholesterol_mg' : None,
    'phytosterols' : None,
    # Other
    'alcohol_g' : None,
    'water_g' : None,
    'ash_g' : None,
    'caffeine_mg' : None,
    'theobromine_mg' : None
}

barilla_olive_dict = {
    'name': 'Olive sauce barilla',
    'price': 0.40,
    'reference_amount': 100,
    'amount_in_package': 400,
    'where_to_buy': 'https://www.getnow.com/index.php?cl=details&cnid=999&actcontrol=details&anid=430628601335060001&redirected=1',
    'source_nutritional_information': 'https://www.getnow.com/index.php?cl=details&cnid=999&actcontrol=details&anid=430628601335060001&redirected=1',
    'calories_kcal' : 69,
    'total_carbohydrates_g' : 6.3,
    'dietary_fiber_g' : None,
    'starch_g' : None,
    'sugars_g' : 5.4,
    'total_fat_g' : 4,
    'saturated_fat_g' : 0.5,
    'monounsaturated_fat_g' : None,
    'polyunsaturated_fat_g' : None,
    'total_trans_fatty_acids_g' : None,
    'total_omega_3_fatty_acids_mg' : None,
    'total_omega_6_fatty_acids_mg' : None,
    'protein_g' : 1.4,
    # Vitamins
    'vitamin_a_iu' : None,
    'vitamin_c_mg' : None,
    'vitamin_d_iu' : None,
    'vitamin_e_alpha_tocopherol_mg' : None,
    'vitamin_k_mcg' : None,
    'thiamin_mg' : None,
    'riboflavin_mg' : None,
    'niacin_mg' : None,
    'vitamin_b6_mg' : None,
    'folate_mcg' : None,
    'vitamin_b12_mcg' : None,
    'pantothenic_acid_mg' : None,
    'choline_mg' : None,
    'betaine_mg' : None,
    # Minerals
    'calcium_mg' : None,
    'iron_mg' : None,
    'magnesium_mg' : None,
    'phosphorus_mg' : None,
    'potassium_mg' : None,
    'sodium_mg' : 400,
    'zinc_mg' : None,
    'copper_mg' : None,
    'manganese_mg' : None,
    'selenium_mcg' : None,
    'fluoride_mcg' : None,
    # Sterols
    'cholesterol_mg' : None,
    'phytosterols' : None,
    # Other
    'alcohol_g' : None,
    'water_g' : None,
    'ash_g' : None,
    'caffeine_mg' : None,
    'theobromine_mg' : None
}

spinach_dict = {
    'name': 'Spinach',
    'price': 0.213,
    'reference_amount': 100,
    'amount_in_package': 1000,
    'where_to_buy': 'https://www.getnow.com/Tiefkuehl/Gemuese-Kraeuter-Obst/Gemuese-Pilze/Metro-Chef-Blattspinat-Portionen-1kg.html?ffCheckoutTrackData%5Bcampaign%5D=bee2c58c-29ba-4b4e-a778-51a67f8aba0f&listtype=search&searchparam=spinat',
    'source_nutritional_information': 'https://nutritiondata.self.com/facts/vegetables-and-vegetable-products/2626/2',
    'calories_kcal' : 23.0,
    'total_carbohydrates_g' : 3.6,
    'dietary_fiber_g' : 2.2,
    'starch_g' : None,
    'sugars_g' : 0.4,
    'total_fat_g' : 0.4,
    'saturated_fat_g' : 0.1,
    'monounsaturated_fat_g' : 0.0,
    'polyunsaturated_fat_g' : 0.2,
    'total_trans_fatty_acids_g' : None,
    'total_omega_3_fatty_acids_mg' : 138,
    'total_omega_6_fatty_acids_mg' : 26.0,
    'protein_g' : 2.9,
    # Vitamins
    'vitamin_a_iu' : 9376,
    'vitamin_c_mg' : 28.1,
    'vitamin_d_iu' : None,
    'vitamin_e_alpha_tocopherol_mg' : 2.0,
    'vitamin_k_mcg' : 483,
    'thiamin_mg' : 0.1,
    'riboflavin_mg' : 0.2,
    'niacin_mg' : 0.7,
    'vitamin_b6_mg' : 0.2,
    'folate_mcg' : 194,
    'vitamin_b12_mcg' : 0.0,
    'pantothenic_acid_mg' : 0.1,
    'choline_mg' : 18.0,
    'betaine_mg' : 550,
    # Minerals
    'calcium_mg' : 99.0,
    'iron_mg' : 2.7,
    'magnesium_mg' : 79.0,
    'phosphorus_mg' : 49.0,
    'potassium_mg' : 558,
    'sodium_mg' : 79.0,
    'zinc_mg' : 0.5,
    'copper_mg' : 0.1,
    'manganese_mg' : 0.9,
    'selenium_mcg' : 1.0,
    'fluoride_mcg' : None,
    # Sterols
    'cholesterol_mg' : 0.0,
    'phytosterols' : 9.0,
    # Other
    'alcohol_g' : None,
    'water_g' : 91.4,
    'ash_g' : 1.7,
    'caffeine_mg' : None,
    'theobromine_mg' : None
}

# The nutrition info for an ingredient is saved in a dictionary. All the
# dictionaries are saved in a list.
ingredient_dicts_list = [
    kidney_beans_raw_dict,
    canola_oil_dict,
    white_rice_dict,
    oregano_dict,
    chili_powder_dict,
    tomato_puree_dict,
    beer_alcohol_free_dict,
    mushrooms_dict,
    walnuts_dict,
    whole_grain_pasta_dict,
    pea_protein_powder_dict,
    barilla_napoletana_dict,
    barilla_arrabiata_dict,
    barilla_olive_dict,
    spinach_dict
]
