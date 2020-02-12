

def make_name_of_duplicate_rawingredient3(
    original_name
):
    """
    The problem: A user copies a RawIngredient3 from the FoodData Central
    database. If such an ingredient already exists in their list of
    ingredients, they get duplicate ingredients with exactly the same name.
    Since they are possibly linked to different FullDayOfEating objects,
    it gets confusing.

    The solution: If an ingredient is about to be saved in the users list of
    ingredients, the name of the duplicate ingredient is changed by adding a
    number at the end.
    :param original_name:
    :return:
    """

    # Find the number at the end of the RawIngredient3 object's name,
    # for example Pasta12 => find 12.

    return name_of_duplicate