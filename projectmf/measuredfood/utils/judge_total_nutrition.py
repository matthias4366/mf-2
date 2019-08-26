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
                print('\n Something went wrong, this case should not be possible.')
                print('Location in code: judge_total_nutrition loc 1. \n ')
                print('Faulty variable: ')
                print(' result_percentage_of_tolerable_upper_intake_numbers_list[k]')
                print(result_percentage_of_tolerable_upper_intake_numbers_list[k])
                print('\n')

        # There is only a target.
        elif (result_percentage_of_target_amount_numbers_list[k] != None) and\
        (result_percentage_of_tolerable_upper_intake_numbers_list[k] == None):
            if result_percentage_of_target_amount_numbers_list[k] >= 100:
                result_judge_total_nutrition.append(right_amount_str)
            elif result_percentage_of_target_amount_numbers_list[k] < 100:
                result_judge_total_nutrition.append(too_little_str)
            else:
                print('\n Something went wrong, this case should not be possible.')
                print('Location in code: judge_total_nutrition loc 2. \n ')
                print('Faulty variable: ')
                print(' result_percentage_of_target_amount_numbers_list[k]')
                print(result_percentage_of_target_amount_numbers_list[k])
                print('\n')

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

    # Based on the judgments, create css class names by replacing the spaces
    # underscores.
    result_judge_total_nutrition_css_class_name = []
    for str_k in result_judge_total_nutrition:
        str_css = str_k.replace(' ', '_')
        result_judge_total_nutrition_css_class_name.append(str_css)


    return result_judge_total_nutrition, result_judge_total_nutrition_css_class_name
