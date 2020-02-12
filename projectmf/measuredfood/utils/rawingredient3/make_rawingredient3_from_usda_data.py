

def make_rawingredient3_from_usda_data(
    rawingredient3_model,
    request,
    response_json,
    transform_nutrient_name_usda_to_measuredfood,
):
    """
    :param rawingredient3_model: The RawIngredient3 model.
    :param request: Django request object used to get the user who made the
    request, which is necessary to correctly set the author of the
    RawIngredient3 instance.
    :param response_json: Response from the FoodData Central API, in JSON form.
    :param transform_nutrient_name_usda_to_measuredfood: This function
    takes in the ingredient name from the usda database, works on the string,
    and return the name for the measuredfood database.
    :return: rawingredient3_instance: Based on the JSON data on the
    ingredient obtained from the FoodData Central API, a RawIngredient3 model
    object has been created and it is returned.
    """

    if rawingredient3_model.objects.filter(name=response_json[
        'description']).exists():
        name_ = make

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
            nutrient_name_usda_api = \
                response_json['foodNutrients'][k]['nutrient'][
                    'name']
            id_nutrient_usda_api = \
                response_json['foodNutrients'][k]['nutrient'][
                    'id']
            # print('nutrient_name_from_usda')
            # print(nutrient_name_from_usda)

            equivalent_nutrient_name_measuredfood = \
                transform_nutrient_name_usda_to_measuredfood(
                    nutrient_name_usda_api,
                    id_nutrient_usda_api,
                )
            # print('\n equivalent_nutrient_name_measuredfood')
            # print(equivalent_nutrient_name_measuredfood)
            setattr(
                rawingredient3_instance,
                equivalent_nutrient_name_measuredfood,
                amount_from_usda
            )
    return rawingredient3_instance
