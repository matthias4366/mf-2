def judge_total_nutrition(
    result_percentage_of_target_amount_numbers_list,
    result_percentage_of_tolerable_upper_intake_numbers_list,
):

    result_judge_total_nutrition = []

    no_judgment_str = ''
    right_amount_str = 'good'
    too_much_str = 'too much'
    too_little_str = 'too little'

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

        # Catch the case of no value.
        if (result_percentage_of_target_amount_numbers_list[k] == None) and\
        (result_percentage_of_tolerable_upper_intake_numbers_list[k] == None):
            result_judge_total_nutrition.append(no_judgment_str)

        # There is only a tolerable upper intake.
        elif (result_percentage_of_target_amount_numbers_list[k] == None) and\
        (result_percentage_of_tolerable_upper_intake_numbers_list[k] != None):
            if result_percentage_of_tolerable_upper_intake_numbers_list[k] < 100:
                result_judge_total_nutrition.append(right_amount_str)
            elif result_percentage_of_tolerable_upper_intake_numbers_list[k] >= 100:
                result_judge_total_nutrition.append(too_much_str)
            else:
                print('Something went wrong, this case should not be possible.')

        # There is only a target.
        elif (result_percentage_of_target_amount_numbers_list[k] != None) and\
        (result_percentage_of_tolerable_upper_intake_numbers_list[k] == None):
            if result_percentage_of_target_amount_numbers_list[k] >= 100:
                result_judge_total_nutrition.append(right_amount_str)
            elif result_percentage_of_target_amount_numbers_list[k] < 100:
                result_judge_total_nutrition.append(too_little_str)
            else:
                print('Something went wrong, this case should not be possible.')

        # There are both a target and a tolerable upper intake.
        elif (result_percentage_of_target_amount_numbers_list[k] != None) and\
        (result_percentage_of_tolerable_upper_intake_numbers_list[k] != None):
            if result_percentage_of_target_amount_numbers_list[k] < 100:
                result_judge_total_nutrition.append(too_little_str)
            elif result_percentage_of_target_amount_numbers_list[k] >= 100:
                if result_percentage_of_tolerable_upper_intake_numbers_list[k] < 100:
                    result_judge_total_nutrition.append(right_amount_str)
                elif result_percentage_of_tolerable_upper_intake_numbers_list[k] >= 100:
                    result_judge_total_nutrition.append(too_much_str)
            else:
                print('Something went wrong, this case should not be possible.')

    return result_judge_total_nutrition
