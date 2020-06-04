import pprint


def calculate_specificingredient2_amount_try(
    all_nutrients_and_default_units,
    set_to_zero_if_none,
    # in the old code, this is called specificingredient_scalingoption_fixed
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
):
    """
    Try to calculate the amounts of the SpecificIngredient2 objects. This
    function will be run multiple times.
    :return:
    """

    # Calculate the nutrition already present in the FullDayOfEating2 because
    # of the SpecificIngredient2 objects whose amounts are not variable.
    fulldayofeating_nutrition_so_far = {}
    for nutrient_dict in all_nutrients_and_default_units:
        nutrient_field_name = nutrient_dict['nutrient_name_measuredfood']
        fulldayofeating_nutrition_so_far.update(
            {nutrient_field_name: 0}
        )

    # print('specificingredient2_list_fixed')
    # pprint.pprint(specificingredient2_list_fixed)

    for dict_k in specificingredient2_list_fixed:
        for nutrient_dict in all_nutrients_and_default_units:
            nutrient_field_name = nutrient_dict['nutrient_name_measuredfood']
            if dict_k['raw_ingredient'][nutrient_field_name] is None:
                dict_k['raw_ingredient'][nutrient_field_name] = 0
            fulldayofeating_nutrition_so_far[nutrient_field_name] = \
                fulldayofeating_nutrition_so_far[nutrient_field_name]\
                + float(dict_k['base_amount']) \
                / float(dict_k['raw_ingredient']['reference_amount']) \
                * set_to_zero_if_none(
                    dict_k['raw_ingredient'][nutrient_field_name]
                )

    # print('fulldayofeating_nutrition_so_far')
    # pprint.pprint(fulldayofeating_nutrition_so_far)

    # Set up b for the linalg solver, i.e.

    # Rebuild the targeted_nutrients exactly as they were in the old code (
    # calculate_fulldayofeating). The coupling of ingredients to a nutrient
    # target is not relevant at this point. It is relevant later,
    # when SpecificIngredient2 objects are removed from the calculation,
    # and the nutrient target is removed with them.

    targeted_nutrients = {}

    for specificingredient2_k in specificingredient2_dict_list:
        if specificingredient2_k['nutrient_target'] is not None:
            if specificingredient2_k['nutrient_target'] not in \
                    targeted_nutrients:
                targeted_nutrient_daily_amount = \
                    nutrientprofile_dict[
                        specificingredient2_k['nutrient_target']
                    ]
                targeted_nutrients.update(
                    {
                        specificingredient2_k['nutrient_target']:
                        targeted_nutrient_daily_amount
                    }
                )

    # print('targeted_nutrients in 2')
    # print(targeted_nutrients)

    # calculate the remaining amounts that need to be filled for each
    # targeted nutrient.
    # E.g., the Energy (kcal) target is 2500 and the non
    # variable SpecificIngredient2 already provide 1000 kcal. There are
    # 1500 kcal remaining that need to be filled with the variable
    # SpecificIngredient2.

    # For the targeted nutrients, calculate the remaining values.
    targeted_nutrients_remainder = copy.deepcopy(targeted_nutrients)
    for key_k in targeted_nutrients:
        targeted_nutrients_remainder[key_k] = \
            targeted_nutrients[key_k] \
            - fulldayofeating_nutrition_so_far[key_k]
        # It's okay if some results are negative. Then, some ingredient
        # amounts will be negative later on. Then, the ingredient amount will
        # be set to zero and the SpecificIngredient2 will be set to
        # non-variable.

    # Prepare the arrays for the linear equation solver.
    b = []
    for key_k in targeted_nutrients_remainder:
        b.append(targeted_nutrients_remainder[key_k])
    b = np.asarray(b)

    print('b in 2')
    print(b)

    # The number of nutrient targets needs to be the same as the number of
    # independently scaling entities. Otherwise, the linear equation can not be
    # solved.

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

        x = np.linalg.solve(a, b)

    solution = np.zeros(len(x))
    for k in range(len(x)):
        # Calculate solution
        solution[k] = x[k] * list_independently_scaling_entities[k][
            'raw_ingredient']['reference_amount']

    # print('solution')
    # print(solution)

    # Assign the solution to the respective dictionary.
    for k in range(len(solution)):
        list_independently_scaling_entities[k]['calculated_amount'] = \
            solution[k]

    # print('list_independently_scaling_entities')
    # pprint.pprint(list_independently_scaling_entities)

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
    # print('specificingredient_scalingoption_group_dict_with_results')
    # pprint.pprint(specificingredient_scalingoption_group_dict_with_results)

    specificingredient_id_and_calculated_amount = \
        make_specificingredient2_id_and_calculated_amount_dict(
            specificingredient_scalingoption_group_dict_with_results,
            list_independently_scaling_entities,
            specificingredient2_list_fixed,
        )

    # print('specificingredient_id_and_calculated_amount')
    # pprint.pprint(specificingredient_id_and_calculated_amount)

    # Put the solution (i.e. the calculated amounts) into the
    # correct places in the specificingredient2_dict_list.

    for specificingredient2_k in specificingredient2_dict_list:
        id_specificingredient2_k = specificingredient2_k['id']
        # Find the associated calculation result:
        for r_k in specificingredient_id_and_calculated_amount:
            if r_k['id_specificingredient2'] == id_specificingredient2_k:
                specificingredient2_k['calculated_amount'] = \
                    copy.copy(r_k['calculated_amount'])
                continue

    # print('specificingredient2_dict_list')
    # pprint.pprint(specificingredient2_dict_list)

    return specificingredient2_dict_list
