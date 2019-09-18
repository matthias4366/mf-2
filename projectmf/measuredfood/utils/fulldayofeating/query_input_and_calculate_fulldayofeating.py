

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
    specific_ingredient,
    raw_ingredient2,
    full_day_of_eating,
    nutrient_profile,
    specific_nutrient_target,
    copy,
    all_nutrients_and_default_units,
    np,
    no_specific_ingredient_in_full_day_of_eating_error,
    no_value_for_targeted_nutrient_error,
    number_targeted_nutrients_not_equal_number_scaling_entities_error,
    calculation_result_is_negative_error,
):
    """
    This function groups together multiple sub functions that often need to be
    executed together in a specific order.
    """

    specificingredient_dict_list = query_ingredients_fulldayofeating(
        id_fulldayofeating,
        specific_ingredient,
        raw_ingredient2,
        all_nutrients_and_default_units,
        set_to_zero_if_none,
        no_specific_ingredient_in_full_day_of_eating_error,
    )

    nutrientprofile_dict = query_nutrientprofile_of_fulldayofeating(
        id_fulldayofeating,
        full_day_of_eating,
        nutrient_profile,
    )

    targeted_nutrients = \
        query_specificnutrienttarget_of_fulldayofeating(
            id_fulldayofeating,
            specific_nutrient_target,
            nutrientprofile_dict,
            no_value_for_targeted_nutrient_error,
        )

    specificingredient_id_and_calculated_amount = \
        calculate_fulldayofeating(
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
        )

    # Save the results to the database:
    save_fulldayofeating_calculation_result_to_database(
        specificingredient_id_and_calculated_amount,
        specific_ingredient
    )

    # Query the SpecificIngredient objects again in order to get them with
    # their calculated_amount values. After the first query, they did not
    # have them yet.
    specificingredient_dict_list = query_ingredients_fulldayofeating(
        id_fulldayofeating,
        specific_ingredient,
        raw_ingredient2,
        all_nutrients_and_default_units,
        set_to_zero_if_none,
        no_specific_ingredient_in_full_day_of_eating_error,
    )

    return specificingredient_id_and_calculated_amount,\
        specificingredient_dict_list,\
        nutrientprofile_dict
