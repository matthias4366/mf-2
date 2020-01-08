

def match_nutrient_dri_to_measuredfood(
    match_nutrient_dri_to_measuredfood_dict,
    nutrient_name_dri,
    nutrient_amount_dri,
):
    """
    :param match_nutrient_dri_to_measuredfood_dict: Dictionary matching the
    nutrients obtained from the
    Dietary Reference Intake recommendations found in the
    daily_recommended_intake.xlsx file, source: https://ods.od.nih.gov/
    Health_Information/Dietary_Reference_Intakes.aspx
    to the names under which those nutrients are stored in the measuredfood
    database. Additionally, it contains a unit_conversion_factor to address
    differences in units between the DRI and the measuredfood database.
    :param nutrient_name_dri: Nutrient name as obtained from the Dietary
    Reference Intake recommendations found in the
    daily_recommended_intake.xlsx file, source: https://ods.od.nih.gov/
    Health_Information/Dietary_Reference_Intakes.aspx
    :param nutrient_amount_dri: The amount of the nutrient recommended in the
    Dietary Reference intake found in the
    daily_recommended_intake.xlsx file, source: https://ods.od.nih.gov/
    Health_Information/Dietary_Reference_Intakes.aspx
    :return: nutrient_amount_measuredfood: the nutrient_amount from the
    dietary reference intake, after having been transformed to match the
    units in the measuredfood database.
    nutrient_name_measuredfood: the name under which the nutrient is stored
    in the measured food database.
    """

    # Check if there is matching nutrient name in the measuredfood
    # application for the nutrient name given in the daily recommended intake
    # by the national institute of health.
    try:
        nutrient_name_measuredfood = \
            match_nutrient_dri_to_measuredfood_dict[
                nutrient_name_dri]['matching_name_in_measuredfood']
        if nutrient_name_measuredfood is None:
            return None, None
    except KeyError:
        print(f'KeyError has occured for '
              f'nutrient_name_dir {nutrient_name_dri}.')
        return None, None

    if len(nutrient_amount_dri) < 1:
        print(f'The nutrient_amount_dri string is empty for the nutrient with '
              f'nutrient_name_dri: {nutrient_name_dri}.')
        return None, nutrient_name_measuredfood

    try:

        unit_conversion_factor_ = float(
            match_nutrient_dri_to_measuredfood_dict[
                nutrient_name_dri]['unit_conversion_factor']
        )

    except KeyError:
        print(f'KeyError has occured while trying to find the \n'
              f'unit conversion factor\n'
              f' for '
              f'nutrient_name_dri {nutrient_name_dri}.')
        return None, nutrient_name_measuredfood

    nutrient_amount_dri_ = float(
        nutrient_amount_dri
    )

    nutrient_amount_measuredfood = \
        nutrient_amount_dri_ \
        * unit_conversion_factor_

    return nutrient_amount_measuredfood, nutrient_name_measuredfood


