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
                    'amount': 0,
                    'unit': '',
                    'rawingredient2': '',
                    'scaling': '',
                },
            ]

    }

full_day_of_eating_dict_list = [
    {
        'name': 'Olive sauce and pasta added from initial data',
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
                    'amount': 400,
                    'unit': 'gram',
                    'rawingredient2': 'Olive sauce barilla',
                    'scaling': 'fixed',
                },
                {
                    'amount': 200,
                    'unit': 'gram',
                    'rawingredient2': 'Spinach',
                    'scaling': 'fixed',
                },
                {
                    'amount': 100,
                    'unit': 'gram',
                    'rawingredient2': 'Pea protein powder',
                    'scaling': 'independent',
                },
                {
                    'amount': 400,
                    'unit': 'gram',
                    'rawingredient2': 'Whole wheat pasta',
                    'scaling': 'independent',
                },
                {
                    'amount': 60,
                    'unit': 'gram',
                    'rawingredient2': 'Walnuts',
                    'scaling': 'fixed',
                },
                {
                    'amount': None,
                    'unit': None,
                    'rawingredient2': None,
                    'scaling': None,
                },
                {
                    'amount': None,
                    'unit': None,
                    'rawingredient2': None,
                    'scaling': None,
                },
                {
                    'amount': None,
                    'unit': None,
                    'rawingredient2': None,
                    'scaling': None,
                },
                {
                    'amount': None,
                    'unit': None,
                    'rawingredient2': None,
                    'scaling': None,
                },
                {
                    'amount': None,
                    'unit': None,
                    'rawingredient2': None,
                    'scaling': None,
                },
                {
                    'amount': None,
                    'unit': None,
                    'rawingredient2': None,
                    'scaling': None,
                },
            ]

    }
]
