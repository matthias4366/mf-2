

def calculate_carbohydrate_without_fiber_model_instance(
    rawingredient3_instance,
    set_to_zero_if_none,
):
    """
    :param rawingredient3_instance:
    :return:
    """

    carbohydrate_by_difference_ = getattr(
        rawingredient3_instance,
        'Carbohydrate, by difference-name-1005-id',
    )
    carbohydrate_by_difference_ = \
        set_to_zero_if_none(carbohydrate_by_difference_)

    fiber_total_dietary_ = getattr(
        rawingredient3_instance,
        'Fiber, total dietary-name-1079-id',
    )
    fiber_total_dietary_ = set_to_zero_if_none(fiber_total_dietary_)

    carbohydrate_without_fiber_ = \
        carbohydrate_by_difference_ - fiber_total_dietary_

    # print('carbohydrate_without_fiber_')
    # print(carbohydrate_without_fiber_)

    setattr(
        rawingredient3_instance,
        "carbohydrate_without_fiber",
        carbohydrate_without_fiber_
    )

    return rawingredient3_instance
