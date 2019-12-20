

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

    try:

        unit_conversion_factor_ = float(
            match_nutrient_dri_to_measuredfood_dict[
                nutrient_name_dri]['unit_conversion_factor']
        )

        # Catch the case that the DRI value might be not determined, and thus
        # marked as the string 'ND' or 'NDe' in the cell.
        if isinstance(nutrient_amount_dri, str):
            nutrient_amount_dri_ = 0
        else:
            nutrient_amount_dri_ = float(
                nutrient_amount_dri
            )

        nutrient_amount_measuredfood = \
            nutrient_amount_dri_ \
            * unit_conversion_factor_

        nutrient_name_measuredfood = \
            match_nutrient_dri_to_measuredfood_dict[
                nutrient_name_dri]['matching_name_in_measuredfood']

        return nutrient_amount_measuredfood, nutrient_name_measuredfood

    except KeyError:
        return None, None
