

def make_number_from_national_institute_of_health_str(
    nutrient_amount_dri,
    re,
):
    """
    In the nutrition values from the national institute of health, there are
    bad characters such as "*" or letters. These need to be removed.

    :param nutrient_amount_dri:
    :param re:
    :return:
    """

    # Extract all the characters that are either numeric or the .
    # This supposes that there are not two dots.
    get_vals = list([val for val in nutrient_amount_dri
                    if val == '.' or val.isnumeric()])
    nutrient_amount_measuredfood = "".join(get_vals)

    return nutrient_amount_measuredfood
