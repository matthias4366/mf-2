

def query_ingredients_fulldayofeating(
    id_fulldayofeating,
    specific_ingredient,
    raw_ingredient3,
    all_nutrients_and_default_units,
    set_to_zero_if_none,
    no_specific_ingredient_in_full_day_of_eating_error,
):
    """
    This function assists the function calculate_total_price_fulldayofeating.
    calculate_total_price_fulldayofeating should remain a pure function, i.e.
    it should work without database queries. Hence, the database queries are
    outsourced to the query_ingredients_fulldayofeating function.

    Based on the id_fulldayofeating, this function queries all the related
    SpecificIngredient objects and saves them in a dictionary and saves the
    dictionaries in a list, which will ultimately be the result.

    Additionally, the RawIngredient3 objects related to the SpecificIngredient
    objects are queried and their information is stored in a sub dictionary
    in the dictionary of the SpecificIngredient.
    """
    # The point of the ordering is to display the ingredients in the
    # calculation results of the full day of eating in the same order in
    # which the user entered them in the form of the full day of eating.
    queryset_specificingredient = specific_ingredient.objects.filter(
        fulldayofeating_id=id_fulldayofeating
        ).order_by('id')

    specificingredient_dict_list = list(
        queryset_specificingredient.values()
        )

    # Add the RawIngredient3 dictionaries to the SpecificIngredient dictionaries
    # to make the nutrition values (kcal etc.) accessible for calculation.
    for k in range(len(specificingredient_dict_list)):
        rawingredient_k_queryset = raw_ingredient3.objects.filter(
            id=specificingredient_dict_list[k]['rawingredient_id']
        ).values()
        rawingredient_k_dict = list(rawingredient_k_queryset)[0]

        # Make sure that no None fields are returned.
        for nutrient_dict in all_nutrients_and_default_units:

            # print('\n')
            # print('nutrient_dict')
            # print(nutrient_dict)
            # print('\n')

            nutrient_name = nutrient_dict['nutrient_name_measuredfood']
            rawingredient_k_dict[nutrient_name] = \
                set_to_zero_if_none(rawingredient_k_dict[nutrient_name])

        specificingredient_dict_list[k].update(
            raw_ingredient=rawingredient_k_dict
            )

    # Catch the error that the user did not add any ingredients whatsoever.
    if len(specificingredient_dict_list) == 0:
        raise(no_specific_ingredient_in_full_day_of_eating_error())

    return specificingredient_dict_list
