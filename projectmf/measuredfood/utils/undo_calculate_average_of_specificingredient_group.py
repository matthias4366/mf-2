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
