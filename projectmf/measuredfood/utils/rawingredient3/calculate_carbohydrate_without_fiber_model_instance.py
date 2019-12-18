

def calculate_carbohydrate_without_fiber_model_instance(
    rawingredient3_instance,
    set_to_zero_if_none,
):
    """
    :param rawingredient3_instance:
    :param set_to_zero_if_none:
    :return:
    """

    carbohydrate_by_difference_ = getattr(
        rawingredient3_instance,
        'carbohydrate_by_difference-name-1005-id',
    )
    carbohydrate_by_difference_ = \
        set_to_zero_if_none(carbohydrate_by_difference_)

    fiber_total_dietary_ = getattr(
        rawingredient3_instance,
        'fiber_total_dietary-name-1079-id',
    )
    fiber_total_dietary_ = set_to_zero_if_none(fiber_total_dietary_)

    carbohydrate_without_fiber_ = \
        carbohydrate_by_difference_ - fiber_total_dietary_

    # If the amount of carbohydrates is not defined, it is possible to obtain
    # a negative result. That does not make physical sense, hence it is
    # caught here.
    if carbohydrate_without_fiber_ < 0:
        carbohydrate_without_fiber_ = 0

    setattr(
        rawingredient3_instance,
        "carbohydrate_without_fiber-name-1-id",
        carbohydrate_without_fiber_
    )

    return rawingredient3_instance
