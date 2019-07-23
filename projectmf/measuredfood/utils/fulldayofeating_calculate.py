def calculate_fulldayofeating(
    id_fulldayofeating,
    SpecificIngredient,
    FullDayOfEating,
    NutrientProfile
    ):
    """
    This function should be independent of everything else.
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
    Step 1:
    Get the ID of the FullDayOfEating that is calculated.
    """

    """
    Step 2:
    Get the related SpecificIngredients and the NutrientProfile.
    """
    queryset_specificingredient_0 = SpecificIngredient.objects.filter(
        fulldayofeating_id=id_fulldayofeating
        )
    queryset_specificingredient_1 = SpecificIngredient.objects.filter(
        fulldayofeating_id=id_fulldayofeating
        )

    """
    Step 3:
    Initialize a list of SpecificIngredients.
    """
    # 0 is not to be touched.
    list_of_dict_specificingredient_0 = list(
        queryset_specificingredient_0.values()
        )
    # 1 will be used for calculations, i.e. the fixed values will be removed.
    list_of_dict_specificingredient_1 = list(
        queryset_specificingredient_1.values()
        )
    """
    Remove all SpecificIngredients whose scaling_option is set to 'fixed'.
    """
    specificingredient_scaling_variable = []
    for dict in list_of_dict_specificingredient_1:
        if dict['scaling_option'] != 'FIXED':
            specificingredient_scaling_variable.append(dict)

    """
    TODO: Check for error: add up all the fixed ingredients and see if some
    nutrients are already higher than their targets.
    """

    """
    For each group of ingredients, create an average ingredient representing
    the group. Use the base_amounts to set the ratios.
    """



    """
    Check for error: When multiple ingredients belong to the same group, they
    need to have base_amounts defined, otherwise the ratios are not defined.
    If none of the ingredients in the group have base_amounts defined, it is
    assumed that all ingredients are to have equal ratios.
    The ingredients are now called 'averaged_ingredients'.
    """

    """
    Step 4:
    Solve the linear equation system. Now we have the calculated_amounts_1.
    De-average the ingredients while considering the ratios defined by the
    base_amounts, as before. E.g. 300 g rice_and_beans => 100 g rice + 200 g beans.
    Check which ingredients have steps. If an ingredient has a step defined,
    take the respective calculated_amounts_1 value and round it to the nearest
    step. E.g. stepsize: 100 g, calculated_amount_1 = 123 g =>
    calculated_amount_2 = 100 g.
    Create a new, internal copy of the FullDayOfEating, for example by adding
    the fields to the model. The fields would be: scaling_interim_1
    (which will be set to fixed after the calculated_amount_1 has been rounded
    to the nearest step),
    calculated_amount_interim_2.
    Set all the ingredients who have calculated_amount_2 values to fix.
    Solve the linear equation system again with the remaining ingredients.
    """

    """
    It should be a pure function, i.e. it should work exclusively with inputs
    and outputs.
    """
    # Make mock values for now to make sure you are building this as a PURE
    # function.
    list_calculated_amount = []
    for k in range(len(list_of_dict_specificingredient_0)):
        list_calculated_amount.append(k*100+1)
    error_message_calculate_fulldayofeating = None

    return list_calculated_amount, error_message_calculate_fulldayofeating

def create_ingredient_average():
    """
    For each group of ingredients, create an average ingredient representing
    the group. Use the base_amounts to set the ratios.
    """

    return 'result create ingredient average'
