

def calculate_average_of_specificingredient_group(
    all_nutrients_and_default_units,
    specificingredient_scalingoption_group_dict,
    copy,
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
        for nutrient_dict in all_nutrients_and_default_units:
            field_name = nutrient_dict['nutrient_name_measuredfood']
            rawingredient_dict_initial.update(
                {field_name: 0}
            )
        rawingredient_dict_initial.update(
            {'reference_amount': 100}
        )
        averaged_specificingredient_initial = {}
        averaged_specificingredient_initial.update(
            {'raw_ingredient': rawingredient_dict_initial}
        )

        # Name the averaged ingredient using the group name.
        averaged_specificingredient = copy.deepcopy(
            averaged_specificingredient_initial
        )
        averaged_specificingredient['raw_ingredient']['name'] = \
            'average_group_' + key_k

        # Add a group property with the group name to have it easily on hand.
        averaged_specificingredient['group'] = key_k

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
        # Helper variable to calculate the average reference_amount.
        sum_reference_amount_g = 0
        for m in range(len(group_k)):
            sum_reference_amount_g = sum_reference_amount_g \
                + averaged_specificingredient[
                                         'raw_ingredient']['reference_amount']
            for nutrient_dict in all_nutrients_and_default_units:
                nutrient_field_name = \
                    nutrient_dict['nutrient_name_measuredfood']
                # Change field values to supported values, i.e. None to 0.
                if group_k[m]['raw_ingredient'][nutrient_field_name] is None:
                    group_k[m]['raw_ingredient'][nutrient_field_name] = 0
                averaged_specificingredient[
                    'raw_ingredient'][nutrient_field_name] = \
                    averaged_specificingredient['raw_ingredient'][
                    nutrient_field_name] \
                    + (group_k[m]['base_amount'] / total_base_amount) \
                    * group_k[m]['raw_ingredient'][nutrient_field_name]

        # Calculate the average reference_amount.
        averaged_specificingredient['raw_ingredient']['reference_amount'] = \
            sum_reference_amount_g / len(group_k)

        # Add all the averaged ingredients to a list.
        list_averaged_specificingredients.append(averaged_specificingredient)

    return list_averaged_specificingredients
