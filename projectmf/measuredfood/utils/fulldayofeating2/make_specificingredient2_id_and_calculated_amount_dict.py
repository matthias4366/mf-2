

def make_specificingredient2_id_and_calculated_amount_dict(
    specificingredient_scalingoption_group_dict_with_results,
    list_independently_scaling_entities,
    specificingredient2_list_fixed,
):
    """
    The amounts of the SpecificIngredient2 objects inside the FullDayOfEating2
    have been calculated. The calculated_amount values along with the
    SpecificIngredient2 id are extracted and put into a new dictionary. The
    purpose is to extract the essential results and put them into a easy to
    handle dictionary.
    :param specificingredient_scalingoption_group_dict_with_results:
    :param list_independently_scaling_entities:
    :param specificingredient2_list_fixed:
    :return: specificingredient_id_and_calculated_amount
    """

    specificingredient_id_and_calculated_amount = []

    # Find the SpecificIngredient2 id's and the associated calculated amounts.
    for group_name, specificingredient_list in \
            specificingredient_scalingoption_group_dict_with_results.items():
        for k in range(len(specificingredient_list)):
            id_result = specificingredient_list[k]['id']

            calculated_amount_result = round(
                specificingredient_list[k]['calculated_amount'],
                specificingredient_list[k]['n_decimals_to_round_to']
            )

            new_dict = {
                'id_specificingredient2': id_result,
                'calculated_amount': calculated_amount_result
            }
            specificingredient_id_and_calculated_amount.append(new_dict)

    # Assign the calculated_amount values from the SpecificIngredient2
    # with amount_is_variable = True and no group to the return variable.
    for k in range(len(list_independently_scaling_entities)):
        if list_independently_scaling_entities[k]['group'] == 'no group':
            if list_independently_scaling_entities[k]['amount_is_variable']:

                id_result = list_independently_scaling_entities[k]['id']

                # Round the calculated_amount_result before adding it to the
                # return dictionary.
                calculated_amount_result = round(
                    list_independently_scaling_entities[k]['calculated_amount'],
                    list_independently_scaling_entities[k]
                    ['n_decimals_to_round_to']
                )

                new_dict = {
                    'id_specificingredient2': id_result,
                    'calculated_amount': calculated_amount_result
                }
                specificingredient_id_and_calculated_amount.append(new_dict)

    # Assign the calculated_amount values from the SpecificIngredient2
    # with amount_is_variable == False to the return variable.

    for k in range(len(specificingredient2_list_fixed)):
        id_result = specificingredient2_list_fixed[k]['id']
        # For the SpecificIngredients with amount_is_variable == False,
        # no calculations are done. Hence, the calculated_amount values are
        # equal to the base_amount values.
        # Since the base amounts are used, rounding is not necessary.
        calculated_amount_result = \
            specificingredient2_list_fixed[k]['base_amount']
        new_dict = {
            'id_specificingredient2': id_result,
            'calculated_amount': calculated_amount_result
        }
        specificingredient_id_and_calculated_amount.append(new_dict)

    return specificingredient_id_and_calculated_amount
