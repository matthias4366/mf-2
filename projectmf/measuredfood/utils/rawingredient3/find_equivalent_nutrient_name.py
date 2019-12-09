

def find_equivalent_nutrient_name(
    all_nutrients_and_default_units,
    nutrient_name_from_usda,
):
    """
    The function
    find_equivalent_nutrient_name takes in a nutrient name returned from the
    FoodData Central API and finds the equivalent nutrient name in the
    measuredfood database.
    :param all_nutrients_and_default_units: This list of dictionaries
    contains all the nutrients and default units. It is used to set up the
    fields of the RawIngredient3 model. Therefore, it determines which
    nutritional information is stored for the ingredients in the measuredfood
    database, under what name and which units are used..
    :param nutrient_name_from_usda: The nutrient name returned from the
    FoodData Central API.
    :return: equivalent_nutrient_name_measuredfood
    """
    equivalent_nutrient_name_measuredfood = None
    for nutrient_dict in all_nutrients_and_default_units:
        # print(f'nutrient_dict[\'nutrient_name_usda_api\']:')
        print(nutrient_dict)
        # print('True or not?')
        # print(nutrient_dict['nutrient_name_usda_api'] ==
        #       nutrient_name_from_usda)
        if nutrient_dict['nutrient_name_usda_api'] == \
                nutrient_name_from_usda:
            equivalent_nutrient_name_measuredfood = \
                nutrient_dict[
                    'nutrient_name_measuredfood']
    return equivalent_nutrient_name_measuredfood
