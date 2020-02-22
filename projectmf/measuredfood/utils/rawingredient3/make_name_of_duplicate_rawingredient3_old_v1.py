

def make_name_of_duplicate_rawingredient3(
    original_name,
    re,
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
    :param re: Python module for regular expressions.
    :return:
    """

    # Find the number at the end of the RawIngredient3 object's name,
    # for example Pasta12 => find 12.

    current_number_at_end_list = re.findall('([0-9]+)$', original_name)

    if len(current_number_at_end_list) == 0:
        new_number = 1
        original_name_stem = original_name
    else:
        current_number_at_end = current_number_at_end_list[0]
        new_number = int(current_number_at_end) + 1
        n_chars_in_original_name_stem = \
            len(original_name) - len(str(current_number_at_end))
        original_name_stem = original_name[
            0:n_chars_in_original_name_stem
        ]

    name_of_duplicate = original_name_stem + str(new_number)

    return name_of_duplicate
