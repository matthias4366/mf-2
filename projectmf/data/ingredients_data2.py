"""
It is desired to test the measured food application. A full recipe creation is
to be performed. For this, ingredients are to be added. The data for the
ingredients is stored centrally in this python file.
"""
# New template



{
    'name': None,
    'reference_amount': None,  # default: 100 g
    'calories': None,  # 'default_unit': 'kcal'
    'carbohydrates': None,  # 'default_unit': 'gram'
    'fat': None,  # 'default_unit': 'gram'
    'protein': None,  # 'default_unit': 'gram'
    'linoleic_acid': None,  # 'default_unit': 'gram'
    'alpha_linoleic_acid': None,  # 'default_unit': 'gram'
    'vitamin_a': None,  #'default_unit': 'microgram'
    'vitamin_c': None,  # 'default_unit': 'milligram'
    'vitamin_d': None,  #'default_unit': 'microgram'
    'vitamin_e': None,  # 'default_unit': 'milligram'
    'vitamin_k': None,  # 'default_unit': 'microgram'
    'thiamin': None,  # 'default_unit': 'milligram'
    'riboflavin': None,  # 'default_unit': 'milligram'
    'niacin': None,  # 'default_unit': 'milligram'
    'vitamin_b6': None,  # 'default_unit': 'milligram'
    'folate': None,  # 'default_unit': 'microgram'
    'vitamin_b12': None,  # 'default_unit': 'microgram'
    'pantothenic_acid': None,  #'default_unit': 'milligram'
    'biotin': None,  # 'default_unit': 'microgram'
    'choline': None,  # 'default_unit': 'milligram'
    'calcium': None,  # 'default_unit': 'milligram'
    'chromium': None,  # 'default_unit': 'microgram'
    'copper': None,  # 'default_unit': 'microgram'
    'fluoride': None,  # 'default_unit': 'milligram'
    'iodine': None,  # 'default_unit': 'microgram'
    'iron': None,  # 'default_unit': 'milligram'
    'magnesium': None,  # 'default_unit': 'milligram'
    'manganese': None,  # 'default_unit': 'milligram'
    'molybdenum': None,  # 'default_unit': 'microgram'
    'phosphorus': None,  # 'default_unit': 'milligram'
    'selenium': None,  # 'default_unit': 'microgram'
    'zinc': None,  # 'default_unit': 'milligram'
    'potassium': None,  # 'default_unit': 'gram'
    'sodium': None,  # 'default_unit': 'gram'
    'chloride': None,  # 'default_unit': 'gram'
    'buy_here_link': None,
    'source_nutritional_information_link': None,
},


