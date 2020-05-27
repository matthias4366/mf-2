

def query_input_and_calculate_fulldayofeating2(
    id_fulldayofeating2,
    specificingredient2,
    query_ingredients_fulldayofeating2,
    pprint,
    rawingredient3,
    all_nutrients_and_default_units,
    set_to_zero_if_none,
):
    """

    :param id_fulldayofeating2: The primary key of the FullDayOfEating2
    object that is to be calculated.
    :return: Return the calculation results of the FullDayOfEating2 in a format
    that can be given to the calculation result html template.
    """
    specificingredient2_dict_list = query_ingredients_fulldayofeating2(
        id_fulldayofeating2,
        specificingredient2,
        pprint,
        rawingredient3,
        all_nutrients_and_default_units,
        set_to_zero_if_none,
    )

    # print('specificingredient2_dict_list')
    # pprint.pprint(specificingredient2_dict_list)

    return None
