

def query_result_calculation_fulldayofeating(
    id_fulldayofeating,
    specific_ingredient,
    raw_ingredient2,
):

    """
    In the page calculate_fulldayofeating.html, at the bottom, a table
    should display the results of the calculation. Here, the results are
    queried and given to the context dictionary.

    TODO: This function might cause an unnecessary database query,
    as the same data can be saved into a proper results dictionary right
    when it is calculated.
    But this way, the steps are more logically separated, which is fine as well.

    """

    # Get the names of the raw ingredients belonging to the fulldayofeating
    queryset_specificingredient = specific_ingredient.objects.filter(
        fulldayofeating_id=id_fulldayofeating
        )
    list_specificingredient_id = [
        s.id for s in queryset_specificingredient
        ]

    # Get the information about the specific ingredients belonging to the
    # fulldayofeating
    list_of_dict_specificingredient = list(
        queryset_specificingredient.values()
        )

    result_calculation_fulldayofeating = []
    for k in range(len(list_of_dict_specificingredient)):
        specific_ingredient_obj = specific_ingredient.objects.get(
                    id=list_specificingredient_id[k]
                    )

        calculated_amount_k = \
            getattr(specific_ingredient_obj, 'calculated_amount')
        base_amount_unit_k = \
            getattr(specific_ingredient_obj, 'base_amount_unit')

        rawingredient_k_id = specific_ingredient.objects.filter(
                    id=list_specificingredient_id[k]
                    ).values('rawingredient_id')
        rawingredient_k_id = list(rawingredient_k_id)
        rawingredient_k_id = rawingredient_k_id[0]
        rawingredient_k_id = rawingredient_k_id['rawingredient_id']

        rawingredient_k_queryset = raw_ingredient2.objects.filter(
            id=rawingredient_k_id
        )
        name_k = rawingredient_k_queryset.values('name')
        name_k = list(name_k)[0]['name']

        buy_here_link_k = rawingredient_k_queryset.values('buy_here_link')
        buy_here_link_k = list(buy_here_link_k)[0]['buy_here_link']

        merged_dict_k = {
            'specificingredient_id': list_specificingredient_id[k],
            'calculated_amount': calculated_amount_k,
            'base_amount_unit': base_amount_unit_k,
            'name': name_k,
            'buy_here_link': buy_here_link_k
        }
        result_calculation_fulldayofeating.append(merged_dict_k)

    return result_calculation_fulldayofeating
