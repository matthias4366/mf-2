
def calculate_fulldayofeating(id_fulldayofeating):
    """
    Calculate the fulldayofeating, i.e. calculate the calculated_amount
    values for the SpecificIngredient instances associated with a
    FullDayOfEating, which is associated with a NutrientProfile.

    Step 1:
    Get the ID of the FullDayOfEating that is calculated.

    Step 2:
    Get the related SpecificIngredients and the NutrientProfile.

    Step 3:
    Initialize a list of SpecificIngredients.
    Remove all SpecificIngredients whose scaling_option is set to 'fixed'.
    Check for error: add up all the fixed ingredients and see if some nutrients
    are already higher than the target.
    For each group of ingredients, create an average ingredient representing
    the group. Use the base_amounts to set the ratios.
    Check for error: When multiple ingredients belong to the same group, they
    need to have base_amounts defined, otherwise the ratios are not defined.
    If none of the ingredients in the group have base_amounts defined, it is
    assumed that all ingredients are to have equal ratios.
    The ingredients are now called 'averaged_ingredients'.

    Step 4:
    Solve the linear equation system. Now we have the calculated_amounts_1.
    De-average the ingredients while considering the ratios defined by the
    base_amounts, as before. E.g. 300 g rice_and_beans => 100 g rice + 200 g beans.
    Check which ingredients have steps. If an ingredient has a step defined,
    take the respective calculated_amounts_1 value and round it to the nearest
    step. E.g. stepsize: 100 g, calculated_amount_1 = 123 g =>
    calculated_amount_2 = 100 g.
    Create a new, internal copy of the FullDayOfEating, for example by adding
    the fields to the model. The fields would be: scaling_interim_1,
    calculated_amount_interim_2.
    Set all the ingredients who have calculated_amount_2 values to fix


    """
    pass
