

def calculate_fulldayofeating(
    pprint,
    copy,
    all_nutrients_and_default_units,
    np,
    calculate_average_of_specificingredient_group,
    undo_calculate_average_of_specificingredient_group,
    specificingredient_dict_list,
    targeted_nutrients,
    set_to_zero_if_none,
):

    """
    This function should be independent of everything else.
    It should be a PURE function, i.e. work solely with inputs and outputs.

    Calculate the fulldayofeating, i.e. calculate the calculated_amount
    values for the SpecificIngredient instances associated with a
    FullDayOfEating, which is associated with a NutrientProfile.
    """

    result_calculate_fulldayofeating = {
        'values': {},
        'errors': {
            # If there was a critical error in the linear matrix equation
            # solver, set this variable to True.
            'solver_failed': False,
            # If the inputs are set up badly, it is possible to get negative
            # results for the calculated amount values. For example,
            # if the targets are 10000 kcal and 23 g of protein and the
            # ingredients are beans and pea protein powder. Covering the
            # calories with the beans already surpases the protein goal.
            # Hence, to make the numbers add up, the solution for the
            # amount of pea protein will be negative.
            'negative_result': False,

            # For the linear equation system to be solvable, the number of
            # independently scaling entities (i.e. independently scaling
            # ingredients or groups)
            # has to equal the number of nutrient targets (e.g. calories,
            # protein).
            'mismatch': False,
            # Show the user both the independently scaling entities and the
            # nutrient targets so they can understand where they went wrong.
            'list_names_independently_scaling_entities': None,
            'list_nutrient_targets': None,
            'n_independently_scaling_entities': None,
            'n_nutrient_targets': None,

            # The user can choose to target a nutrient for which there is no
            # value in the nutrient profile.
            'missing_nutrientprofile_value': False,
        },

    }

    # TODO: Currently, I am rounding to 2 decimal numbers.
    #   Maybe find a way to adapt the rounding to how many decimals the user
    #   input had.
    for k in range(len(specificingredient_dict_list)):

        specificingredient_dict_list[k].update(
            n_decimals_to_round_to=2
            )

        # Convert base_amount from decimal to float so it can be used for
        # calculations.
        specificingredient_dict_list[k]['base_amount'] = \
            float(specificingredient_dict_list[k]['base_amount'])

    # print('\n specificingredient_dict_list \n')
    # pprint.pprint(specificingredient_dict_list)

    """
    Iterate through the dictionaries representing the SpecificIngredients
    and sort them by their 'scaling_option' property.
    """
    specificingredient_scalingoption_fixed = []
    specificingredient_scalingoption_independent = []

    # Create a dictionary where the keys are the group names and the fields
    # are lists of SpecificIngredients as dictionaries belonging to that group.
    specificingredient_scalingoption_group_dict = {}

    for dict_k in specificingredient_dict_list:
        if dict_k['scaling_option'] == 'FIXED':
            specificingredient_scalingoption_fixed.append(dict_k)
        elif dict_k['scaling_option'] == 'INDEPENDENT':
            specificingredient_scalingoption_independent.append(dict_k)
        elif len(dict_k['scaling_option']) == 1:
            # If the group already exists in
            # specificingredient_scalingoption_group_dict, add dict_k to it.
            if dict_k['scaling_option']\
                    in specificingredient_scalingoption_group_dict:
                # Check that the new SpecificIngredient has the same units as
                # the first SpecificIngredient in the group.
                if dict_k['base_amount_unit'] == \
                    specificingredient_scalingoption_group_dict[
                                    dict_k['scaling_option']
                                    ][0]['base_amount_unit']:
                    specificingredient_scalingoption_group_dict[
                        dict_k['scaling_option']
                        ].append(dict_k)
                else:
                    # TODO: Make this into a proper error message and show it
                    # to the user.
                    print(
                        '\nERROR: All specific ingredients belonging to the'
                        ' same group must have the same units.\n')
                    return None
            # If the group does not exist
            # specificingredient_scalingoption_group_dict, create it an add
            # dict_k to it.
            else:
                specificingredient_scalingoption_group_dict.update(
                    {dict_k['scaling_option']: [dict_k]}
                    )
        else:
            # This case is impossible, since the user is only presented
            # with valid selections for the scaling_option. It's still good
            # practice to have this piece of code.
            print('\nERROR. The value given for scaling_group option was'
                  ' not valid.\n')
            return None

    # print('\n specificingredient_scalingoption_fixed')
    # pprint.pprint(specificingredient_scalingoption_fixed)
    # print('\n specificingredient_scalingoption_independent')
    # pprint.pprint(specificingredient_scalingoption_independent)
    # print('\n specificingredient_scalingoption_group_dict')
    # pprint.pprint(specificingredient_scalingoption_group_dict)

    list_averaged_specificingredients = \
        calculate_average_of_specificingredient_group(
            all_nutrients_and_default_units,
            specificingredient_scalingoption_group_dict,
            copy,
        )
    # print('\n list_averaged_specificingredients \n')
    # pprint.pprint(list_averaged_specificingredients)

    # group the averaged SpecificIngredients together with the
    # SpecificIngredients whose scaling_option was set to independent.
    list_independently_scaling_entities = []
    list_independently_scaling_entities.extend(
        specificingredient_scalingoption_independent
        )
    list_independently_scaling_entities.extend(
        list_averaged_specificingredients
        )
    # print('\n list_independently_scaling_entities \n')
    # pprint.pprint(list_independently_scaling_entities)

    fulldayofeating_nutrition_so_far = {}
    for nutrient_dict in all_nutrients_and_default_units:
        nutrient_field_name = nutrient_dict['name']
        fulldayofeating_nutrition_so_far.update(
            {nutrient_field_name: 0}
        )
    # print('\n fulldayofeating_nutrition_so_far \n')
    # pprint.pprint(fulldayofeating_nutrition_so_far)

    for dict_k in specificingredient_scalingoption_fixed:
        for nutrient_dict in all_nutrients_and_default_units:
            nutrient_field_name = nutrient_dict['name']
            if dict_k['raw_ingredient'][nutrient_field_name] is None:
                dict_k['raw_ingredient'][nutrient_field_name] = 0
            fulldayofeating_nutrition_so_far[nutrient_field_name] = \
                fulldayofeating_nutrition_so_far[nutrient_field_name]\
                + dict_k['base_amount'] \
                / dict_k['raw_ingredient']['reference_amount'] \
                * set_to_zero_if_none(
                    dict_k['raw_ingredient'][nutrient_field_name]
                )

    # For the targeted nutrients, calculate the remaining values.
    targeted_nutrients_remainder = copy.deepcopy(targeted_nutrients)
    for key_k in targeted_nutrients:
        targeted_nutrients_remainder[key_k] = \
            targeted_nutrients[key_k] \
            - fulldayofeating_nutrition_so_far[key_k]
        # Check if the 'FIXED' SpecificIngredients already run over the
        # nutrition goal.
        if targeted_nutrients_remainder[key_k] <= 0:
            print('ERROR: The ingredients with the \'FIXED\' scaling_options '
                  'already provide too much nutrition.')
            return None

    # print('\n targeted_nutrients_remainder in calculate_fulldayofeating \n')
    # pprint.pprint(targeted_nutrients_remainder)

    # Prepare the arrays for the linear equation solver.
    b = []
    for key_k in targeted_nutrients_remainder:
        b.append(targeted_nutrients_remainder[key_k])
    b = np.asarray(b)
    # print('\nb \n')
    # pprint.pprint(b)

    # Check for the error that the number of nutrient targets does not match
    # the number of independently scaling entities.
    if len(b) != len(list_independently_scaling_entities):
        result_calculate_fulldayofeating['errors']['mismatch'] = True
        print('Mismatch error in calculate_fulldayofeating.')
        x = np.zeros(len(list_independently_scaling_entities))

        # print('\n list_independently_scaling_entities \n')
        # pprint.pprint(list_independently_scaling_entities)
        # print('\n x \n')
        # pprint.pprint(x)

        list_names_independently_scaling_entities = []
        for dict_k in list_independently_scaling_entities:
            name_independtly_scaling_entity = \
                dict_k['raw_ingredient']['name']
            list_names_independently_scaling_entities.append(
                name_independtly_scaling_entity
            )
        result_calculate_fulldayofeating['errors'][
            'list_names_independently_scaling_entities'] = \
            list_names_independently_scaling_entities

        result_calculate_fulldayofeating['errors'][
            'n_independently_scaling_entities'] = \
            len(list_names_independently_scaling_entities)

        # print('\n list_names_independently_scaling_entities \n')
        # pprint.pprint(list_names_independently_scaling_entities)

        list_nutrient_targets = []
        for key_k in targeted_nutrients_remainder:
            list_nutrient_targets.append(key_k)
        result_calculate_fulldayofeating['errors'][
            'list_nutrient_targets'] = list_nutrient_targets

        result_calculate_fulldayofeating['errors'][
            'n_nutrient_targets'] = len(list_nutrient_targets)

        # print('\n list_nutrient_targets \n')
        # pprint.pprint(list_nutrient_targets)

    else:
        a = np.zeros(shape=(len(b), len(b)))
        column_index = 0
        for dict_k in list_independently_scaling_entities:
            row_index = 0
            for key_k in targeted_nutrients_remainder:
                a[row_index][column_index] = dict_k['raw_ingredient'][key_k]
                row_index = row_index + 1
            column_index = column_index + 1
        # print('\na \n')
        # pprint.pprint(a)

        # Solve the linear equation.
        # Catch the case that the linear equation system is not solvable, in
        # order to give the user a useful error page.
        # noinspection PyBroadException
        try:
            x = np.linalg.solve(a, b)
        except:
            result_calculate_fulldayofeating['errors']['solver_failed']\
                = True
            print('\n solver failed in calculate_fulldayofeating\n')
            return result_calculate_fulldayofeating
        # print('\nx \n')
        # pprint.pprint(x)

    # Multiply the entries in x with the reference_amount of each
    # SpecificIngredient
    solution = np.zeros(len(x))
    # print('\nsolution \n')
    # pprint.pprint(solution)

    for k in range(len(x)):
        # Calculate solution
        solution[k] = x[k] * list_independently_scaling_entities[k][
            'raw_ingredient']['reference_amount']

        # If any of the solutions are negative, the whole calculation is not
        # useful to the user. The user will be shown an explanatory error
        # page.
        if solution[k] < 0:
            result_calculate_fulldayofeating['errors']['negative_result']\
                = True

    # print('\n solution \n')
    # pprint.pprint(solution)

    # Assign the solution to the respective dictionary.
    for k in range(len(solution)):
        list_independently_scaling_entities[k]['calculated_amount'] = \
            solution[k]
    # print('\n list_independently_scaling_entities \n')
    # pprint.pprint(list_independently_scaling_entities)

    # Initialize the return value.
    specificingredient_id_and_calculated_amount = []

    # Assign the calculated_amount values to the return variable.

    # Assign the calculated_amount values from the SpecificIngredients
    # belonging to groups to the return variable.

    # From list_independently_scaling_entities, get all the
    # averaged_specificingredient instances.
    calculated_amount_and_group_name = {}
    for k in range(len(list_independently_scaling_entities)):
        if list_independently_scaling_entities[k]['raw_ingredient']['name']\
                .startswith('average_group_'):
            group_name = list_independently_scaling_entities[k]['group']
            calculated_amount = \
                list_independently_scaling_entities[k]['calculated_amount']
            total_base_amount = \
                list_independently_scaling_entities[k]['total_base_amount']
            new_dict = {
                group_name:
                {'calculated_amount': calculated_amount,
                 'total_base_amount': total_base_amount}
                                     }
            calculated_amount_and_group_name.update(new_dict)

    # print('\n calculated_amount_and_group_name \n')
    # pprint.pprint(calculated_amount_and_group_name)

    # unaverage the averaged_specificingredient instances
    specificingredient_scalingoption_group_dict_with_results =\
        undo_calculate_average_of_specificingredient_group(
            specificingredient_scalingoption_group_dict,
            calculated_amount_and_group_name
        )
    # print('\n specificingredient_scalingoption_group_dict_with_results \n')
    # pprint.pprint(specificingredient_scalingoption_group_dict_with_results)

    for group_name, specificingredient_list in \
            specificingredient_scalingoption_group_dict_with_results.items():
        for k in range(len(specificingredient_list)):
            id_result = specificingredient_list[k]['id']

            calculated_amount_result = round(
                specificingredient_list[k]['calculated_amount'],
                specificingredient_list[k]['n_decimals_to_round_to']
            )

            new_dict = {
                'id': id_result,
                'calculated_amount': calculated_amount_result
            }
            specificingredient_id_and_calculated_amount.append(new_dict)

    # Assign the calculated_amount values from the SpecificIngredients
    # with scaling_option == 'INDEPENDENT' to the return variable.
    for k in range(len(list_independently_scaling_entities)):
        # The averaged_specificingredient do not have a 'scaling_option' key.
        if 'scaling_option' in list_independently_scaling_entities[k].keys():
            if list_independently_scaling_entities[k]['scaling_option'] \
                    == 'INDEPENDENT':
                id_result = list_independently_scaling_entities[k]['id']

                # Round the calculated_amount_result before adding it to the
                # return dictionary.
                calculated_amount_result = round(
                    list_independently_scaling_entities[k]['calculated_amount'],
                    list_independently_scaling_entities[k]
                    ['n_decimals_to_round_to']
                )

                new_dict = {
                    'id': id_result,
                    'calculated_amount': calculated_amount_result
                }
                specificingredient_id_and_calculated_amount.append(new_dict)

    # Assign the calculated_amount values from the SpecificIngredients
    # with scaling_option == 'FIXED' to the return variable.

    for k in range(len(specificingredient_scalingoption_fixed)):
        id_result = specificingredient_scalingoption_fixed[k]['id']
        # For the SpecificIngredients with scaling_option = 'FIXED',
        # no calculations are done. Hence, the base_amounts are used.
        # Since the base amounts are used, rounding is not necessary.
        # TODO: This might be confusing.
        calculated_amount_result = \
            specificingredient_scalingoption_fixed[k]['base_amount']
        new_dict = {
            'id': id_result,
            'calculated_amount': calculated_amount_result
        }
        specificingredient_id_and_calculated_amount.append(new_dict)

    result_calculate_fulldayofeating['values'] = \
        copy.deepcopy(specificingredient_id_and_calculated_amount)

    # Make it a PURE function, i.e. return the values instead of directly
    # saving them to the database.

    # print('\n result_calculate_fulldayofeating[\'values\'] \n')
    # pprint.pprint(result_calculate_fulldayofeating['values'])

    return result_calculate_fulldayofeating
