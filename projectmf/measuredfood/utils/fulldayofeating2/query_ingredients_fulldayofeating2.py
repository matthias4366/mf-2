

def query_ingredients_fulldayofeating2(
    id_fulldayofeating2,
    specificingredient2,
    pprint,
    rawingredient3,
    all_nutrients_and_default_units,
    set_to_zero_if_none,
):
    """
    Query the SpecificIngredient2 objects related to a FullDayOfEating2
    objects. Save them in a dictionary that is used to calculate the amounts
    of the ingredients in the FullDayOfEating2.
    :param id_fulldayofeating2: primary key of the FullDayOfEating2 object.
    :param specificingredient2: SpecificIngredient2 model.
    :param pprint: pprint module for nice printing during development.
    :param rawingredient3: RawIngredient3 model.
    :param all_nutrients_and_default_units: constant
    ALL_NUTRIENTS_AND_DEFAULT_UNITS
    :param set_to_zero_if_none: function that sets a value to zero if it is
    None, so there are no problems in the calculations.
    :return: specificingredient_dict_list
    """

    queryset_specificingredient = specificingredient2.objects.filter(
        fulldayofeating2_id=id_fulldayofeating2
        ).order_by('id')
    # pprint.pprint('queryset_specificingredient')
    # pprint.pprint(queryset_specificingredient)

    specificingredient_dict_list = list(
        queryset_specificingredient.values()
        )

    # Add the RawIngredient3 dictionaries to the SpecificIngredient dictionaries
    # to make the nutrition values (kcal etc.) accessible for calculation.
    for k in range(len(specificingredient_dict_list)):
        rawingredient_k_queryset = rawingredient3.objects.filter(
            id=specificingredient_dict_list[k]['rawingredient3_id']
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

    return specificingredient_dict_list
