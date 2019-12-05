

def make_rawingredient3_from_usda_data(
    rawingredient3_model,
    request,
    response_json,
    all_nutrients_and_default_units,
):
    """

    :param rawingredient3_model: The RawIngredient3 model.
    :param request: Django request object used to get the user who made the
    request, which is necessary to correctly set the author of the
    RawIngredient3 instance.
    :param response_json: Response from the FoodData Central API, in JSON form.
    :param all_nutrients_and_default_units: Dictionary contained in
    ingredient_properties3.py. It is a collection of all nutrients, such as
    'carbohydrates' etc., and the default unit for each nutrient, such as
    gram ('g') for 'carbohydrates'.
    :return: rawingredient3_instance: Based on the JSON data on the
    ingredient obtained from the FoodData Central API, a RawIngredient3 model
    object has been created and it is returned.
    """
    rawingredient3_instance = rawingredient3_model(
        author=request.user,
        name=response_json['description']
    )

    for k in range(len(response_json['foodNutrients'])):
        # print(f'k: {k}')
        # Check if the amount is in the current dictionary:
        if 'amount' in response_json['foodNutrients'][k]:
            amount_from_usda = \
                response_json['foodNutrients'][k]['amount']
            nutrient_name_from_usda = \
                response_json['foodNutrients'][k]['nutrient'][
                    'name']
            # print('nutrient_name_from_usda')
            # print(nutrient_name_from_usda)

            equivalent_nutrient_name_measuredfood = None
            for nutrient_dict in all_nutrients_and_default_units:
                # print(f'nutrient_dict[\'name_usda\']:')
                # print(nutrient_dict['name_usda'])
                # print('True or not?')
                # print(nutrient_dict['name_usda'] ==
                #       nutrient_name_from_usda)
                if nutrient_dict['name_usda'] == \
                        nutrient_name_from_usda:
                    equivalent_nutrient_name_measuredfood = \
                        nutrient_dict[
                            'name_measuredfood']

            # print(f'equivalent_nutrient_name_measuredfood: '
            #       f'{equivalent_nutrient_name_measuredfood}')
            # print(f'amount_from_usda: '
            #       f'{amount_from_usda}')

            setattr(
                rawingredient3_instance,
                equivalent_nutrient_name_measuredfood,
                amount_from_usda)
    return rawingredient3_instance
