

def save_fulldayofeating_calculation_result_to_database(
    specificingredient_id_and_calculated_amount,
    specific_ingredient
):
    """
    This is not a pure function as it saves to the database.
    This function takes in the results calculated by the
    calculate_fulldayofeating function and saves them in the database.
    The relevant entries are the 'calculated_amount' fields of the
    SpecificIngredients.
    """
    for k in range(len(specificingredient_id_and_calculated_amount)):
        s = specific_ingredient.objects.get(
            pk=specificingredient_id_and_calculated_amount[k]['id']
        )
        s.calculated_amount = \
            specificingredient_id_and_calculated_amount[k]['calculated_amount']
        s.save()
