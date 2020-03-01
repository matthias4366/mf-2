

def make_displayed_name(
    name_,
    id_,
):
    """
    Display an object name such that two objects with the same name are
    discernable.

    When a user copies a FullDayOfEating from another user, all the
    RawIngredient3 objects are copied as well. It is possible, that the user
    already has RawIngredient3 objects with the same name. In that case,
    the user could not distinguish the old RawIngredient3 objects from the
    newly added RawIngredient3 objects, causing confusion. The confusion is
    reduced by adding the object ID to name created by the object's __str__()
    method.

    :param name_:
    :param id_:
    :return:
    """
    displayed_name_ = \
        name_ \
        + ' #ID' \
        + str(id_)
    return displayed_name_
