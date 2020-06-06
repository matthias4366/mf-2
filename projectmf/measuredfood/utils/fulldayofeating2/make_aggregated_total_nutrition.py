# import pprint


def make_aggregated_total_nutrition(
    specificingredient2_dict_list,
    calculate_total_nutrition_fulldayofeating2,
    all_nutrients_and_default_units,
    set_to_zero_if_none,
    calculate_percentage_of_target_amount,
    nutrientprofile_dict,
    calculate_percent_max_fulldayofeating,
    judge_total_nutrition,
    copy,
):
    """
    The calculated_amount values in the SpecificIngredient2 objects in a
    FullDayOfEating2 have been calculated.

    Now, the total nutrition of the FullDayOfEating2 is calculated and
    returned in a dictionary that can be used in the html template.
    :return:
    """

    result_total_nutrition_fulldayofeating, \
        result_total_nutrition_fulldayofeating_rounded = \
        calculate_total_nutrition_fulldayofeating2(
            specificingredient2_dict_list,
            all_nutrients_and_default_units,
            set_to_zero_if_none,
        )

    # print('result_total_nutrition_fulldayofeating')
    # pprint.pprint(result_total_nutrition_fulldayofeating)
    # print('result_total_nutrition_fulldayofeating_rounded')
    # pprint.pprint(result_total_nutrition_fulldayofeating_rounded)

    # Make the result_total_nutrition_fulldayofeating_rounded into a list.
    result_total_nutrition_fulldayofeating_rounded_list = []
    nutrient_name_measuredfood_list = []
    for key, value in \
            result_total_nutrition_fulldayofeating_rounded.items():
        result_total_nutrition_fulldayofeating_rounded_list.append(value)
        nutrient_name_measuredfood_list.append(key)

    # Calculate the ratio of the total nutrition in the full day of eating
    # in relation to the target amounts in the nutrient profile and
    # express the result as a percentage.

    result_percentage_of_target_amount_str, \
        result_percentage_of_target_amount_numbers = \
        calculate_percentage_of_target_amount(
            nutrientprofile_dict,
            result_total_nutrition_fulldayofeating,
            set_to_zero_if_none,
        )

    # Make the result_percentage_of_target_amount_str into a list
    result_percentage_of_target_amount_list = []

    for key, value in result_percentage_of_target_amount_str.items():
        result_percentage_of_target_amount_list.append(value)

    # Make the result_percentage_of_target_amount_numbers into a list
    result_percentage_of_target_amount_numbers_list = []
    for key, value in result_percentage_of_target_amount_numbers.items():
        result_percentage_of_target_amount_numbers_list.append(value)

    # 'Max amount' and 'tolerable upper intake' are used interchangeably.
    result_percent_max_dict, \
        result_percentage_of_tolerable_upper_intake_str_list, \
        result_percentage_of_tolerable_upper_intake_numbers_list = \
        calculate_percent_max_fulldayofeating(
            nutrientprofile_dict,
            result_total_nutrition_fulldayofeating,
        )

    # Make the default units into a list and display them in the table.
    default_unit_list = []
    for dict_k in all_nutrients_and_default_units:
        default_unit_list.append(dict_k['unit_nutrient_usda_api'])

    result_judge_total_nutrition, \
        result_judge_total_nutrition_css_class_name = judge_total_nutrition(
            result_percentage_of_target_amount_numbers_list,
            result_percentage_of_tolerable_upper_intake_numbers_list,
            set_to_zero_if_none,
        )

    aggregated_total_nutrition_fulldayofeating = \
        zip(
            nutrient_name_measuredfood_list,
            result_total_nutrition_fulldayofeating_rounded_list,
            default_unit_list,
            result_percentage_of_target_amount_list,
            result_percentage_of_tolerable_upper_intake_str_list,
            result_judge_total_nutrition,
            result_judge_total_nutrition_css_class_name,
        )

    aggregated_ = copy.deepcopy(aggregated_total_nutrition_fulldayofeating)

    # Remove the nutrients which are not to be displayed.
    aggregated_total_nutrition_not_all_nutrients_displayed = []
    for ab in aggregated_:
        for nutrient_dict in all_nutrients_and_default_units:
            if nutrient_dict['is_displayed']:
                if ab[0] == nutrient_dict['nutrient_name_measuredfood']:
                    # Add a tuple containing the nutrient name from the
                    # USDA API, which is much more readable and thus
                    # better to display.
                    ab = ab + (nutrient_dict['nutrient_name_usda_api'],)
                    aggregated_total_nutrition_not_all_nutrients_displayed. \
                        append(ab)
                else:
                    continue
            else:
                continue

    return aggregated_total_nutrition_not_all_nutrients_displayed
