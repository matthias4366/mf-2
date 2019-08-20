def judge_total_nutrition(
    result_percentage_of_target_amount_numbers_list,
    result_percentage_of_tolerable_upper_intake_numbers_list,
):

    result_judge_total_nutrition = []

    str_no_judgment = 'no judgment'

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
        (result_percentage_of_tolerable_upper_intake_numbers_list[k] == None):\
            result_judge_total_nutrition.append('')
        # There is only a tolerable upper intake.
        elif (result_percentage_of_target_amount_numbers_list[k] == None) and\
        (result_percentage_of_tolerable_upper_intake_numbers_list[k] != None):\
            pass
        # There is only a target.
        elif (result_percentage_of_target_amount_numbers_list[k] != None) and\
        (result_percentage_of_tolerable_upper_intake_numbers_list[k] == None):\
            pass
        # There are both a target and a tolerable upper intake.
        elif (result_percentage_of_target_amount_numbers_list[k] != None) and\
        (result_percentage_of_tolerable_upper_intake_numbers_list[k] != None):\
            pass




    return result_judge_total_nutrition
