import pprint


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

    n_iterations_max = 100
    n = 1
    while n < n_iterations_max:

        n += 1

        # TODO: Before production, remove the print statements.
        print(f"Iteration number {n}")
        print('specificingredient2_dict_list')
        pprint.pprint(specificingredient2_dict_list)

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

        calculated_amount_fullfill_all_criteria = True

        # TODO: Check if a calculated amount is negative
        # adapt_specificingredient2_calculated_amount_negative_result()

        for specificingredient2_dict_k in specificingredient2_dict_list:
            if specificingredient2_dict_k['calculated_amount'] < 0:
                specificingredient2_dict_k['calculated_amount'] = 0
                specificingredient2_dict_k['amount_is_variable'] = False
                break
            break 

        # TODO: Check if a maximum amount has been exceeded
        # adapt_specificingredient2_calculated_amount_maximum()

        # TODO: Check if a minimum amount has been undercut
        # adapt_specificingredient2_calculated_amount_minimum()

        # TODO: Check if ingredients have step sizes.
        # adapt_specificingredient2_calculated_amount_step()

    return specificingredient2_dict_list
