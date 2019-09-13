

def calculate_percentage_of_tolerable_upper_intake(
    tolerableupperintake_dict,
    result_total_nutrition_fulldayofeating,
):

    # Initialize result
    result_percentage_of_tolerable_upper_intake_str = {}
    for key, value in result_total_nutrition_fulldayofeating.items():
        result_percentage_of_tolerable_upper_intake_str[key] = ''

    # Also give the results in the form of numbers so I can use them for
    # the judgement of the total nutrition.
    result_percentage_of_tolerable_upper_intake_numbers = {}
    for key, value in result_total_nutrition_fulldayofeating.items():
        result_percentage_of_tolerable_upper_intake_numbers[key] = None

    for key, value in tolerableupperintake_dict.items():
        # pick out only the fields which represent a tolerable upper intake
        if '_tolerable_upper_intake' in key:
            # Get the name of the nutrient by removing '_upper_intake'.

            nutrient_name = key[:-len('_tolerable_upper_intake')]

            tolerableupperintake_value_exists = \
                (value is not None) and (value > 0)

            if tolerableupperintake_value_exists:

                percentage_tolerable_upper_intake = \
                    (result_total_nutrition_fulldayofeating[
                         nutrient_name] / value) * 100

                percentage_tolerable_upper_intake_rounded = \
                    round(percentage_tolerable_upper_intake, 0)

                result_percentage_of_tolerable_upper_intake_numbers[
                    nutrient_name] = \
                    percentage_tolerable_upper_intake_rounded

                percentage_tolerable_upper_intake_str = \
                    str(percentage_tolerable_upper_intake_rounded)+' %'

                result_percentage_of_tolerable_upper_intake_str[
                    nutrient_name] = \
                    percentage_tolerable_upper_intake_str
            else:
                result_percentage_of_tolerable_upper_intake_str[
                    nutrient_name] = ''

    return result_percentage_of_tolerable_upper_intake_str,\
        result_percentage_of_tolerable_upper_intake_numbers
