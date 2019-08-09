def calculate_fulldayofeating(
    id_fulldayofeating,
    SpecificIngredient,
    FullDayOfEating,
    NutrientProfile,
    RawIngredient,
    pprint,
    copy,
    INGREDIENT_FIELDS_NUTRITION,
    np
    ):
    """
    This function should be independent of everything else.
    It should be a PURE function, i.e. work solely with inputs and outputs.
    It is given an id_fulldayofeating. Based on that, it retrieves the
    SpecificIngredients belonging to that FullDayOfEating and the
    NutrientProfile. It then calculates the final amounts and saves them to the
    fields "calculated_amount".

    Calculate the fulldayofeating, i.e. calculate the calculated_amount
    values for the SpecificIngredient instances associated with a
    FullDayOfEating, which is associated with a NutrientProfile.
    """

    """
    Query the related SpecificIngredients and store the results in dictionaries.
    """
    queryset_specificingredient_0 = SpecificIngredient.objects.filter(
        fulldayofeating_id=id_fulldayofeating
        )
    queryset_specificingredient_1 = SpecificIngredient.objects.filter(
        fulldayofeating_id=id_fulldayofeating
        )

    # 0 is not to be changed.
    specificingredient_dict_list_0 = list(
        queryset_specificingredient_0.values()
        )

    # 1 will be used for calculations, i.e. the fixed values will be removed.
    specificingredient_dict_list_1 = list(
        queryset_specificingredient_1.values()
        )

    # Add the RawIngredient dictionaries to the SpecificIngredient dictionaries
    # to make the nutrition values (kcal etc.) accessible for calculation.
    for k in range(len(specificingredient_dict_list_1)):
        rawingredient_k_queryset = RawIngredient.objects.filter(
            id = specificingredient_dict_list_1[k]['rawingredient_id']
        ).values()
        rawingredient_k_dict = list(rawingredient_k_queryset)[0]
        specificingredient_dict_list_1[k].update(
            raw_ingredient = rawingredient_k_dict
            )

    # print('\n specificingredient_dict_list_1 \n')
    # pprint.pprint(specificingredient_dict_list_1)

    # In the end, the calculated amounts are to be rounded. The number of
    # decimals to which to round is the number of decimals the user used for
    # the base amounts. Therefore, the number of decimals for the base amounts
    # are determined and stored in the dictionaries.
    # Convert the base_amount from DecimalField to float. But, before,
    # save the number of decimals based on the DecimalField.
    for k in range(len(specificingredient_dict_list_1)):
        base_amount_str = str(specificingredient_dict_list_1[k]['base_amount'])

        # TODO: This code is very unelegant. Rewrite it using regular
        # expressions.
        # The number of trailing zeros at the end of the base_amount. E.g.
        # 400.230000 has 4 trailing zeros. 2.000 has 3 trailing zeros.
        n_trailing_zeros = 0
        for l in reversed(range(len(base_amount_str))):
            if base_amount_str[l] == '0':
                n_trailing_zeros = n_trailing_zeros + 1
            else:
                break

        n_total_digits_after_decimal_point = 0
        for l in reversed(range(len(base_amount_str))):
            if base_amount_str[l] != '.':
                n_total_digits_after_decimal_point = \
                n_total_digits_after_decimal_point + 1
            else:
                break

        n_decimals_to_round_to = n_total_digits_after_decimal_point\
        - n_trailing_zeros

        specificingredient_dict_list_1[k].update(
            n_decimals_to_round_to = n_decimals_to_round_to
            )

        # Convert base_amount from decimal to float so it can be used for
        # calculations.
        specificingredient_dict_list_1[k]['base_amount'] = \
        float(specificingredient_dict_list_1[k]['base_amount'])

    # print('\n specificingredient_dict_list_1 \n')
    # pprint.pprint(specificingredient_dict_list_1)

    """
    Query the related NutrientProfile and store the results in dictionaries.
    """
    queryset_nutrientprofile_of_fulldayofeating = \
    FullDayOfEating.objects.filter(
        id=id_fulldayofeating
    ).values('nutrient_profile')
    nutrientprofile_id = \
    list(queryset_nutrientprofile_of_fulldayofeating)[0]['nutrient_profile']

    queryset_nutrientprofile_data = NutrientProfile.objects.filter(
        id = nutrientprofile_id
    )

    nutrientprofile_dict = list(queryset_nutrientprofile_data.values())[0]
    # print('\nnutrientprofile_dict \n')
    # pprint.pprint(nutrientprofile_dict)

    # Collect all the nutrition goals that are actually targeted.
    targeted_nutrients = {}
    for nutrient_field_name in INGREDIENT_FIELDS_NUTRITION:
        if nutrientprofile_dict[nutrient_field_name+'_is_targeted']:
            targeted_nutrients.update(
                {nutrient_field_name: nutrientprofile_dict[nutrient_field_name]}
            )
    # print('\ntargeted_nutrients \n')
    # pprint.pprint(targeted_nutrients)

    """
    Iterate through the dictionaries representing the SpecificIngredients
    and sort them by their 'scaling_option' property.
    """
    specificingredient_scalingoption_fixed = []
    specificingredient_scalingoption_independent = []

    # Create a dictionary where the keys are the group names and the fields
    # are lists of SpecificIngredients as dictionaries belonging to that group.
    specificingredient_scalingoption_group_dict = {}

    counter_added_to_existing_group = 0

    for dict_k in specificingredient_dict_list_1:
        if dict_k['scaling_option'] == 'FIXED':
            specificingredient_scalingoption_fixed.append(dict_k)
        elif dict_k['scaling_option'] == 'INDEPENDENT':
            specificingredient_scalingoption_independent.append(dict_k)
        elif len(dict_k['scaling_option']) == 1:
            # If the group already exists in
            # specificingredient_scalingoption_group_dict, add dict_k to it.
            if dict_k['scaling_option'] in specificingredient_scalingoption_group_dict:
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
                    print('\nERROR: All specific ingredients belonging to the'\
                           ' same group'\
                          ' must have the same units.\n')
                    return None
            # If the group does not exist
            # specificingredient_scalingoption_group_dict, create it an add
            # dict_k to it.
            else:
                specificingredient_scalingoption_group_dict.update(
                    {dict_k['scaling_option'] : [dict_k]}
                    )
        else:
            # This case is impossible, since the user is only presented
            # with valid selections for the scaling_option. It's still good
            # practice to have this piece of code.
            print('\nERROR. The value given for scaling_group option was' \
                  ' not valid.\n')
            return None

    # print('\n specificingredient_scalingoption_fixed')
    # pprint.pprint(specificingredient_scalingoption_fixed)
    # print('\n specificingredient_scalingoption_independent')
    # pprint.pprint(specificingredient_scalingoption_independent)
    # print('\n specificingredient_scalingoption_group_dict')
    # pprint.pprint(specificingredient_scalingoption_group_dict)

    list_averaged_specificingredients = calculate_average_of_specificingredient_group(
        INGREDIENT_FIELDS_NUTRITION,
        specificingredient_scalingoption_group_dict,
        copy,
        pprint,
        targeted_nutrients
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

    # Initialize fulldayofeating_nutrition_so_far
    fulldayofeating_nutrition_so_far = {}
    for nutrient_field_name in INGREDIENT_FIELDS_NUTRITION:
        fulldayofeating_nutrition_so_far.update(
            {nutrient_field_name: 0}
        )
    # print('\n fulldayofeating_nutrition_so_far \n')
    # pprint.pprint(fulldayofeating_nutrition_so_far)

    # Sum up the nutrition from the SpecificIngredients with the scaling_option
    # set to 'FIXED'.
    for dict_k in specificingredient_scalingoption_fixed:
         for nutrient_field_name in INGREDIENT_FIELDS_NUTRITION:
             if dict_k['raw_ingredient'][nutrient_field_name] == None:
                 dict_k['raw_ingredient'][nutrient_field_name] = \
                 0
             fulldayofeating_nutrition_so_far[nutrient_field_name]=\
             fulldayofeating_nutrition_so_far[nutrient_field_name]\
             + dict_k['base_amount'] \
             / dict_k['raw_ingredient']['reference_amount_g'] \
             * dict_k['raw_ingredient'][nutrient_field_name]
    # print('\n fulldayofeating_nutrition_so_far \n')
    # pprint.pprint(fulldayofeating_nutrition_so_far)

    # For the targeted nutrients, calculate the remaining values.
    targeted_nutrients_remainder = copy.deepcopy(targeted_nutrients)
    for key_k in targeted_nutrients:
        targeted_nutrients_remainder[key_k] = \
        targeted_nutrients[key_k] \
        - fulldayofeating_nutrition_so_far[key_k]
        # Check if the 'FIXED' SpecificIngredients already run over the
        # nutrition goal.
        if targeted_nutrients_remainder[key_k] <= 0:
            print('ERROR: The ingredients with the \'FIXED\' scaling_options '\
                  'already provide too much nutrition.')
            return None
    # print('\n targeted_nutrients_remainder \n')
    # pprint.pprint(targeted_nutrients_remainder)

    # Prepare the arrays for the linear equation solver.
    b = []
    for key_k in targeted_nutrients_remainder:
        b.append(targeted_nutrients_remainder[key_k])
    b = np.asarray(b)
    # print('\nb \n')
    # pprint.pprint(b)

    a = np.zeros(shape=(len(b),len(b)))
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
    x = np.linalg.solve(a, b)
    # print('\nx \n')
    # pprint.pprint(x)

    # Multiply the entries in x with the reference_amount_g of each
    # SpecificIngredient
    solution = np.zeros(len(x))
    # print('\nsolution \n')
    # pprint.pprint(solution)

    for k in range(len(x)):
        # Calculate solution
        solution[k] = x[k] * list_independently_scaling_entities\
        [k]['raw_ingredient']['reference_amount_g']
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
        new_dict = {}
        if list_independently_scaling_entities[k]['raw_ingredient']['name']\
        .startswith('average_group_'):
            group_name = list_independently_scaling_entities[k]['group']
            calculated_amount = \
            list_independently_scaling_entities[k]['calculated_amount']
            total_base_amount = \
            list_independently_scaling_entities[k]['total_base_amount']
            new_dict = {group_name:
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
        calculated_amount_and_group_name,
        pprint
    )
    # print('\n specificingredient_scalingoption_group_dict_with_results \n')
    # pprint.pprint(specificingredient_scalingoption_group_dict_with_results)

    for group_name, specificingredient_list in \
    specificingredient_scalingoption_group_dict_with_results.items():
        for k in range(len(specificingredient_list)):
            id_result = specificingredient_list[k]['id']

            # TODO: delete this old code.
            # calculated_amount_result = \
            # specificingredient_list[k]['calculated_amount']

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
                # TODO: remove trailing zeros when there are zero decimals.
                calculated_amount_result = round(
                    list_independently_scaling_entities[k]['calculated_amount'],
                    list_independently_scaling_entities[k]\
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


    # Make it a PURE function, i.e. return the values instead of directly
    # saving them to the database.
    return specificingredient_id_and_calculated_amount

def calculate_average_of_specificingredient_group(
    INGREDIENT_FIELDS_NUTRITION,
    specificingredient_scalingoption_group_dict,
    copy,
    pprint,
    targeted_nutrients
):
    """
    For each group of ingredients, create an average ingredient representing
    the group. Use the base_amounts to set the ratios.
    """

    # Add all the averaged ingredients to a list.
    list_averaged_specificingredients = []

    for key_k in specificingredient_scalingoption_group_dict:
        group_k = specificingredient_scalingoption_group_dict[key_k]

        # Initialize the averaged_specificingredient_initial intentionally
        # as opposed to starting with a copy of a SpecificIngredient. This way,
        # only the needed fields will be included.
        rawingredient_dict_initial = {}
        for field_name in INGREDIENT_FIELDS_NUTRITION:
            rawingredient_dict_initial.update(
                {field_name: 0}
            )
        rawingredient_dict_initial.update(
            {'reference_amount_g': 100}
        )
        # print('\n rawingredient_dict_initial \n')
        # pprint.pprint(rawingredient_dict_initial)
        averaged_specificingredient_initial = {}
        averaged_specificingredient_initial.update(
            {'raw_ingredient': rawingredient_dict_initial}
        )
        # print('\n averaged_specificingredient_initial \n')
        # pprint.pprint(averaged_specificingredient_initial)

        # Name the averaged ingredient using the group name.
        averaged_specificingredient = copy.deepcopy(averaged_specificingredient_initial)
        averaged_specificingredient['raw_ingredient']['name'] = \
        'average_group_' + key_k

        # Add a group property with the group name to have it easily on hand.
        averaged_specificingredient['group'] = key_k

        # print('\n averaged_specificingredient \n')
        # pprint.pprint(averaged_specificingredient)

        # Average the SpecificIngredients in group_k

        # Initialise the sum of the base_amounts
        total_base_amount = 0
        for m in range(len(group_k)):
            total_base_amount = total_base_amount + group_k[m]['base_amount']
        # Add the total base amount to the averaged_specificingredient
        # so it is available later when it is needed.
        averaged_specificingredient['total_base_amount'] = total_base_amount
        # print('\n type_total_base_amount \n')
        # print(type(total_base_amount))

        # Go through the SpecificIngredients belonging to a certain group
        # and add them to the averaged_specificingredient.
        # Helper variable to calculate the average reference_amount_g.
        sum_reference_amount_g = 0
        for m in range(len(group_k)):
            sum_reference_amount_g = sum_reference_amount_g \
            + averaged_specificingredient['raw_ingredient']['reference_amount_g']
            for nutrient_field_name in INGREDIENT_FIELDS_NUTRITION:
                # Change field values to supported values, i.e. None to 0.
                if group_k[m]['raw_ingredient'][nutrient_field_name] == None:
                    group_k[m]['raw_ingredient'][nutrient_field_name] = \
                    0
                averaged_specificingredient['raw_ingredient'][nutrient_field_name] = \
                averaged_specificingredient['raw_ingredient'][nutrient_field_name] \
                + (group_k[m]['base_amount'] / total_base_amount) \
                * group_k[m]['raw_ingredient'][nutrient_field_name]

        # Calculate the average reference_amount_g.
        averaged_specificingredient['raw_ingredient']['reference_amount_g'] = \
        sum_reference_amount_g / len(group_k)

        # Add all the averaged ingredients to a list.
        list_averaged_specificingredients.append(averaged_specificingredient)

    return list_averaged_specificingredients

def undo_calculate_average_of_specificingredient_group(
    specificingredient_scalingoption_group_dict,
    calculated_amount_and_group_name,
    pprint
):

    # print('\n specificingredient_scalingoption_group_dict \n')
    # pprint.pprint(specificingredient_scalingoption_group_dict)

    # print('\n calculated_amount_and_group_name \n')
    # pprint.pprint(calculated_amount_and_group_name)

    # """
    # Iterate over the groups: A, B, C etc.
    for group, list_specificingredients in \
    specificingredient_scalingoption_group_dict.items():
        # Iterate over all the SpecificIngredients belonging to the current
        # group.
        for k in range(len(specificingredient_scalingoption_group_dict[group])):
            # Based on the id of the current SpecificIngredient, get the
            # corresponding calculated_amount.

            # Assign the solution for the calculated_amount to the correct
            # dictionary.
            specificingredient_scalingoption_group_dict\
            [group][k]['calculated_amount'] =\
            calculated_amount_and_group_name[group]['calculated_amount'] *\
            specificingredient_scalingoption_group_dict\
            [group][k]['base_amount'] / \
            calculated_amount_and_group_name[group]['total_base_amount']

    # """


    return specificingredient_scalingoption_group_dict
