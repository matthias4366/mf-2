

def prepare_calculation_result_for_display(
    specificingredient2_dict_list,
):
    result_calculate_fulldayofeating_formatted_for_template = []

    for specificingredient2_k in specificingredient2_dict_list:

        merged_dict_k = {
            'specificingredient_id': specificingredient2_k['id'],
            'calculated_amount': specificingredient2_k['calculated_amount'],
            'name': specificingredient2_k['raw_ingredient']['name'],
        }
        result_calculate_fulldayofeating_formatted_for_template.append(
            merged_dict_k
        )

    return result_calculate_fulldayofeating_formatted_for_template
