def query_ingredients_fulldayofeating(
    id_fulldayofeating,
    SpecificIngredient,
    RawIngredient2,
    pprint,
):
    """
    This function assists the function calculate_total_price_fulldayofeating.
    calculate_total_price_fulldayofeating should remain a pure function, i.e.
    it should work without database queries. Hence, the database queries are
    outsourced to the query_ingredients_fulldayofeating function.

    Based on the id_fulldayofeating, this function queries all the related
    SpecificIngredient objects and saves them in a dictionary and saves the
    dictionaries in a list, which will ultimately be the result.

    Additionally, the RawIngredient2 objects related to the SpecificIngredient
    objects are queried and their information is stored in a sub dictionary
    in the dictionary of the SpecificIngredient.
    """

    # initialize result
    specificingredient_dict_list = []

    """
    Query the related SpecificIngredients and store the results in dictionaries.
    """
    queryset_specificingredient = SpecificIngredient.objects.filter(
        fulldayofeating_id=id_fulldayofeating
        )

    specificingredient_dict_list = list(
        queryset_specificingredient.values()
        )

    # Add the RawIngredient2 dictionaries to the SpecificIngredient dictionaries
    # to make the nutrition values (kcal etc.) accessible for calculation.
    for k in range(len(specificingredient_dict_list)):
        rawingredient_k_queryset = RawIngredient2.objects.filter(
            id = specificingredient_dict_list[k]['rawingredient_id']
        ).values()
        rawingredient_k_dict = list(rawingredient_k_queryset)[0]
        specificingredient_dict_list[k].update(
            raw_ingredient = rawingredient_k_dict
            )

    # print('\n specificingredient_dict_list \n')
    # pprint.pprint(specificingredient_dict_list)

    return specificingredient_dict_list
