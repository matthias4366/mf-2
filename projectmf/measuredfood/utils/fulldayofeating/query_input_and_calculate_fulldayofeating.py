def query_input_and_calculate_fulldayofeating(
    query_ingredients_fulldayofeating,
    query_nutrientprofile_of_fulldayofeating,
    query_specificnutrienttarget_of_fulldayofeating,
    calculate_fulldayofeating,
    calculate_average_of_specificingredient_group,
    undo_calculate_average_of_specificingredient_group,
    save_fulldayofeating_calculation_result_to_database,
    set_to_zero_if_none,
    id_fulldayofeating,
    SpecificIngredient,
    RawIngredient2,
    pprint,
    FullDayOfEating,
    NutrientProfile,
    SpecificNutrientTarget,
    copy,
    ALL_NUTRIENTS_AND_DEFAULT_UNITS,
    np,
):
    """
    This function groups together multiple sub functions that often need to be
    executed together in a specific order.
    """

    specificingredient_dict_list = query_ingredients_fulldayofeating(
        id_fulldayofeating,
        SpecificIngredient,
        RawIngredient2,
        pprint,
        ALL_NUTRIENTS_AND_DEFAULT_UNITS,
        set_to_zero_if_none,
    )

    nutrientprofile_dict = query_nutrientprofile_of_fulldayofeating(
        id_fulldayofeating,
        FullDayOfEating,
        NutrientProfile,
    )

    targeted_nutrients = query_specificnutrienttarget_of_fulldayofeating(
        id_fulldayofeating,
        SpecificNutrientTarget,
        nutrientprofile_dict,
        pprint,
    )

    result_calculate_fulldayofeating = \
    calculate_fulldayofeating(
        pprint,
        copy,
        ALL_NUTRIENTS_AND_DEFAULT_UNITS,
        np,
        calculate_average_of_specificingredient_group,
        undo_calculate_average_of_specificingredient_group,
        specificingredient_dict_list,
        nutrientprofile_dict,
        targeted_nutrients,
        set_to_zero_if_none,
        )

    # print('\n result_calculate_fulldayofeating in query_input_and_calculate_fulldayofeating \n')
    # pprint.pprint(result_calculate_fulldayofeating)

    specificingredient_id_and_calculated_amount = \
    copy.deepcopy(result_calculate_fulldayofeating['values'])

    # print('\n specificingredient_id_and_calculated_amount in query_input_and_calculate_fulldayofeating \n')
    # pprint.pprint(specificingredient_id_and_calculated_amount)

    # Save the results to the database:
    save_fulldayofeating_calculation_result_to_database(
        specificingredient_id_and_calculated_amount,
        SpecificIngredient
    )

    # Query the SpecificIngredient objects again in order to get them with
    # their calculated_amount values. After the first query, they did not
    # have them yet.
    specificingredient_dict_list = query_ingredients_fulldayofeating(
        id_fulldayofeating,
        SpecificIngredient,
        RawIngredient2,
        pprint,
        ALL_NUTRIENTS_AND_DEFAULT_UNITS,
        set_to_zero_if_none,
    )

    # print('\n specificingredient_dict_list in query_input_and_calculate_fulldayofeating \n')
    # pprint.pprint(specificingredient_dict_list)

    return result_calculate_fulldayofeating,\
    specificingredient_dict_list
