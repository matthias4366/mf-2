def calculate_percentage_of_target_amount(
    nutrientprofile_dict,
    result_total_nutrition_fulldayofeating,
    pprint,
    set_to_zero_if_none,
):

    # Initialize the result
    result_percentage_of_target_amount_str = {}
    result_percentage_of_target_amount_numbers = {}

    for key, value in result_total_nutrition_fulldayofeating.items():

        if nutrientprofile_dict[key] is None:
            result_percentage_of_target_amount_str[key] = ''
            result_percentage_of_target_amount_numbers[key] = None

        elif nutrientprofile_dict[key] == 0:
            result_percentage_of_target_amount_str[key] = 'target amount is zero'
            result_percentage_of_target_amount_numbers[key] = None

        else:
            percentage_target_amount = \
            set_to_zero_if_none(value)\
            / set_to_zero_if_none(nutrientprofile_dict[key])\
            * 100

            percentage_target_amount_rounded = \
            round(percentage_target_amount, 0)

            result_percentage_of_target_amount_numbers[key] = \
            percentage_target_amount_rounded

            result_percentage_of_target_amount_str[key] = \
            str(percentage_target_amount_rounded) + ' ' + '%'

    return result_percentage_of_target_amount_str, \
    result_percentage_of_target_amount_numbers
