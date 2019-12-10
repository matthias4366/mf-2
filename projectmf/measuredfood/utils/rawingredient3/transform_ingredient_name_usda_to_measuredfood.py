

def transform_ingredient_name_usda_to_measuredfood(
    nutrient_name_usda_api,
    id_nutrient_usda_api,
):
    """
    :param nutrient_name_usda_api: The name of nutrient as it was returned by
    the USDA API.
    :param id_nutrient_usda_api: The id of the nutrient as it was returned by
    the USDA API.
    :return:
    """

    if len(nutrient_name_usda_api) < 1:
        raise Exception()

    ingredient_name_measuredfood = \
        str(nutrient_name_usda_api) \
        + '-' \
        + 'name' \
        + '-' \
        + str(id_nutrient_usda_api) \
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
