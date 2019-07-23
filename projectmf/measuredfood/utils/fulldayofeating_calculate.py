def calculate_fulldayofeating(
    id_fulldayofeating,
    SpecificIngredient,
    FullDayOfEating,
    NutrientProfile
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
    Get the related SpecificIngredients and the NutrientProfile.
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
    Initialize a list of SpecificIngredients.
    """
    # 0 is not to be changed.
    specificingredient_dict_list_0 = list(
        queryset_specificingredient_0.values()
        )
    # 1 will be used for calculations, i.e. the fixed values will be removed.
    specificingredient_dict_list_1 = list(
        queryset_specificingredient_1.values()
        )



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
