

def calculate_fulldayofeating(
    copy,
    all_nutrients_and_default_units,
    np,
    calculate_average_of_specificingredient_group,
    undo_calculate_average_of_specificingredient_group,
    specificingredient_dict_list,
    targeted_nutrients,
    set_to_zero_if_none,
    number_targeted_nutrients_not_equal_number_scaling_entities_error,
    calculation_result_is_negative_error,
    fixed_ingredient_exceeds_nutrient_profile_value_error,
):

    """
    This function should be independent of everything else.
    It should be a PURE function, i.e. work solely with inputs and outputs.

    Calculate the fulldayofeating, i.e. calculate the calculated_amount
    values for the SpecificIngredient instances associated with a
    FullDayOfEating, which is associated with a NutrientProfile.
    """

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
                    #   to the user. (Not yet relevant as the units can not
                    #   be chosen.) Once the units can be chosen this still
                    #   won't be a problem because then unit conversion
                    #   calculations will be implemented.
                    print(
                        '\nERROR: All specific ingredients belonging to the'
                        ' same group must have the same units.\n')
                    return None
            # If the group does not exist in
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

    list_averaged_specificingredients = \
        calculate_average_of_specificingredient_group(
            all_nutrients_and_default_units,
            specificingredient_scalingoption_group_dict,
            copy,
        )

    # group the averaged SpecificIngredients together with the
    # SpecificIngredients whose scaling_option was set to independent.
    list_independently_scaling_entities = []
    list_independently_scaling_entities.extend(
        specificingredient_scalingoption_independent
        )
    list_independently_scaling_entities.extend(
        list_averaged_specificingredients
        )

    fulldayofeating_nutrition_so_far = {}
    for nutrient_dict in all_nutrients_and_default_units:
        nutrient_field_name = nutrient_dict['nutrient_name_measuredfood']
        fulldayofeating_nutrition_so_far.update(
            {nutrient_field_name: 0}
        )

    for dict_k in specificingredient_scalingoption_fixed:
        for nutrient_dict in all_nutrients_and_default_units:
            nutrient_field_name = nutrient_dict['nutrient_name_measuredfood']
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
            raise fixed_ingredient_exceeds_nutrient_profile_value_error

    # Prepare the arrays for the linear equation solver.
    b = []
    for key_k in targeted_nutrients_remainder:
        b.append(targeted_nutrients_remainder[key_k])
    b = np.asarray(b)

    # Check for the error that the number of nutrient targets does not match
    # the number of independently scaling entities.
    if len(b) != len(list_independently_scaling_entities):

        list_independently_scaling_entity = []
        for dict_k in list_independently_scaling_entities:
            name_independtly_scaling_entity = \
                dict_k['raw_ingredient']['name']
            list_independently_scaling_entity.append(
                name_independtly_scaling_entity
            )

        n_independently_scaling_entity = \
            len(list_independently_scaling_entity)

        list_targeted_nutrient = []
        for key_k in targeted_nutrients_remainder:
            list_targeted_nutrient.append(key_k)

        n_targeted_nutrient = len(list_targeted_nutrient)
        
        raise number_targeted_nutrients_not_equal_number_scaling_entities_error(
            n_targeted_nutrient,
            list_targeted_nutrient,
            n_independently_scaling_entity,
            list_independently_scaling_entity,
        )

    else:
        a = np.zeros(shape=(len(b), len(b)))
        column_index = 0
        for dict_k in list_independently_scaling_entities:
            row_index = 0
            for key_k in targeted_nutrients_remainder:
                a[row_index][column_index] = dict_k['raw_ingredient'][key_k]
                row_index = row_index + 1
            column_index = column_index + 1

        # Solve the linear equation.
        
        # New procedure. Make sure, that if the code gets to this point, 
        # the linear equation system is solvable. Just try to calculate it. 
        # The possible failure causes Sandor could think of have been caught,
        # i.e. the number of targeted nutrients is not equal to the number of
        # independently scaling ingredients or ingredient groups.

        x = np.linalg.solve(a, b)

    # Multiply the entries in x with the reference_amount of each
    # SpecificIngredient
    solution = np.zeros(len(x))

    list_ingredient_negative_result = []

    for k in range(len(x)):
        # Calculate solution
        solution[k] = x[k] * list_independently_scaling_entities[k][
            'raw_ingredient']['reference_amount']

        # If any of the solutions are negative, the whole calculation is not
        # useful to the user. The user will be shown an explanatory error
        # page.
        if solution[k] < 0:
            list_ingredient_negative_result.append(
                list_independently_scaling_entities[k][
                    'raw_ingredient']['name']
            )

    if len(list_ingredient_negative_result) > 0:
        raise(calculation_result_is_negative_error(
            list_ingredient_negative_result
        ))

    # Assign the solution to the respective dictionary.
    for k in range(len(solution)):
        list_independently_scaling_entities[k]['calculated_amount'] = \
            solution[k]

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

    # unaverage the averaged_specificingredient instances
    specificingredient_scalingoption_group_dict_with_results =\
        undo_calculate_average_of_specificingredient_group(
            specificingredient_scalingoption_group_dict,
            calculated_amount_and_group_name
        )

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

    # Reorder the result so the order of the ingredients in the
    # calculation results html page is the same as the order of the
    # ingredients in the full day of eating update form page.
    specificingredient_id_and_calculated_amount_reordered = []
    for k in range(len(specificingredient_dict_list)):
        specificingredient_id = specificingredient_dict_list[k]['id']
        find_dict_in_calculated_results = \
            next(item for item in
                 specificingredient_id_and_calculated_amount
                 if item["id"] == specificingredient_id)
        specificingredient_id_and_calculated_amount_reordered.append(
            find_dict_in_calculated_results
        )

    return specificingredient_id_and_calculated_amount_reordered
