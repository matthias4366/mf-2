def determine_missing_nutrition_data_fulldayofeating(
    specificingredient_dict_list,
    nutrient_name_list,
):

    """
    This function is not used and has been shelved. It would make the user
    experience worse. I will keep it for a later date.
    """

    is_nutrition_data_fulldayofeating_missing = []

    # Go through each nutrient.
    for nutrient_name in nutrient_name_list:

        is_missing_k = False

        for specificingredient_dict in specificingredient_dict_list:
            if specificingredient_dict['raw_ingredient'][nutrient_name] is None:
                is_missing_k = True
            else:
                pass

        is_nutrition_data_fulldayofeating_missing.append(is_missing_k)

    return is_nutrition_data_fulldayofeating_missing
