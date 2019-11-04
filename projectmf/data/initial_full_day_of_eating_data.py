"""

Fried rice:
Original recipe:

https://www.youtube.com/watch?v=dsNwv6tsR68

Veg:

Original:
Broccoli - added to fixtures.
Carrots - added to fixtures.
Peas
Mushrooms
1 handful green onions.
green beans.
Celery
cabbage
bok choi
Spices:
garlic powder
pepper
soy sauce


My version:
Broccoli - added to fixtures.
Carrots - added to fixtures.
Peas - added to fixtures.
Mushrooms - added to fixtures.
test [1 handful green onions]
green beans - added to fixtures.
test [bok choi]
Spices:
test [Garlic powder]
Maggi sauce - added to fixtures.

Calculation results:
391.51 	gram 	Rice, white, long-grain, regular, raw, unenriched 	Buy
97.88 	gram 	Green beans 	Buy
19.58 	gram 	Maggi 	Buy
97.88 	gram 	Broccoli 	Buy
97.88 	gram 	Carrot 	Buy
97.88 	gram 	Peas 	Buy
160.61 	gram 	Pea protein powder 	Buy
45.0 	gram 	Walnuts 	Buy


"""

full_day_of_eating_dict_template = \
    [


        {
            'name': '',
            'cooking_instruction': '',
            'nutrient_profile': '',
            'list_nutrient_target':
                [
                    'calories',
                    'protein'
                ],
            'list_dict_specific_ingredient':
                [
                    {
                        'base_amount': 0,
                        'base_amount_unit': 'gram',
                        'rawingredient': '',
                        'scaling_option': '',
                    },
                ]

        },


    ]

