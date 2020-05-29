

def query_input_and_calculate_fulldayofeating2(
    id_fulldayofeating2,
    specificingredient2,
    query_ingredients_fulldayofeating2,
    pprint,
    rawingredient3,
    all_nutrients_and_default_units,
    set_to_zero_if_none,
    fulldayofeating2,
    nutrientprofile,
    query_nutrientprofile_of_fulldayofeating2,
    calculate_fulldayofeating2,
    calculate_average_of_specificingredient2_group,
    copy,
):
    """

    :param id_fulldayofeating2:
    :param specificingredient2:
    :param query_ingredients_fulldayofeating2:
    :param pprint:
    :param rawingredient3:
    :param all_nutrients_and_default_units:
    :param set_to_zero_if_none:
    :param fulldayofeating2:
    :param nutrientprofile:
    :param query_nutrientprofile_of_fulldayofeating2:
    :param calculate_fulldayofeating2:
    :param calculate_average_of_specificingredient2_group:
    :param copy:
    :return:
    """
    # """
    #
    # :param id_fulldayofeating2: The primary key of the FullDayOfEating2
    # object that is to be calculated.
    # :return: Return the calculation results of the FullDayOfEating2 in a format
    # that can be given to the calculation result html template.
    # """
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

    nutrientprofile_dict = query_nutrientprofile_of_fulldayofeating2(
        id_fulldayofeating2,
        fulldayofeating2,
        nutrientprofile,
    )

    # print('nutrientprofile_dict')
    # pprint.pprint(nutrientprofile_dict)

    # NEXT: calculate full day of eating 2

    r_calculate_fulldayofeating2 = calculate_fulldayofeating2(
        specificingredient2_dict_list,
        calculate_average_of_specificingredient2_group,
        all_nutrients_and_default_units,
        copy,
    )

    print('r_calculate_fulldayofeating2')
    pprint.pprint(r_calculate_fulldayofeating2)

    return None