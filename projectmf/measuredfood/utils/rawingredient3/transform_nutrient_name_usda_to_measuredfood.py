

def transform_nutrient_name_usda_to_measuredfood(
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

    nutrient_name_measuredfood = \
        str(nutrient_name_usda_api) \
        + '-' \
        + 'name' \
        + '-' \
        + str(id_nutrient_usda_api) \
        + '-' \
        + 'id'

    nutrient_name_measuredfood.replace(" ", "_")
    nutrient_name_measuredfood.replace("__", "")
    nutrient_name_measuredfood.replace("___", "")
    nutrient_name_measuredfood.replace("____", "")
    nutrient_name_measuredfood.replace("_____", "")
    nutrient_name_measuredfood.replace("______", "")
    nutrient_name_measuredfood.replace("_______", "")

    return nutrient_name_measuredfood
