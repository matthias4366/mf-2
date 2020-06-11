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
    logging,
    no_value_for_targeted_nutrient_error,
):
    """
    :return:
    """

    logger_calculatefulldayofeating2 = logging.getLogger(__name__)
    logger_calculatefulldayofeating2.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

    file_handler = logging.FileHandler(
        'calculate_fulldayofeating2.log',
        mode='a'
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger_calculatefulldayofeating2.addHandler(file_handler)

    n_iterations_max = 100
    n = 1
    while n < n_iterations_max:

        # # TODO: Before production, remove the print statements.
        logger_calculatefulldayofeating2.debug('This will get logged')
        logger_calculatefulldayofeating2.debug(f"Iteration number {n}")
        # print('specificingredient2_dict_list')
        # pprint.pprint(specificingredient2_dict_list)

        n += 1

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

        logger_calculatefulldayofeating2.debug(
            'list_independently_scaling_entities'
        )
        logger_calculatefulldayofeating2.debug(
            pprint.pformat(
                list_independently_scaling_entities
            )
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
                no_value_for_targeted_nutrient_error,
            )

        # calculated_amount_fullfill_all_criteria is a variable to
        # determine if the calculated amounts are good as
        # they are or whether the FullDayOfEating2 has to be recalculated.
        calculated_amount_fullfill_all_criteria = True

        for specificingredient2_dict_k in specificingredient2_dict_list:
            if specificingredient2_dict_k['calculated_amount'] < 0:
                logger_calculatefulldayofeating2.debug(
                    f"Calculated amount smaller than 0 for ingredient "
                    f"{specificingredient2_dict_k['raw_ingredient']['name']}."
                    )
                calculated_amount_fullfill_all_criteria = False
                specificingredient2_dict_k['calculated_amount'] = 0
                specificingredient2_dict_k['base_amount'] = 0
                specificingredient2_dict_k['amount_is_variable'] = False
                specificingredient2_dict_k['nutrient_target'] = None
                continue

        if not calculated_amount_fullfill_all_criteria:
            continue

        for specificingredient2_dict_k in specificingredient2_dict_list:
            if specificingredient2_dict_k['max_amount'] is None:
                continue
            else:
                if specificingredient2_dict_k['calculated_amount'] > \
                        specificingredient2_dict_k['max_amount']:
                    # print('Calculated amount greater than maximum.')
                    calculated_amount_fullfill_all_criteria = False
                    specificingredient2_dict_k['calculated_amount'] = \
                        specificingredient2_dict_k['max_amount']
                    continue

        if not calculated_amount_fullfill_all_criteria:
            continue

        for specificingredient2_dict_k in specificingredient2_dict_list:
            if specificingredient2_dict_k['min_amount'] is None:
                continue
            else:
                if specificingredient2_dict_k['calculated_amount'] < \
                        specificingredient2_dict_k['min_amount']:
                    # print('Calculated amount less than minimum.')
                    calculated_amount_fullfill_all_criteria = False
                    specificingredient2_dict_k['calculated_amount'] = \
                        specificingredient2_dict_k['min_amount']
                    continue

        if not calculated_amount_fullfill_all_criteria:
            continue

        for specificingredient2_dict_k in specificingredient2_dict_list:

            if specificingredient2_dict_k['step_size'] is None:
                # print('No step size is defined, all good.')
                continue

            tolerance = 0.01
            remainder = \
                float(specificingredient2_dict_k['calculated_amount']) \
                % float(specificingredient2_dict_k['step_size'])
            # print('remainder')
            # print(remainder)
            relative_remainder = \
                remainder / \
                float(specificingredient2_dict_k['calculated_amount'])
            # print('relative_remainder')
            # print(relative_remainder)
            amount_is_multiple_of_step_size = \
                relative_remainder < tolerance

            if amount_is_multiple_of_step_size:
                # print('Calculated amount was multiple of step size.')
                continue

            if not amount_is_multiple_of_step_size:
                # print('Calculated amount was not multiple of step size.')
                calculated_amount_fullfill_all_criteria = False
                r_floor_division = \
                    specificingredient2_dict_k['calculated_amount'] \
                    // float(specificingredient2_dict_k['step_size'])
                # print('r_floor_division')
                # print(r_floor_division)
                difference_to_next_higher_step = \
                    abs(
                        (r_floor_division + 1)
                        * float(specificingredient2_dict_k['step_size'])
                        - specificingredient2_dict_k['calculated_amount']
                    )
                difference_to_next_lower_step = \
                    abs(
                        r_floor_division
                        * float(specificingredient2_dict_k['step_size'])
                        - specificingredient2_dict_k['calculated_amount']
                    )
                r_is_closer_to_next_higher_step = \
                    difference_to_next_higher_step \
                    < difference_to_next_lower_step

                calculated_amount_fit_to_higher_step = \
                    (r_floor_division + 1) \
                    * float(specificingredient2_dict_k['step_size'])
                calculated_amount_fit_to_lower_step = \
                    r_floor_division \
                    * float(specificingredient2_dict_k['step_size'])

                if r_is_closer_to_next_higher_step:
                    calculated_amount_fit_to_closest_step = \
                        calculated_amount_fit_to_higher_step
                else:
                    calculated_amount_fit_to_closest_step = \
                        calculated_amount_fit_to_lower_step

                if specificingredient2_dict_k['round_step'] == 'round down':
                    specificingredient2_dict_k['calculated_amount'] = \
                        calculated_amount_fit_to_lower_step
                elif specificingredient2_dict_k['round_step'] \
                        == 'closest value':
                    specificingredient2_dict_k['calculated_amount'] = \
                        calculated_amount_fit_to_closest_step
                elif specificingredient2_dict_k['round_step'] == 'round up':
                    specificingredient2_dict_k['calculated_amount'] = \
                        calculated_amount_fit_to_higher_step
                else:
                    # This case should not be possible
                    # print('Invalid round_step
                    # property on SpecificIngredient2.')
                    pass

                continue

        if not calculated_amount_fullfill_all_criteria:
            continue

        if calculated_amount_fullfill_all_criteria:
            break

    return specificingredient2_dict_list
