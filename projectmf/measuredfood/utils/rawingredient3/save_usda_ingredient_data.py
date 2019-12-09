

def make_rawingredient3_from_usda_data(
    rawingredient3_model,
    request,
    response_json,
    all_nutrients_and_default_units,
    find_equivalent_nutrient_name,
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
    :param find_equivalent_nutrient_name: The function
    find_equivalent_nutrient_name takes in a nutrient name returned from the
    FoodData Central API and finds the equivalent nutrient name in the
    measuredfood database.
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
            nutrient_id = \
                response_json['foodNutrients'][k]['nutrient'][
                    'id']
            # print('nutrient_name_from_usda')
            # print(nutrient_name_from_usda)

            equivalent_nutrient_name_measuredfood = \
                find_equivalent_nutrient_name(
                    all_nutrients_and_default_units,
                    nutrient_name_from_usda,
                )

            if equivalent_nutrient_name_measuredfood is None:
                file_name_to_save_message = \
                    'nutrients_missing_from_measuredfood_database.txt'
                message_missing_nutrient = '\n' \
                    + 'The following nutrient name from the FoodCentral ' \
                    + 'database was not found in the measured food database:'\
                    + f'nutrient_name_from_usda: {nutrient_name_from_usda}'\
                    + f'nutrient_id: {nutrient_id}'\
                    + '\n'
                with open(file_name_to_save_message, 'w') as outfile:
                    outfile.write(message_missing_nutrient)
            else:
                setattr(
                    rawingredient3_instance,
                    equivalent_nutrient_name_measuredfood,
                    amount_from_usda)
    return rawingredient3_instance
