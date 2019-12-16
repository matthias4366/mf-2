

def calculate_carbohydrate_without_fiber_form(
    form_rawingredient3,
    set_to_zero_if_none,
):
    """
    In the USDA database, the 'Carbohydrate, by difference' value includes
    the fibre. Of course, the number of carbohydrates should not include
    fiber. The number of carbohydrate_without_fiber is calculated by
    subtracting the number of 'Carbohydrate, by difference' and
    'Fiber, total dietary'.
    :param form_rawingredient3: The form used to create or update a
    RawIngredient3 model instance.
    :param set_to_zero_if_none: If the value is None, set it to zero.
    :return:
    """

    carbohydrate_without_fiber_ = \
        set_to_zero_if_none(
            form_rawingredient3.fields[
                'Carbohydrate, by difference-name-1005-id'
            ]
        ) \
        - \
        set_to_zero_if_none(
            form_rawingredient3.fields[
                'Fiber, total dietary-name-1079-id'
            ]
        )

    print('carbohydrate_without_fiber_')
    print(carbohydrate_without_fiber_)

    form_rawingredient3['carbohyrate_without_fiber'] = \
        carbohydrate_without_fiber_

    return form_rawingredient3
