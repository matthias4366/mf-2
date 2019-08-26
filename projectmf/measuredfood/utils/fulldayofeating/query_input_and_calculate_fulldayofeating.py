def query_input_and_calculate_fulldayofeating(
    query_ingredients_fulldayofeating,
    query_nutrientprofile_of_fulldayofeating,
    query_nutrienttargetselection_of_fulldayofeating,
    calculate_fulldayofeating,
    calculate_average_of_specificingredient_group,
    undo_calculate_average_of_specificingredient_group,
    id_fulldayofeating,
    SpecificIngredient,
    RawIngredient2,
    pprint,
    FullDayOfEating,
    NutrientProfile,
    NutrientTargetSelection,
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
    )

    nutrientprofile_dict = query_nutrientprofile_of_fulldayofeating(
        id_fulldayofeating,
        FullDayOfEating,
        NutrientProfile,
    )

    targeted_nutrients = query_nutrienttargetselection_of_fulldayofeating(
        id_fulldayofeating,
        FullDayOfEating,
        NutrientTargetSelection,
        nutrientprofile_dict,
    )

    result_calculate_fulldayofeating = \
    calculate_fulldayofeating(
        id_fulldayofeating,
        FullDayOfEating,
        NutrientProfile,
        NutrientTargetSelection,
        RawIngredient2,
        pprint,
        copy,
        ALL_NUTRIENTS_AND_DEFAULT_UNITS,
        np,
        calculate_average_of_specificingredient_group,
        undo_calculate_average_of_specificingredient_group,
        specificingredient_dict_list,
        nutrientprofile_dict,
        targeted_nutrients,
        )

    return result_calculate_fulldayofeating,\
    specificingredient_dict_list