full_day_of_eating_dict_list = \
    [
        {
            'name': 'Olive sauce and pasta',
            'cooking_instruction': '',
            'nutrient_profile': 'Maintenance EU',
            'list_nutrient_target':
                [
                    'calories',
                    'protein'
                ],
            'list_dict_specific_ingredient':
                [
                    {
                        'base_amount': 400,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Olive sauce barilla',
                        'scaling_option': 'fixed',
                    },
                    {
                        'base_amount': 200,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Spinach',
                        'scaling_option': 'fixed',
                    },
                    {
                        'base_amount': 100,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Pea protein powder',
                        'scaling_option': 'independent',
                    },
                    {
                        'base_amount': 400,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Whole wheat pasta',
                        'scaling_option': 'independent',
                    },
                    {
                        'base_amount': 60,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Walnuts',
                        'scaling_option': 'fixed',
                    },
                ]
        },
        {
            'name': 'Chili mexican',
            'cooking_instruction': '',
            'nutrient_profile': 'Maintenance EU',
            'list_nutrient_target':
                [
                    'calories',
                    'protein'
                ],
            'list_dict_specific_ingredient':
                [
                    {
                        'base_amount': 200,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Beans, pinto, mature seeds, raw',
                        'scaling_option': 'A',
                    },
                    {
                        'base_amount': 200,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Rice, white, long-grain, regular, '
                                         'raw, unenriched',
                        'scaling_option': 'A',
                    },
                    {
                        'base_amount': 320,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Water for white rice',
                        'scaling_option': 'A',
                    },
                    {
                        'base_amount': 1,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Salt for water for white rice',
                        'scaling_option': 'A',
                    },
                    {
                        'base_amount': 285,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Corn',
                        'scaling_option': 'fixed',
                    },
                    {
                        'base_amount': 100,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Pea protein powder',
                        'scaling_option': 'independent',
                    },
                    {
                        'base_amount': 0.63,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Chili powder',
                        'scaling_option': 'fixed',
                    },
                    {
                        'base_amount': 325,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Tomato puree, MUTTI',
                        'scaling_option': 'fixed',
                    },
                    {
                        'base_amount': 60,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Walnuts',
                        'scaling_option': 'fixed',
                    },
                    {
                        'base_amount': 5,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Coriander',
                        'scaling_option': 'fixed',
                    },
                ]
        },
        {
            'name': 'Napoletana',
            'cooking_instruction': '',
            'nutrient_profile': 'Maintenance EU',
            'list_nutrient_target':
                [
                    'calories',
                    'protein'
                ],
            'list_dict_specific_ingredient':
                [
                    {
                        'base_amount': 400,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Napoletana sauce barilla',
                        'scaling_option': 'fixed',
                    },
                    {
                        'base_amount': 100,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Whole wheat pasta',
                        'scaling_option': 'independent',
                    },
                    {
                        'base_amount': 100,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Pea protein powder',
                        'scaling_option': 'independent',
                    },
                    {
                        'base_amount': 60,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Walnuts',
                        'scaling_option': 'fixed',
                    },
                    {
                        'base_amount': 200,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Carrot',
                        'scaling_option': 'fixed',
                    },
                    {
                        'base_amount': 200,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Peas',
                        'scaling_option': 'fixed',
                    },
                ]
        },
        {
            'name': 'Chili mushrooms',
            'cooking_instruction': '',
            'nutrient_profile': 'Maintenance EU',
            'list_nutrient_target':
                [
                    'calories',
                    'protein'
                ],
            'list_dict_specific_ingredient':
                [
                    {
                        'base_amount': 60,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Walnuts',
                        'scaling_option': 'fixed',
                    },
                    {
                        'base_amount': 225,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Mushrooms',
                        'scaling_option': 'fixed',
                    },
                    {
                        'base_amount': 350,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Tomato puree, MUTTI',
                        'scaling_option': 'fixed',
                    },
                    {
                        'base_amount': 0.63,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Chili powder',
                        'scaling_option': 'fixed',
                    },
                    {
                        'base_amount': 100,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Pea protein powder',
                        'scaling_option': 'independent',
                    },
                    {
                        'base_amount': 200,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Rice, white, long-grain, '
                                         'regular, raw, unenriched',
                        'scaling_option': 'A',
                    },
                    {
                        'base_amount': 200,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Kidney beans, raw',
                        'scaling_option': 'A',
                    },
                    {
                        'base_amount': 5,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Oregano',
                        'scaling_option': 'fixed',
                    },
                ]
        },
        {
            'name': 'Fried rice',
            'cooking_instruction':
                """
                Original recipe:

                https://www.youtube.com/watch?v=dsNwv6tsR68
                
                Veg:
                
                Original:
                Broccoli - added to fixtures.
                Carrots - added to fixtures.
                Peas
                Mushrooms
                1 handful green onions.
                green beans.
                Celery
                cabbage
                bok choi
                Spices:
                garlic powder
                pepper
                soy sauce
                
                
                My version:
                Broccoli - added to fixtures.
                Carrots - added to fixtures.
                Peas - added to fixtures.
                Mushrooms - added to fixtures.
                test [1 handful green onions]
                green beans - added to fixtures.
                test [bok choi]
                Spices:
                test [Garlic powder]
                Maggi sauce - added to fixtures.
                
                Just add Maggi sauce to taste.
                
                """,
            'nutrient_profile': 'Maintenance EU',
            'list_nutrient_target':
                [
                    'calories',
                    'protein'
                ],
            'list_dict_specific_ingredient':
                [
                    {
                        'base_amount': 100,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Rice, white, long-grain, '
                                         'regular, raw, unenriched',
                        'scaling_option': 'A',
                    },
                    {
                        'base_amount': 100,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Pea protein powder',
                        'scaling_option': 'independent',
                    },
                    {
                        'base_amount': 60,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Walnuts',
                        'scaling_option': 'fixed',
                    },
                    {
                        'base_amount': 225,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Mushrooms',
                        'scaling_option': 'fixed',
                    },
                    {
                        'base_amount': 5,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Maggi',
                        'scaling_option': 'A',
                    },
                    {
                        'base_amount': 25,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Carrot',
                        'scaling_option': 'A',
                    },
                    {
                        'base_amount': 25,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Peas',
                        'scaling_option': 'A',
                    },
                    {
                        'base_amount': 25,
                        'base_amount_unit': 'gram',
                        'rawingredient': 'Broccoli',
                        'scaling_option': 'A',
                    },
                ]
        },
    ]
