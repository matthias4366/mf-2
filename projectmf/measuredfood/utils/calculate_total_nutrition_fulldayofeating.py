def calculate_total_nutrition_fulldayofeating(
    id_fulldayofeating,
    ALL_NUTRIENTS_AND_DEFAULT_UNITS,
    pprint,
    copy,
    SpecificIngredient,
    RawIngredient2,
):
    """
    Below the calculation results of a full day of eating, the total nutrition
    contained in that full day of eating is to be displayed.
    This function is predicated on the assumption that the calculated_amount
    values have already been calculated.
    """

    # Initialize the dictionary which will store the results
    result_total_nutrition_fulldayofeating = {}
    for dict_k in ALL_NUTRIENTS_AND_DEFAULT_UNITS:
        nutrient_name = dict_k['name']
        new_dict = {nutrient_name: 0}
        result_total_nutrition_fulldayofeating.update(
            new_dict
        )

    # Go through all the SpecificIngredients related to the FullDayOfEating.
    # For each SpecificIngredient, calculate its Nutrition by
    # multiplying the calculated_amount divided by the reference amount
    # multiplied by each nutrient value in the associated RawIngredient.

    # Get a list of all the SpecificIngredients associated to a FullDayOfEating.

    queryset_specificingredient_1 = SpecificIngredient.objects.filter(
        fulldayofeating_id=id_fulldayofeating
        )
    specificingredient_dict_list_1 = list(
        queryset_specificingredient_1.values()
        )

    # print('\n specificingredient_dict_list_1 \n')
    # pprint.pprint(specificingredient_dict_list_1)

    # Add the RawIngredient2 dictionaries to the SpecificIngredient dictionaries
    # to make the nutrition values (kcal etc.) accessible for calculation.
    for k in range(len(specificingredient_dict_list_1)):
        rawingredient_k_queryset = RawIngredient2.objects.filter(
            id = specificingredient_dict_list_1[k]['rawingredient_id']
        ).values()
        rawingredient_k_dict = list(rawingredient_k_queryset)[0]
        specificingredient_dict_list_1[k].update(
            raw_ingredient = rawingredient_k_dict
            )

    # print('\n specificingredient_dict_list_1 \n')
    # pprint.pprint(specificingredient_dict_list_1)

    # Sum up the total nutrition
    for k in range(len(specificingredient_dict_list_1)):
        # For each nutrient, calculate the amount of that nutrient contained
        # in the calculated_amount of the SpecificIngredient
        for dict_k in ALL_NUTRIENTS_AND_DEFAULT_UNITS:
            nutrient_name = dict_k['name']
            result_total_nutrition_fulldayofeating[nutrient_name] = \
            result_total_nutrition_fulldayofeating[nutrient_name] \
            + set_to_zero_if_none(specificingredient_dict_list_1[k]['raw_ingredient'][nutrient_name]) \
            * specificingredient_dict_list_1[k]['calculated_amount']\
            / specificingredient_dict_list_1[k]['raw_ingredient']\
            ['reference_amount']

    # Round the values in the result_total_nutrition_fulldayofeating
    # Initialize the dictionary containing the rounded values.
    result_total_nutrition_fulldayofeating_rounded = {}
    for dict_k in ALL_NUTRIENTS_AND_DEFAULT_UNITS:
        nutrient_name = dict_k['name']
        new_dict = {nutrient_name: 0}
        result_total_nutrition_fulldayofeating_rounded.update(
            new_dict
        )

    # Round the values and save them to the respective dictionary.
    for dict_k in ALL_NUTRIENTS_AND_DEFAULT_UNITS:
        nutrient_name = dict_k['name']
        result_total_nutrition_fulldayofeating_rounded[nutrient_name] = \
        round(result_total_nutrition_fulldayofeating[nutrient_name],1)

    return result_total_nutrition_fulldayofeating_rounded

def set_to_zero_if_none(input):
    if input is None:
        return 0
    else:
        return input
