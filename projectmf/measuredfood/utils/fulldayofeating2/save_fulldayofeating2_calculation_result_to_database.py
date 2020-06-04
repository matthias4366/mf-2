

def save_fulldayofeating2_calculation_result_to_database(
    specificingredient2_dict_list,
    specificingredient2,
):
    for specificingredient2_k in specificingredient2_dict_list:
        s = specificingredient2.objects.get(
            pk=specificingredient2_k['id']
        )
        s.calculated_amount = \
            specificingredient2_k['calculated_amount']
        s.save()
