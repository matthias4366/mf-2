

def query_ingredients_fulldayofeating(
    id_fulldayofeating,
    specific_ingredient,
    raw_ingredient2,
    all_nutrients_and_default_units,
    set_to_zero_if_none,
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
    queryset_specificingredient = specific_ingredient.objects.filter(
        fulldayofeating_id=id_fulldayofeating
        )

    specificingredient_dict_list = list(
        queryset_specificingredient.values()
        )

    # Add the RawIngredient2 dictionaries to the SpecificIngredient dictionaries
    # to make the nutrition values (kcal etc.) accessible for calculation.
    for k in range(len(specificingredient_dict_list)):
        rawingredient_k_queryset = raw_ingredient2.objects.filter(
            id=specificingredient_dict_list[k]['rawingredient_id']
        ).values()
        rawingredient_k_dict = list(rawingredient_k_queryset)[0]

        # Make sure that no None fields are returned.
        for nutrient_dict_k in all_nutrients_and_default_units:
            nutrient_name = nutrient_dict_k['name']
            rawingredient_k_dict[nutrient_name] = \
                set_to_zero_if_none(rawingredient_k_dict[nutrient_name])

        specificingredient_dict_list[k].update(
            raw_ingredient=rawingredient_k_dict
            )

    return specificingredient_dict_list
