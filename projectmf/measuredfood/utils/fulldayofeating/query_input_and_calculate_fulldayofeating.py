

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
    pprint,
    full_day_of_eating,
    nutrient_profile,
    specific_nutrient_target,
    copy,
    all_nutrients_and_default_units,
    np,
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
    )

    # Catch the error that the user did not add any ingredients whatsoever.
    if len(specificingredient_dict_list) == 0:
        result_calculate_fulldayofeating = {
            'errors': {
                'ingredients_are_present': False
            }
        }
        specificingredient_dict_list = None
        targeted_nutrients_errors = None
        nutrientprofile_dict = None
        return result_calculate_fulldayofeating,\
            specificingredient_dict_list,\
            targeted_nutrients_errors,\
            nutrientprofile_dict

    nutrientprofile_dict = query_nutrientprofile_of_fulldayofeating(
        id_fulldayofeating,
        full_day_of_eating,
        nutrient_profile,
    )

    targeted_nutrients, targeted_nutrients_errors = \
        query_specificnutrienttarget_of_fulldayofeating(
            id_fulldayofeating,
            specific_nutrient_target,
            nutrientprofile_dict,
        )

    # If there is an error in the form of missing nutrient targets in the
    # NutrientProfile, then the rest of the function does not need to be
    # executed because an error message will be shown instead of calculated
    # amounts.
    if targeted_nutrients_errors['missing_nutrientprofile_value']:
        # Set the variables that would be calculated if there was no error to
        # None so that the interpreter does not complain about unknown
        # variable names.
        result_calculate_fulldayofeating = None
        specificingredient_dict_list = None
        return result_calculate_fulldayofeating,\
            specificingredient_dict_list,\
            targeted_nutrients_errors,\
            nutrientprofile_dict

    result_calculate_fulldayofeating = \
        calculate_fulldayofeating(
            pprint,
            copy,
            all_nutrients_and_default_units,
            np,
            calculate_average_of_specificingredient_group,
            undo_calculate_average_of_specificingredient_group,
            specificingredient_dict_list,
            targeted_nutrients,
            set_to_zero_if_none,
        )

    specificingredient_id_and_calculated_amount = \
        copy.deepcopy(result_calculate_fulldayofeating['values'])

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
    )

    return result_calculate_fulldayofeating,\
        specificingredient_dict_list,\
        targeted_nutrients_errors,\
        nutrientprofile_dict
