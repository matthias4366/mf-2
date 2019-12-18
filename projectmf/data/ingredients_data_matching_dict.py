"""
RawIngredient2 has been updated from RawIngredient3. Therefore, the nutrient
fields have new names. Therefore, the nutrient fields in the dictionaries
stored in ingredients_data2.py have to be renamed. The
ingredients_data_matching_dict matches the old field name from RawIngredient2
to the new field name in RawIngredient3.

Fields that do not exist in RawIngredient3 are marked as 'REMOVED'.
"""
ingredients_data_matching_dict =     \
    {
        'name': 'name',
        'buy_here_link': 'buy_here_link',
        'source_nutritional_information_link':
            'source_nutritional_information_link',
        'is_public': 'REMOVED',
        'reference_amount': 'REMOVED',
        'price_per_reference_amount': 'price_per_reference_amount',
        'calories': 'energy-name-1008-id',
        'carbohydrates': 'carbohydrate_without_fiber-name-1-id',
        'fat': None,
        'protein': None,
        'linoleic_acid': None,
        'alpha_linoleic_acid': None,
        # Vitamin A unit conversion:
        # Vitamin A: 1 IU is the biological equivalent of 0.3 mcg retinol,
        # or of 0.6 mcg beta-carotene
        # Source: https://dietarysupplementdatabase.usda.nih.gov/
        # ingredient_calculator/help.php
        # => * 0.3
        'vitamin_a': None,
        'vitamin_c': None,
        'vitamin_d': None,
        'vitamin_e': None,
        'vitamin_k': None,
        'thiamin': None,
        'riboflavin': None,
        'niacin': None,
        'vitamin_b6': None,
        'folate': None,
        'vitamin_b12': None,
        'pantothenic_acid': None,  # 'default_unit': 'milligram'
        'biotin': None,  # 'default_unit': 'microgram'
        'choline': None,  # 'default_unit': 'milligram'
        'calcium': None,  # 'default_unit': 'milligram'
        'chromium': None,  # 'default_unit': 'microgram'
        'copper': None,  # 'default_unit': 'microgram'
        # Since fluoride is added to salt, it makes sense to track it.
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
    }
