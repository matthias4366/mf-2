def calculate_fulldayofeating(
    id_fulldayofeating,
    SpecificIngredient,
    FullDayOfEating,
    NutrientProfile,
    RawIngredient,
    pprint
    ):
    """
    This function should be independent of everything else.
    It should be a PURE function, i.e. work solely with inputs and outputs.
    It is given an id_fulldayofeating. Based on that, it retrieves the
    SpecificIngredients belonging to that FullDayOfEating and the
    NutrientProfile. It then calculates the final amounts and saves them to the
    fields "calculated_amount".

    Calculate the fulldayofeating, i.e. calculate the calculated_amount
    values for the SpecificIngredient instances associated with a
    FullDayOfEating, which is associated with a NutrientProfile.
    """
    # Some stuff so the function is not empty
    print(f'\nFunction calculate_fulldayofeating is called.\n')

    """
    Get the ID of the FullDayOfEating that is calculated.
    """

    # done by taking the value as a function argument.

    """
    Query the related SpecificIngredients and the NutrientProfile.
    """
    queryset_specificingredient_0 = SpecificIngredient.objects.filter(
        fulldayofeating_id=id_fulldayofeating
        )
    queryset_specificingredient_1 = SpecificIngredient.objects.filter(
        fulldayofeating_id=id_fulldayofeating
        )

    queryset_nutrientprofile_of_fulldayofeating = \
    FullDayOfEating.objects.filter(
        id=id_fulldayofeating
    ).values('nutrient_profile')
    nutrientprofile_id = \
    list(queryset_nutrientprofile_of_fulldayofeating)[0]['nutrient_profile']

    queryset_nutrientprofile_data = NutrientProfile.objects.filter(
        id = nutrientprofile_id
    )

    """
    For the SpecificIngredients, store the data from the querysets in
    dictionaries. The RawIngredient should be included in that same dictionary
    in explicit form.
    """
    # 0 is not to be changed.
    specificingredient_dict_list_0 = list(
        queryset_specificingredient_0.values()
        )

    # 1 will be used for calculations, i.e. the fixed values will be removed.
    specificingredient_dict_list_1 = list(
        queryset_specificingredient_1.values()
        )

    # Add the RawIngredient dictionaries to the SpecificIngredient dictionaries
    # to make the nutrition values (kcal etc.) accessible for calculation.
    for k in range(len(specificingredient_dict_list_1)):
        rawingredient_k_queryset = RawIngredient.objects.filter(
            id = specificingredient_dict_list_1[k]['rawingredient_id']
        ).values()
        rawingredient_k_dict = list(rawingredient_k_queryset)[0]
        specificingredient_dict_list_1[k].update(
            raw_ingredient = rawingredient_k_dict
            )

    # print('\nspecificingredient_dict_list_1 AFTER the addition of the ' \
    #       'RawIngredient dictionaries:')
    # pprint.pprint(specificingredient_dict_list_1)



    """
    Iterate through the dictionaries representing the SpecificIngredients
    and sort them by their 'scaling_option' property.
    """
    specificingredient_scalingoption_fixed = []
    specificingredient_scalingoption_independent = []
    specificingredient_scalingoption_group = []
    for dict_k in specificingredient_dict_list_1:
        if dict_k['scaling_option'] == 'FIXED':
            specificingredient_scalingoption_fixed.append(dict_k)
        elif dict_k['scaling_option'] == 'INDEPENDENT':
            specificingredient_scalingoption_independent.append(dict_k)
    #     elif len(dict_k['scaling_option']) == 1:
    #     else:
    #         print('ERROR. The value given for scaling_group option was' \
    #               ' not valid.')

    # print('\n specificingredient_scalingoption_fixed')
    # pprint.pprint(specificingredient_scalingoption_fixed)
    print('\n specificingredient_scalingoption_independent')
    pprint.pprint(specificingredient_scalingoption_independent)

    """
    Return the values to make this a PURE function
    """
    # return

def create_ingredient_average():
    """
    For each group of ingredients, create an average ingredient representing
    the group. Use the base_amounts to set the ratios.
    """

    return 'result create ingredient average'
