

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
):
    """
    :return:
    """

    list_independently_scaling_entities,\
        specificingredient2_list_fixed\
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
        )



    return list_independently_scaling_entities
