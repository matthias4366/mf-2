

def calculate_percent_max_fulldayofeating(
    nutrientprofile_dict,
    result_total_nutrition_fulldayofeating,
):
    """
    It is preconditioned that a full day of eating has been calculated and its
    total nutrition content has been calculated. The ratio of the nutrient
    content in the full day of eating to the maximum amounts of the nutrient
    given in the nutrient profile is calculated and expressed as a percentag.
    The goal is to be below 100 percent in order to avoid nutrient overdoses.
    """

    # New, more logical return value.
    result_percent_max_dict = {}
    # Legacy return value. It was used so the previous code could be reused 
    # without changes.
    result_percentage_of_tolerable_upper_intake_str_list = []
    # Legacy return value.
    result_percentage_of_tolerable_upper_intake_numbers_list = []

    for key, value in result_total_nutrition_fulldayofeating.items():
        key_max_amount = 'max_' + key
        max_amount = nutrientprofile_dict[key_max_amount]
        if max_amount is not None and (max_amount > 0):
            percent_max = (value / max_amount) * 100
            percent_max = round(percent_max, 0)
            new_dict = {key: percent_max}
            result_percent_max_dict.update(new_dict)
            result_percentage_of_tolerable_upper_intake_str_list.append(
                str(percent_max)+' %'
            )
            result_percentage_of_tolerable_upper_intake_numbers_list.append(
                percent_max
            )
        else:
            new_dict = {key: None}
            result_percent_max_dict.update(new_dict)
            result_percentage_of_tolerable_upper_intake_str_list.append(
                str('')
            )
            result_percentage_of_tolerable_upper_intake_numbers_list.append(
                None
            )

    return \
        result_percent_max_dict, \
        result_percentage_of_tolerable_upper_intake_str_list, \
        result_percentage_of_tolerable_upper_intake_numbers_list
