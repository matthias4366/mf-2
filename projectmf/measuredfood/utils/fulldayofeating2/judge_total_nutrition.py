

def judge_total_nutrition(
    result_percentage_of_target_amount_numbers_list,
    result_percentage_of_tolerable_upper_intake_numbers_list,
    set_to_zero_if_none,
):

    result_judge_total_nutrition = []

    right_amount_str = 'good'
    too_much_str = 'too much'
    too_little_str = 'too little'
    error_message = 'Error: % target <= % max.'

    # Check if the total amount for a nutrient is greater than the target
    # amount.
    # If it is, it is either the right amount or too much.
    # If it is not, it is too little.

    # If the total amount for a nutrient is greater than the target amount,
    # then check if the total amount for a nutrient is greater than the
    # tolerable upper intake.
    # If it is, it is too much.
    # If it is not, it is the right amount.

    # Iterate over the each nutrient in the list.
    for k in range(len(result_percentage_of_target_amount_numbers_list)):

        # New code:
        # Catch the error that the nutrient target is greater than the
        # maximum amount.
        # If the target amount is greater in absolute terms, the percentage
        # of the target amount is smaller than the percentage of the maximum
        # amount.
        percent_of_target = \
            result_percentage_of_target_amount_numbers_list[k]

        percent_of_maximum = \
            result_percentage_of_tolerable_upper_intake_numbers_list[k]

        if percent_of_target is not None and percent_of_maximum is not None:

            target_is_greater_or_equal_than_maximum = \
                set_to_zero_if_none(percent_of_target) \
                <= set_to_zero_if_none(percent_of_maximum)
            if target_is_greater_or_equal_than_maximum:
                result_judge_total_nutrition.append(error_message)
                continue

        # Check if the amount is too little.
        if percent_of_target is not None:
            if percent_of_target < 100:
                result_judge_total_nutrition.append(too_little_str)
                continue

        # Check if the amount is too much.
        if percent_of_maximum is not None:
            if percent_of_maximum > 100:
                result_judge_total_nutrition.append(too_much_str)
                continue

        # If no errors have been triggered, default to the right amount.
        result_judge_total_nutrition.append(right_amount_str)

    # Based on the judgments, create css class names by replacing the spaces
    # underscores.
    result_judge_total_nutrition_css_class_name = []
    for str_k in result_judge_total_nutrition:
        str_css = str_k.replace(' ', '_')
        result_judge_total_nutrition_css_class_name.append(str_css)

    return result_judge_total_nutrition, \
        result_judge_total_nutrition_css_class_name
