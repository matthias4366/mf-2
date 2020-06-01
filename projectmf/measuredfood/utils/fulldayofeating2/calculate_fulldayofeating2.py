

def calculate_fulldayofeating2(
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
):
    """
    :return:
    """

    # TODO: Put the while loop here. Keep calculating the fulldayofeating and
    #  adapting the specificingredient2_dict_list until the calculations
    #  yield an acceptable result. Set a max number of tries (100) to avoid a
    #  runaway loop.

    list_independently_scaling_entities,\
        specificingredient2_list_fixed, \
        specificingredient_scalingoption_group_dict\
        = \
        make_list_variable_ingredient_and_group(
            specificingredient2_dict_list,
            calculate_average_of_specificingredient2_group,
            all_nutrients_and_default_units,
            copy,
        )

    # Make a calculation attempt. Put it into a function. Have it return an
    # updated specificingredient2_dict_list.

    specificingredient2_dict_list = \
        calculate_specificingredient2_amount_try(
            all_nutrients_and_default_units,
            set_to_zero_if_none,
            specificingredient2_list_fixed,
            specificingredient2_dict_list,
            nutrientprofile_dict,
            copy,
            np,
            list_independently_scaling_entities,
            number_targeted_nutrients_not_equal_number_scaling_entities_error,
            undo_calculate_average_of_specificingredient_group,
            specificingredient_scalingoption_group_dict,
            make_specificingredient2_id_and_calculated_amount_dict,
        )



    return specificingredient2_dict_list
