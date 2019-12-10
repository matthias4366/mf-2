

def transform_ingredient_name_usda_to_measuredfood(
    nutrient_dict,
):
    """

    :param nutrient_dict:
    :return:
    """

    # print('\nnutrient_dict[\'nutrient_name_usda_api\']')
    # print(nutrient_dict['nutrient_name_usda_api'])

    if len(nutrient_dict['nutrient_name_usda_api']) < 1:
        raise Exception()

    ingredient_name_measuredfood = \
        nutrient_dict['nutrient_name_usda_api'] \
        + '-' \
        + 'name' \
        + '-' \
        + nutrient_dict['id_nutrient_usda_api'] \
        + '-' \
        + 'id'

    ingredient_name_measuredfood.replace(" ", "_")
    ingredient_name_measuredfood.replace("__", "")
    ingredient_name_measuredfood.replace("___", "")
    ingredient_name_measuredfood.replace("____", "")
    ingredient_name_measuredfood.replace("_____", "")
    ingredient_name_measuredfood.replace("______", "")
    ingredient_name_measuredfood.replace("_______", "")

    return ingredient_name_measuredfood
