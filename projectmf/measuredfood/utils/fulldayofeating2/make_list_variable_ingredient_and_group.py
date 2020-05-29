

def make_list_variable_ingredient_and_group(
    specificingredient2_dict_list,
    calculate_average_of_specificingredient2_group,
    all_nutrients_and_default_units,
    copy,
):
    """
    Make a list of all the indepedently scaling entities. The
    SpecificIngredient2 objects that do not belong to a group and are
    variable in their amount are part of this list. Additionally,
    the averaged ingredients representing ingredient groups are part of this
    list.
    :param specificingredient2_dict_list:
    :param calculate_average_of_specificingredient2_group:
    :param all_nutrients_and_default_units:
    :param copy:
    :return:
    """
    # Prepare the list of SpecificIngredient2 objects for calculation.
    # Select the SpecificIngredient2 objects that do not belong to a group
    # and are variable.

    specificingredient2_list_fixed = []
    specificingredient2_list_variable_no_group = []

    # Create a dictionary where the keys are the group names and the fields
    # are lists of SpecificIngredients as dictionaries belonging to that group.
    specificingredient_scalingoption_group_dict = {}

    for dict_k in specificingredient2_dict_list:
        if dict_k['amount_is_variable']:
            if dict_k['group'] == 'no group':
                specificingredient2_list_variable_no_group.append(dict_k)
            else:
                if dict_k['group'] \
                        in specificingredient_scalingoption_group_dict:
                    specificingredient_scalingoption_group_dict[
                        dict_k['group']
                        ].append(dict_k)
                # If the group does not exist inside
                # specificingredient_scalingoption_group_dict, create it an add
                # dict_k to it.
                else:
                    specificingredient_scalingoption_group_dict.update(
                        {dict_k['group']: [dict_k]}
                    )
        else:
            specificingredient2_list_fixed.append(dict_k)

    # From the SpecificIngredient2 objects belonging to groups and being
    # variable, make averages.

    specificingredient2_list_averaged = \
        calculate_average_of_specificingredient2_group(
            all_nutrients_and_default_units,
            specificingredient_scalingoption_group_dict,
            copy,
        )

    # Desired result:
    # Independently scaling entities.
    # a dict list of SpecificIngredient2 objects with the
    # proper associated nutrient contents (i.e. RawIngredient3 values).
    # group the averaged SpecificIngredients together with the
    list_independently_scaling_entities = []
    list_independently_scaling_entities.extend(
        specificingredient2_list_variable_no_group
        )
    list_independently_scaling_entities.extend(
        specificingredient2_list_averaged
        )

    return list_independently_scaling_entities,\
        specificingredient2_list_fixed