# The nutrition info for an ingredient is saved in a dictionary. All the
# dictionaries are saved in a list.
ingredient_dict_list = [
    {
        'name': 'Kidney Beans, raw',
        'price_per_reference_amount': 0.35,
        'reference_amount': 100,
        'amount_in_package': 500,
        'buy_here_link': 'https://www.get-grocery.com/en/dal-lentils-beans/112-trs-red-kidney-beans-rajma-1-5017689005092.html',
        'source_nutritional_information_link': \
            'https://nutritiondata.self.com/facts/legumes-and-legume-products/4301/2',
        'calories' : 337,
        'carbohydrates' : 61.3,
        'fat' : 1.1,
        'alpha_linoleic_acid' : 0.358,
        'linoleic_acid' : 0.228,
        'protein' : 22.5,
        # Vitamins
        'vitamin_a' : 0,
        'vitamin_c' : 4.5,
        'vitamin_d' : 0,
        'vitamin_e' : 0.2,
        'vitamin_k' : 5.6,
        'thiamin' : 0.6,
        'riboflavin' : 0.2,
        'niacin' : 2.1,
        'vitamin_b6' : 0.4,
        'folate' : 394,
        'vitamin_b12' : 0,
        'pantothenic_acid' : 0.8,
        # Minerals
        'calcium' : 83.0,
        'iron' : 6.7,
        'magnesium' : 138,
        'phosphorus' : 0.747,
        'potassium' : 1.359,
        'sodium' : 0.012,
        'zinc' : 2.8,
        'copper' : 0.7,
        'manganese' : 1.1,
        'selenium' : 3.2,
    },
    {
        'name': 'Canola oil',
        'price_per_reference_amount': 0.52,
        'reference_amount': 100,
        'amount_in_package': 750,
        'buy_here_link': 'https://www.getnow.com/Themenwelten/Sommer-Sonne-Salate/Rapso-100-reines-Rapsoel-750ml.html?userInput=raps&ignoreForCache[]=userInput&queryFromSuggest=true&ignoreForCache[]=queryFromSuggest',
        'source_nutritional_information_link': 'https://nutritiondata.self.com/facts/fats-and-oils/621/2',
        'calories' : 884,
        'carbohydrates' : 0,
        'fat' : 100,
        'alpha_linoleic_acid' : 9.138,
        'linoleic_acid' : 18.645,
        'protein' : 0.0,
        # Vitamins
        'vitamin_a' : 0.0,
        'vitamin_c' : 0.0,
        'vitamin_d' : None,
        'vitamin_e' : 17.5,
        'vitamin_k' : 71.3,
        'thiamin' : 0.0,
        'riboflavin' : 0.0,
        'niacin' : 0.0,
        'vitamin_b6' : 0.0,
        'folate' : 0.0,
        'vitamin_b12' : 0.0,
        'pantothenic_acid' : 0.0,
        # Minerals
        'calcium' : 0,
        'iron' : 0,
        'magnesium' : 0,
        'phosphorus' : 0,
        'potassium' : 0,
        'sodium' : 0,
        'zinc' : 0,
        'copper' : 0,
        'manganese' : 0,
        'selenium' : 0,
    },
    {
        'name': 'Rice, white, long-grain, regular, raw, unenriched',
        'price_per_reference_amount': 0.13,
        'reference_amount': 100,
        'amount_in_package': 10000,
        'buy_here_link': 'https://www.get-grocery.com/en/rice-noodles/323-tilda-broken-basmati-rice-5011157330402.html',
        'source_nutritional_information_link': 'https://nutritiondata.self.com/facts/cereal-grains-and-pasta/5812/2',
        'calories' : 365,
        'carbohydrates' : 79.9,
        'fat' : 0.7,
        'alpha_linoleic_acid' : 0.031,
        'linoleic_acid' : 0.146,
        'protein' : 7.1,
        # Vitamins
        'vitamin_a' : 0.0,
        'vitamin_c' : 0.0,
        'vitamin_d' : None,
        'vitamin_e' : 0.1,
        'vitamin_k' : 0.1,
        'thiamin' : 0.1,
        'riboflavin' : 0.0,
        'niacin' : 1.6,
        'vitamin_b6' : 0.2,
        'folate' : 8.0,
        'vitamin_b12' : 0.0,
        'pantothenic_acid' : 1.0,
        # Minerals
        'calcium' : 28.0,
        'iron' : 0.8,
        'magnesium' : 25.0,
        'phosphorus' : 0.115,
        'potassium' : 0.115,
        'sodium' : 0.005,
        'zinc' : 1.1,
        'copper' : 0.2,
        'manganese' : 1.1,
        'selenium' : 15.1,
    },
    {
        'name': 'Oregano',
        'price_per_reference_amount': 0,
        'reference_amount': 100,
        'amount_in_package': 0,
        'buy_here_link': None,
        'source_nutritional_information_link': None,
        'calories' : 0,
        'carbohydrates' : 0,
        'fat' : 0,
        'alpha_linoleic_acid' : 0,
        'linoleic_acid' : 0,
        'protein' : 0,
        # Vitamins
        'vitamin_a' : 0,
        'vitamin_c' : 0,
        'vitamin_d' : 0,
        'vitamin_e' : 0,
        'vitamin_k' : 0,
        'thiamin' : 0,
        'riboflavin' : 0,
        'niacin' : 0,
        'vitamin_b6' : 0,
        'folate' : 0,
        'vitamin_b12' : 0,
        'pantothenic_acid' : 0,
        # Minerals
        'calcium' : 0,
        'iron' : 0,
        'magnesium' : 0,
        'phosphorus' : 0,
        'potassium' : 0,
        'sodium' : 0,
        'zinc' : 0,
        'copper' : 0,
        'manganese' : 0,
        'selenium' : 0,
    },
    {
        'name': 'Chili powder',
        'price_per_reference_amount': 0,
        'reference_amount': 100,
        'amount_in_package': 0,
        'buy_here_link': None,
        'source_nutritional_information_link': None,
        'calories' : 0,
        'carbohydrates' : 0,
        'fat' : 0,
        'alpha_linoleic_acid' : 0,
        'linoleic_acid' : 0,
        'protein' : 0,
        # Vitamins
        'vitamin_a' : 0,
        'vitamin_c' : 0,
        'vitamin_d' : 0,
        'vitamin_e' : 0,
        'vitamin_k' : 0,
        'thiamin' : 0,
        'riboflavin' : 0,
        'niacin' : 0,
        'vitamin_b6' : 0,
        'folate' : 0,
        'vitamin_b12' : 0,
        'pantothenic_acid' : 0,
        # Minerals
        'calcium' : 0,
        'iron' : 0,
        'magnesium' : 0,
        'phosphorus' : 0,
        'potassium' : 0,
        'sodium' : 0,
        'zinc' : 0,
        'copper' : 0,
        'manganese' : 0,
        'selenium' : 0,
    },
    {
        'name': 'Tomato puree, MUTTI',
        'price_per_reference_amount': 0.30,
        'reference_amount': 100,
        'amount_in_package': 750,
        'buy_here_link': 'https://www.getnow.com/Speisekammer/Konserven/Gemuese-Sauerkonserven/Mutti-Passierte-italienische-Tomaten-700g.html?userInput=mutti%20tom&ignoreForCache[]=userInput&queryFromSuggest=true&ignoreForCache[]=queryFromSuggest',
        'source_nutritional_information_link': None,
        'calories' : 38.0,
        'carbohydrates' : 9.0,
        'fat' : 0.2,
        'alpha_linoleic_acid' : 0.004,
        'linoleic_acid' : 0.082,
        'protein' : 1.7,
        # Vitamins
        # vitamin a taken from https://nutritiondata.self.com/facts/vegetables-and-vegetable-products/2960/2
        # and converted based on *0.3 from https://dietarysupplementdatabase.usda.nih.gov/Conversions.php
        'vitamin_a' : 153,
        'vitamin_c' : 10.6,
        'vitamin_d' : None,
        'vitamin_e' : 2.0,
        'vitamin_k' : 3.4,
        'thiamin' : 0.0,
        'riboflavin' : 0.1,
        'niacin' : 1.5,
        'vitamin_b6' : 0.1,
        'folate' : 11.0,
        'vitamin_b12' : 0.0,
        'pantothenic_acid' : 0.4,
        # Minerals
        'calcium' : 18.0,
        'iron' : 1.8,
        'magnesium' : 23.0,
        'phosphorus' : 0.040,
        'potassium' : 0.439,
        'sodium' : 0.399,
        'zinc' : 0.4,
        'copper' : 0.3,
        'manganese' : 0.2,
        'selenium' : 0.7,
    },
    {
        'name': 'Beer, alcohol free',
        'price_per_reference_amount': 0.21,
        'reference_amount': 100,
        'amount_in_package': 1980,
        'buy_here_link': 'https://www.getnow.com/index.php?cl=details&cnid=269&actcontrol=details&anid=430628601819020001&redirected=1',
        'source_nutritional_information_link': 'https://www.getnow.com/index.php?cl=details&cnid=269&actcontrol=details&anid=430628601819020001&redirected=1',
        'calories' : 22.4,
        'carbohydrates' : 4.8,
        'fat' : None,
        'alpha_linoleic_acid' : None,
        'linoleic_acid' : None,
        'protein' : 0.3,
        # Vitamins
        'vitamin_a' : None,
        'vitamin_c' : None,
        'vitamin_d' : None,
        'vitamin_e' : None,
        'vitamin_k' : None,
        'thiamin' : None,
        'riboflavin' : None,
        'niacin' : None,
        'vitamin_b6' : None,
        'folate' : None,
        'vitamin_b12' : None,
        'pantothenic_acid' : None,
        # Minerals
        'calcium' : None,
        'iron' : None,
        'magnesium' : None,
        'phosphorus' : None,
        'potassium' : None,
        'sodium' : None,
        'zinc' : None,
        'copper' : None,
        'manganese' : None,
        'selenium' : None,
    },
    {
        'name': 'Mushrooms',
        'price_per_reference_amount': 0.33,
        'reference_amount': 100,
        'amount_in_package': 450,
        'buy_here_link': None,
        # Mushrooms, white, raw
        'source_nutritional_information_link': 'https://nutritiondata.self.com/facts/vegetables-and-vegetable-products/2482/2',
        'calories' : 22,
        'carbohydrates' : 3.3,
        'fat' : 0.3,
        'alpha_linoleic_acid' : None,
        'linoleic_acid' : 0.139,
        'protein' : 3.1,
        # Vitamins
        'vitamin_a' : 0,
        'vitamin_c' : 2.1,
        'vitamin_d' : 18.0,
        'vitamin_e' : 0.0,
        'vitamin_k' : 0.0,
        'thiamin' : 0.1,
        'riboflavin' : 0.4,
        'niacin' : 3.6,
        'vitamin_b6' : 0.1,
        'folate' : 16.0,
        'vitamin_b12' : 0.0,
        'pantothenic_acid' : 1.5,
        # Minerals
        'calcium' : 3.0,
        'iron' : 0.5,
        'magnesium' : 9.0,
        'phosphorus' : 0.086,
        'potassium' : 0.318,
        'sodium' : 0.005,
        'zinc' : 0.5,
        'copper' : 0.3,
        'manganese' : 0.0,
        'selenium' : 9.3,
    },
    {
        'name': 'Walnuts',
        'price_per_reference_amount': 1.499,
        'reference_amount': 100,
        'amount_in_package': 1000,
        'buy_here_link': 'https://www.amazon.de/gp/product/B0799MYYNC/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1',
        'source_nutritional_information_link': 'https://nutritiondata.self.com/facts/nut-and-seed-products/3138/2',
        'calories' : 654,
        'carbohydrates' : 13.7,
        'fat' : 65.2,
        'alpha_linoleic_acid' : 9.079,
        'linoleic_acid' : 38.092,
        'protein' : 15.2,
        # Vitamins
        'vitamin_a' : 20.0,
        'vitamin_c' : 1.3,
        'vitamin_d' : None,
        'vitamin_e' : 0.7,
        'vitamin_k' : 2.7,
        'thiamin' : 0.3,
        'riboflavin' : 0.2,
        'niacin' : 1.1,
        'vitamin_b6' : 0.5,
        'folate' : 98.0,
        'vitamin_b12' : 0.0,
        'pantothenic_acid' : 0.6,
        # Minerals
        'calcium' : 98.0,
        'iron' : 2.9,
        'magnesium' : 158,
        'phosphorus' : 0.346,
        'potassium' : 0.441,
        'sodium' : 0.002,
        'zinc' : 3.1,
        'copper' : 1.6,
        'manganese' : 3.4,
        'selenium' : 4.9,
    },
    {
        'name': 'Whole wheat pasta',
        'price_per_reference_amount': 0.38,
        'reference_amount': 100,
        'amount_in_package': 500,
        'buy_here_link': 'https://www.getnow.com/index.php?cl=details&cnid=193&actcontrol=details&anid=430628603914340001&redirected=1',
        # macros from package, micros from nutrition data
        'source_nutritional_information_link': 'https://nutritiondata.self.com/facts/cereal-grains-and-pasta/5783/2',
        'calories' : 348,
        'carbohydrates' : 64,
        'fat' : 2.5,
        'alpha_linoleic_acid' : 0.027,
        'linoleic_acid' : 0.529,
        'protein' : 13,
        # Vitamins
        'vitamin_a' : 0.0,
        'vitamin_c' : 0.0,
        'vitamin_d' : None,
        'vitamin_e' : None,
        'vitamin_k' : None,
        'thiamin' : 0.5,
        'riboflavin' : 0.1,
        'niacin' : 5.1,
        'vitamin_b6' : 0.2,
        'folate' : 57.0,
        'vitamin_b12' : 0.0,
        'pantothenic_acid' : 1.0,
        # Minerals
        'calcium' : 40.0,
        'iron' : 3.6,
        'magnesium' : 143,
        'phosphorus' : 0.258,
        'potassium' : 0.215,
        'sodium' : 0.008,
        'zinc' : 2.4,
        'copper' : 0.5,
        'manganese' : 3.1,
        'selenium' : 73.0,
    },
    {
        'name': 'Pea protein powder',
        'price_per_reference_amount': 1.04,
        'reference_amount': 100,
        'amount_in_package': 2500,
        'buy_here_link': 'https://de.myprotein.com/sporternahrung/erbsenprotein-isolat/10530136.html',
        'source_nutritional_information_link': 'https://de.myprotein.com/sporternahrung/erbsenprotein-isolat/10530136.html',
        'calories' : 357,
        'carbohydrates' : 3.0,
        'fat' : 5.0,
        'alpha_linoleic_acid' : None,
        'linoleic_acid' : None,
        'protein' : 75,
        # Vitamins
        'vitamin_a' : None,
        'vitamin_c' : None,
        'vitamin_d' : None,
        'vitamin_e' : None,
        'vitamin_k' : None,
        'thiamin' : None,
        'riboflavin' : None,
        'niacin' : None,
        'vitamin_b6' : None,
        'folate' : None,
        'vitamin_b12' : None,
        'pantothenic_acid' : None,
        # Minerals
        'calcium' : None,
        'iron' : None,
        'magnesium' : None,
        'phosphorus' : None,
        'potassium' : None,
        'sodium' : 1,
        'zinc' : None,
        'copper' : None,
        'manganese' : None,
        'selenium' : None,
    },
    {
        'name': 'Napoletana sauce barilla',
        'price_per_reference_amount': 0.40,
        'reference_amount': 100,
        'amount_in_package': 400,
        'buy_here_link': 'https://www.getnow.com/index.php?cl=details&cnid=999&actcontrol=details&anid=430628601335060001&redirected=1',
        'source_nutritional_information_link': 'https://www.getnow.com/index.php?cl=details&cnid=999&actcontrol=details&anid=430628601335060001&redirected=1',
        'calories' : 69,
        'carbohydrates' : 6.3,
        'fat' : 4,
        'alpha_linoleic_acid' : None,
        'linoleic_acid' : None,
        'protein' : 1.4,
        # Vitamins
        'vitamin_a' : None,
        'vitamin_c' : None,
        'vitamin_d' : None,
        'vitamin_e' : None,
        'vitamin_k' : None,
        'thiamin' : None,
        'riboflavin' : None,
        'niacin' : None,
        'vitamin_b6' : None,
        'folate' : None,
        'vitamin_b12' : None,
        'pantothenic_acid' : None,
        # Minerals
        'calcium' : None,
        'iron' : None,
        'magnesium' : None,
        'phosphorus' : None,
        'potassium' : None,
        'sodium' : 0.400,
        'zinc' : None,
        'copper' : None,
        'manganese' : None,
        'selenium' : None,
    },
    {
        'name': 'Arrabiata sauce barilla',
        'price_per_reference_amount': 0.40,
        'reference_amount': 100,
        'amount_in_package': 400,
        'buy_here_link': 'https://www.getnow.com/index.php?cl=details&cnid=999&actcontrol=details&anid=430628601335060001&redirected=1',
        'source_nutritional_information_link': 'https://www.getnow.com/index.php?cl=details&cnid=999&actcontrol=details&anid=430628601335060001&redirected=1',
        'calories' : 69,
        'carbohydrates' : 6.3,
        'fat' : 4,
        'alpha_linoleic_acid' : None,
        'linoleic_acid' : None,
        'protein' : 1.4,
        # Vitamins
        'vitamin_a' : None,
        'vitamin_c' : None,
        'vitamin_d' : None,
        'vitamin_e' : None,
        'vitamin_k' : None,
        'thiamin' : None,
        'riboflavin' : None,
        'niacin' : None,
        'vitamin_b6' : None,
        'folate' : None,
        'vitamin_b12' : None,
        'pantothenic_acid' : None,
        # Minerals
        'calcium' : None,
        'iron' : None,
        'magnesium' : None,
        'phosphorus' : None,
        'potassium' : None,
        'sodium' : 0.400,
        'zinc' : None,
        'copper' : None,
        'manganese' : None,
        'selenium' : None,
    },
    {
        'name': 'Olive sauce barilla',
        'price_per_reference_amount': 0.40,
        'reference_amount': 100,
        'amount_in_package': 400,
        'buy_here_link': 'https://www.getnow.com/index.php?cl=details&cnid=999&actcontrol=details&anid=430628601335060001&redirected=1',
        'source_nutritional_information_link': 'https://www.getnow.com/index.php?cl=details&cnid=999&actcontrol=details&anid=430628601335060001&redirected=1',
        'calories' : 69,
        'carbohydrates' : 6.3,
        'fat' : 4,
        'alpha_linoleic_acid' : None,
        'linoleic_acid' : None,
        'protein' : 1.4,
        # Vitamins
        'vitamin_a' : None,
        'vitamin_c' : None,
        'vitamin_d' : None,
        'vitamin_e' : None,
        'vitamin_k' : None,
        'thiamin' : None,
        'riboflavin' : None,
        'niacin' : None,
        'vitamin_b6' : None,
        'folate' : None,
        'vitamin_b12' : None,
        'pantothenic_acid' : None,
        # Minerals
        'calcium' : None,
        'iron' : None,
        'magnesium' : None,
        'phosphorus' : None,
        'potassium' : None,
        'sodium' : 0.400,
        'zinc' : None,
        'copper' : None,
        'manganese' : None,
        'selenium' : None,
    },
    {
        'name': 'Spinach',
        'price_per_reference_amount': 0.213,
        'reference_amount': 100,
        'amount_in_package': 1000,
        'buy_here_link': 'https://www.getnow.com/Tiefkuehl/Gemuese-Kraeuter-Obst/Gemuese-Pilze/Metro-Chef-Blattspinat-Portionen-1kg.html?ffCheckoutTrackData%5Bcampaign%5D=bee2c58c-29ba-4b4e-a778-51a67f8aba0f&listtype=search&searchparam=spinat',
        'source_nutritional_information_link': 'https://nutritiondata.self.com/facts/vegetables-and-vegetable-products/2626/2',
        'calories' : 23.0,
        'carbohydrates' : 3.6,
        'fat' : 0.4,
        'alpha_linoleic_acid' : 0.138,
        'linoleic_acid' : 0.026,
        'protein' : 2.9,
        # Vitamins
        # vitamin a IU: 9376 from https://nutritiondata.self.com/facts/vegetables-and-vegetable-products/2626/2
        # converted assuming Retinol and using conversion factor from
        # https://dietarysupplementdatabase.usda.nih.gov/ingredient_calculator/help.php
        'vitamin_a' :  2812.8,
        'vitamin_c' : 28.1,
        'vitamin_d' : None,
        'vitamin_e' : 2.0,
        'vitamin_k' : 483,
        'thiamin' : 0.1,
        'riboflavin' : 0.2,
        'niacin' : 0.7,
        'vitamin_b6' : 0.2,
        'folate' : 194,
        'vitamin_b12' : 0.0,
        'pantothenic_acid' : 0.1,
        # Minerals
        'calcium' : 99.0,
        'iron' : 2.7,
        'magnesium' : 79.0,
        'phosphorus' : 0.049,
        'potassium' : 0.558,
        'sodium' : 0.079,
        'zinc' : 0.5,
        'copper' : 0.1,
        'manganese' : 0.9,
        'selenium' : 1.0,
    },
    {
        'name': 'Multivitamin A-Z Komplett Mivolis dm',
        'reference_amount': 1,
        'calories': 0,
        'carbohydrates': 0,
        'fat': 0,
        'protein': 0,
        'linoleic_acid': 0,
        'alpha_linoleic_acid': 0,
        'vitamin_a': 400,
        'vitamin_c': 80,
        'vitamin_d': 5,
        'vitamin_e': 12,
        'vitamin_k': 75,
        'thiamin': 1.1,
        'riboflavin': 1.4,
        'niacin': 16,
        'vitamin_b6': 1.4,
        'folate': 200,
        'vitamin_b12': 2.5,
        'pantothenic_acid': 6,
        'biotin': 50,
        'choline': 0,
        'calcium': 200,
        'chromium': 40,
        'copper': 0,
        'fluoride': 0,
        'iodine': 100,
        'iron': 0,
        'magnesium': 100,
        'manganese': 0,
        'molybdenum': 50,
        'phosphorus': 125,
        'selenium': 25,
        'zinc': 2.25,
        'potassium': 0,
        'sodium': 0,
        'chloride': 0,
        'buy_here_link': None,
        'source_nutritional_information_link': None, # package
    },
    {
        'name': 'Vitamin D3 Tablette Vitabay 5000 I.E.',
        'reference_amount': 1,
        'calories': 0,
        'carbohydrates': 0,
        'fat': 0,
        'protein': 0,
        'linoleic_acid': 0,
        'alpha_linoleic_acid': 0,
        'vitamin_a': 0,
        'vitamin_c': 0,
        'vitamin_d': 125,
        'vitamin_e': 0,
        'vitamin_k': 0,
        'thiamin': 0,
        'riboflavin': 0,
        'niacin': 0,
        'vitamin_b6': 0,
        'folate': 0,
        'vitamin_b12': 0,
        'pantothenic_acid': 0,
        'biotin': 0,
        'choline': 0,
        'calcium': 0,
        'chromium': 0,
        'copper': 0,
        'fluoride': 0,
        'iodine': 0,
        'iron': 0,
        'magnesium': 0,
        'manganese': 0,
        'molybdenum': 0,
        'phosphorus': 0,
        'selenium': 0,
        'zinc': 0,
        'potassium': 0,
        'sodium': 0,
        'chloride': 0,
        'buy_here_link': None,
        'source_nutritional_information_link': None,
    },
    {
        'name': 'Iron tablets, gentle iron',
        'reference_amount': 1,
        'calories': 0,
        'carbohydrates': 0,
        'fat': 0,
        'protein': 0,
        'linoleic_acid': 0,
        'alpha_linoleic_acid': 0,
        'vitamin_a': 0,
        'vitamin_c': 0,
        'vitamin_d': 0,
        'vitamin_e': 0,
        'vitamin_k': 0,
        'thiamin': 0,
        'riboflavin': 0,
        'niacin': 0,
        'vitamin_b6': 0,
        'folate': 0,
        'vitamin_b12': 0,
        'pantothenic_acid': 0,
        'biotin': 0,
        'choline': 0,
        'calcium': 0,
        'chromium': 0,
        'copper': 0,
        'fluoride': 0,
        'iodine': 0,
        'iron': 25,
        'magnesium': 0,
        'manganese': 0,
        'molybdenum': 0,
        'phosphorus': 0,
        'selenium': 0,
        'zinc': 0,
        'potassium': 0,
        'sodium': 0,
        'chloride': 0,
        'buy_here_link': None,
        'source_nutritional_information_link': None,
    },
    {
        'name': 'Vitamin B12 tablets Nu U',
        'reference_amount': 1,
        'calories': 0,
        'carbohydrates': 0,
        'fat': 0,
        'protein': 0,
        'linoleic_acid': 0,
        'alpha_linoleic_acid': 0,
        'vitamin_a': 0,
        'vitamin_c': 0,
        'vitamin_d': 0,
        'vitamin_e': 0,
        'vitamin_k': 0,
        'thiamin': 0,
        'riboflavin': 0,
        'niacin': 0,
        'vitamin_b6': 0,
        'folate': 0,
        'vitamin_b12': 1000,
        'pantothenic_acid': 0,
        'biotin': 0,
        'choline': 0,
        'calcium': 0,
        'chromium': 0,
        'copper': 0,
        'fluoride': 0,
        'iodine': 0,
        'iron': 0,
        'magnesium': 0,
        'manganese': 0,
        'molybdenum': 0,
        'phosphorus': 0,
        'selenium': 0,
        'zinc': 0,
        'potassium': 0,
        'sodium': 0,
        'chloride': 0,
        'buy_here_link': None,
        'source_nutritional_information_link': None,
    },
    {
        'name': 'Zink bisglycinat Nature Love',
        'reference_amount': 1,
        'calories': 0,
        'carbohydrates': 0,
        'fat': 0,
        'protein': 0,
        'linoleic_acid': 0,
        'alpha_linoleic_acid': 0,
        'vitamin_a': 0,
        'vitamin_c': 0,
        'vitamin_d': 0,
        'vitamin_e': 0,
        'vitamin_k': 0,
        'thiamin': 0,
        'riboflavin': 0,
        'niacin': 0,
        'vitamin_b6': 0,
        'folate': 0,
        'vitamin_b12': 0,
        'pantothenic_acid': 0,
        'biotin': 0,
        'choline': 0,
        'calcium': 0,
        'chromium': 0,
        'copper': 0,
        'fluoride': 0,
        'iodine': 0,
        'iron': 0,
        'magnesium': 0,
        'manganese': 0,
        'molybdenum': 0,
        'phosphorus': 0,
        'selenium': 0,
        'zinc': 25,
        'potassium': 0,
        'sodium': 0,
        'chloride': 0,
        'buy_here_link': None,
        'source_nutritional_information_link': None,
    },
    {
        'name': 'Salt, iodized',
        'reference_amount': 100,
        'calories': 0,
        'carbohydrates': 0,
        'fat': 0,
        'protein': 0,
        'linoleic_acid': 0,
        'alpha_linoleic_acid': 0,
        'vitamin_a': 0,
        'vitamin_c': 0,
        'vitamin_d': 0,
        'vitamin_e': 0,
        'vitamin_k': 0,
        'thiamin': 0,
        'riboflavin': 0,
        'niacin': 0,
        'vitamin_b6': 0,
        'folate': 0,
        'vitamin_b12': 0,
        'pantothenic_acid': 0,
        'biotin': 0,
        'choline': 0,
        'calcium': 0,
        'chromium': 0,
        'copper': 0,
        'fluoride': 31,
        'iodine': 2000,
        'iron': 0,
        'magnesium': 0,
        'manganese': 0,
        'molybdenum': 0,
        'phosphorus': 0,
        'selenium': 0,
        'zinc': 0,
        'potassium': 0,
        'sodium': 38.758,
        'chloride': 0,
        'buy_here_link': None,
        'source_nutritional_information_link': None,  # package aro Jodsalz von getnow
    },
    {
        'name': 'Magnesium citrate',
        'reference_amount': 100,
        'calories': 0,
        'carbohydrates': 0,
        'fat': 0,
        'protein': 0,
        'linoleic_acid': 0,
        'alpha_linoleic_acid': 0,
        'vitamin_a': 0,
        'vitamin_c': 0,
        'vitamin_d': 0,
        'vitamin_e': 0,
        'vitamin_k': 0,
        'thiamin': 0,
        'riboflavin': 0,
        'niacin': 0,
        'vitamin_b6': 0,
        'folate': 0,
        'vitamin_b12': 0,
        'pantothenic_acid': 0,
        'biotin': 0,
        'choline': 0,
        'calcium': 0,
        'chromium': 0,
        'copper': 0,
        'fluoride': 0,
        'iodine': 0,
        'iron': 0,
        'magnesium': 8340,
        'manganese': 0,
        'molybdenum': 0,
        'phosphorus': 0,
        'selenium': 0,
        'zinc': 0,
        'potassium': 0,
        'sodium': 0,
        'chloride': 0,
        'buy_here_link': None,
        'source_nutritional_information_link': None,  # package
    },
    {
        'name': 'Potassium citrate',
        'reference_amount': 100,
        'calories': 0,
        'carbohydrates': 0,
        'fat': 0,
        'protein': 0,
        'linoleic_acid': 0,
        'alpha_linoleic_acid': 0,
        'vitamin_a': 0,
        'vitamin_c': 0,
        'vitamin_d': 0,
        'vitamin_e': 0,
        'vitamin_k': 0,
        'thiamin': 0,
        'riboflavin': 0,
        'niacin': 0,
        'vitamin_b6': 0,
        'folate': 0,
        'vitamin_b12': 0,
        'pantothenic_acid': 0,
        'biotin': 0,
        'choline': 0,
        'calcium': 0,
        'chromium': 0,
        'copper': 0,
        'fluoride': 0,
        'iodine': 0,
        'iron': 0,
        'magnesium': 0,
        'manganese': 0,
        'molybdenum': 0,
        'phosphorus': 0,
        'selenium': 0,
        'zinc': 0,
        'potassium': 36,
        'sodium': 0,
        'chloride': 0,
        'buy_here_link': None,
        'source_nutritional_information_link': None,
    },
    {
        'name': 'Vitamin B-Komplex ratiopharm',
        'reference_amount': 1,
        'calories': 0,
        'carbohydrates': 0,
        'fat': 0,
        'protein': 0,
        'linoleic_acid': 0,
        'alpha_linoleic_acid': 0,
        'vitamin_a': 0,
        'vitamin_c': 0,
        'vitamin_d': 0,
        'vitamin_e': 0,
        'vitamin_k': 0,
        'thiamin': 15,
        'riboflavin': 15,
        'niacin': 15,
        'vitamin_b6': 10,
        'folate': 450,
        'vitamin_b12': 10,
        'pantothenic_acid': 25,
        'biotin': 150,
        'choline': 0,
        'calcium': 0,
        'chromium': 0,
        'copper': 0,
        'fluoride': 0,
        'iodine': 0,
        'iron': 0,
        'magnesium': 0,
        'manganese': 0,
        'molybdenum': 0,
        'phosphorus': 0,
        'selenium': 0,
        'zinc': 0,
        'potassium': 0,
        'sodium': 0,
        'chloride': 0,
        'buy_here_link': None,
        'source_nutritional_information_link': None,  # package
    },
    {
        'name': 'Complete Multivitamin Komplex Tabletten Bulkpowders',
        'reference_amount': 3,
        'calories': None,  # 'default_unit': 'kcal'
        'carbohydrates': None,  # 'default_unit': 'gram'
        'fat': None,  # 'default_unit': 'gram'
        'protein': None,  # 'default_unit': 'gram'
        'linoleic_acid': None,  # 'default_unit': 'gram'
        'alpha_linoleic_acid': None,  # 'default_unit': 'gram'
        'vitamin_a': 400,  #'default_unit': 'microgram'
        'vitamin_c': 150,  # 'default_unit': 'milligram'
        'vitamin_d': 25,  #'default_unit': 'microgram'
        'vitamin_e': 10.5,  # 'default_unit': 'milligram'
        'vitamin_k': 100,  # 'default_unit': 'microgram'
        'thiamin': 25,
        'riboflavin': 25,
        'niacin': 25,
        'vitamin_b6': 25,  # 'default_unit': 'milligram'
        'folate': 400,  # 'default_unit': 'microgram'
        'vitamin_b12': 100,  # 'default_unit': 'microgram'
        'pantothenic_acid': 25,  #'default_unit': 'milligram'
        'biotin': 150,  # 'default_unit': 'microgram'
        'choline': 61,
        'calcium': 495,  # 'default_unit': 'milligram'
        'chromium': 100,  # 'default_unit': 'microgram'
        'copper': 100,  # 'default_unit': 'microgram'
        'fluoride': None,  # 'default_unit': 'milligram'
        'iodine': None,  # 'default_unit': 'microgram'
        'iron': 14.1,  # 'default_unit': 'milligram'
        'magnesium': 150,  # 'default_unit': 'milligram'
        'manganese': 0.100,  # 'default_unit': 'milligram'
        'molybdenum': None,  # 'default_unit': 'microgram'
        'phosphorus': None,  # 'default_unit': 'milligram'
        'selenium': 55,  # 'default_unit': 'microgram'
        'zinc': 15,  # 'default_unit': 'milligram'
        'potassium': None,  # 'default_unit': 'gram'
        'sodium': None,  # 'default_unit': 'gram'
        'chloride': None,  # 'default_unit': 'gram'
        'buy_here_link': 'https://www.bulkpowders.de/complete-multivitamin-komplex-de.html',
        'source_nutritional_information_link': 'https://www.bulkpowders.de/complete-multivitamin-komplex-de.html',
    },
    {
        'name': 'Multivitamin vitasyg',  # Best multivitamin tablet.
        'reference_amount': 1,  # default: 100 g
        'calories': None,  # 'default_unit': 'kcal'
        'carbohydrates': None,  # 'default_unit': 'gram'
        'fat': None,  # 'default_unit': 'gram'
        'protein': None,  # 'default_unit': 'gram'
        'linoleic_acid': None,  # 'default_unit': 'gram'
        'alpha_linoleic_acid': None,  # 'default_unit': 'gram'
        'vitamin_a': 800,  #'default_unit': 'microgram'
        'vitamin_c': 80,  # 'default_unit': 'milligram'
        'vitamin_d': 5,  #'default_unit': 'microgram'
        'vitamin_e': 12,  # 'default_unit': 'milligram'
        'vitamin_k': 75,  # 'default_unit': 'microgram'
        'thiamin': 1.1,  # 'default_unit': 'milligram'
        'riboflavin': 1.4,  # 'default_unit': 'milligram'
        'niacin': 16,  # 'default_unit': 'milligram'
        'vitamin_b6': 1.4,  # 'default_unit': 'milligram'
        'folate': 200,  # 'default_unit': 'microgram'
        'vitamin_b12': 2.5,  # 'default_unit': 'microgram'
        'pantothenic_acid': 6,  #'default_unit': 'milligram'
        'biotin': 50,  # 'default_unit': 'microgram'
        'choline': None,  # 'default_unit': 'milligram'
        'calcium': 200,  # 'default_unit': 'milligram'
        'chromium': 20,  # 'default_unit': 'microgram'
        'copper': 1000,  # 'default_unit': 'microgram'
        'fluoride': None,  # 'default_unit': 'milligram'
        'iodine': 150,  # 'default_unit': 'microgram'
        'iron': 14,  # 'default_unit': 'milligram'
        'magnesium': 75,  # 'default_unit': 'milligram'
        'manganese': 2,  # 'default_unit': 'milligram'
        'molybdenum': 25,  # 'default_unit': 'microgram'
        'phosphorus': 40,  # 'default_unit': 'milligram'
        'selenium': 55,  # 'default_unit': 'microgram'
        'zinc': 10,  # 'default_unit': 'milligram'
        'potassium': 0.04,  # 'default_unit': 'gram'
        'sodium': None,  # 'default_unit': 'gram'
        'chloride': 0.036,  # 'default_unit': 'gram'
        'buy_here_link': 'https://www.amazon.de/dp/B01NCIZG7B/?tag=glv-21&ascsubtag=3770aba8-0eac-417e-9c01-448e295cce7a',
        'source_nutritional_information_link': 'https://www.amazon.de/dp/B01NCIZG7B/?tag=glv-21&ascsubtag=3770aba8-0eac-417e-9c01-448e295cce7a',
    },
    {
        'name': 'Calcium citrate',
        'reference_amount': None,  # default: 100 g
        'calories': None,  # 'default_unit': 'kcal'
        'carbohydrates': None,  # 'default_unit': 'gram'
        'fat': None,  # 'default_unit': 'gram'
        'protein': None,  # 'default_unit': 'gram'
        'linoleic_acid': None,  # 'default_unit': 'gram'
        'alpha_linoleic_acid': None,  # 'default_unit': 'gram'
        'vitamin_a': None,  #'default_unit': 'microgram'
        'vitamin_c': None,  # 'default_unit': 'milligram'
        'vitamin_d': None,  #'default_unit': 'microgram'
        'vitamin_e': None,  # 'default_unit': 'milligram'
        'vitamin_k': None,  # 'default_unit': 'microgram'
        'thiamin': None,  # 'default_unit': 'milligram'
        'riboflavin': None,  # 'default_unit': 'milligram'
        'niacin': None,  # 'default_unit': 'milligram'
        'vitamin_b6': None,  # 'default_unit': 'milligram'
        'folate': None,  # 'default_unit': 'microgram'
        'vitamin_b12': None,  # 'default_unit': 'microgram'
        'pantothenic_acid': None,  #'default_unit': 'milligram'
        'biotin': None,  # 'default_unit': 'microgram'
        'choline': None,  # 'default_unit': 'milligram'
        'calcium': None,  # 'default_unit': 'milligram'
        'chromium': None,  # 'default_unit': 'microgram'
        'copper': None,  # 'default_unit': 'microgram'
        'fluoride': None,  # 'default_unit': 'milligram'
        'iodine': None,  # 'default_unit': 'microgram'
        'iron': None,  # 'default_unit': 'milligram'
        'magnesium': None,  # 'default_unit': 'milligram'
        'manganese': None,  # 'default_unit': 'milligram'
        'molybdenum': None,  # 'default_unit': 'microgram'
        'phosphorus': None,  # 'default_unit': 'milligram'
        'selenium': None,  # 'default_unit': 'microgram'
        'zinc': None,  # 'default_unit': 'milligram'
        'potassium': None,  # 'default_unit': 'gram'
        'sodium': None,  # 'default_unit': 'gram'
        'chloride': None,  # 'default_unit': 'gram'
        'buy_here_link': None,
        'source_nutritional_information_link': None,
    },
]
