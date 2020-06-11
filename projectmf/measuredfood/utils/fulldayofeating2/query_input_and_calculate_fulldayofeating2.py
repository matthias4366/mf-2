

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
    make_list_variable_ingredient_and_group,
    calculate_specificingredient2_amount_try,
    np,
    number_targeted_nutrients_not_equal_number_scaling_entities_error,
    undo_calculate_average_of_specificingredient_group,
    make_specificingredient2_id_and_calculated_amount_dict,
    save_fulldayofeating2_calculation_result_to_database,
    logger_fulldayofeating2,
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
    :param make_list_variable_ingredient_and_group:
    :param calculate_specificingredient2_amount_try:
    :param np:
    :param number_targeted_nutrients_not_equal_number_scaling_entities_error:
    :param undo_calculate_average_of_specificingredient_group:
    :param make_specificingredient2_id_and_calculated_amount_dict:
    :param save_fulldayofeating2_calculation_result_to_database:
    :param logger_fulldayofeating2:
    :return:
    """
    # """
    #
    # :param id_fulldayofeating2: The primary key of the FullDayOfEating2
    # object that is to be calculated.
    # :return: Return the calculation results of the FullDayOfEating2 in a
    # format
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

    logger_fulldayofeating2.info(
        'Inside query_input_and_calculate_fulldayofeating2'
    )

    logger_fulldayofeating2.debug('specificingredient2_dict_list')
    logger_fulldayofeating2.debug(specificingredient2_dict_list)

    nutrientprofile_dict = query_nutrientprofile_of_fulldayofeating2(
        id_fulldayofeating2,
        fulldayofeating2,
        nutrientprofile,
    )

    # print('nutrientprofile_dict')
    # pprint.pprint(nutrientprofile_dict)

    specificingredient2_dict_list = calculate_fulldayofeating2(
        specificingredient2_dict_list,
        calculate_average_of_specificingredient2_group,
        all_nutrients_and_default_units,
        copy,
        make_list_variable_ingredient_and_group,
        calculate_specificingredient2_amount_try,
        set_to_zero_if_none,
        nutrientprofile_dict,
        np,
        number_targeted_nutrients_not_equal_number_scaling_entities_error,
        undo_calculate_average_of_specificingredient_group,
        make_specificingredient2_id_and_calculated_amount_dict,
        logger_fulldayofeating2,
    )

    # print('r_calculate_fulldayofeating2')
    # pprint.pprint(r_calculate_fulldayofeating2)

    # Save the results to the database:
    save_fulldayofeating2_calculation_result_to_database(
        specificingredient2_dict_list,
        specificingredient2,
    )

    return specificingredient2_dict_list, nutrientprofile_dict
