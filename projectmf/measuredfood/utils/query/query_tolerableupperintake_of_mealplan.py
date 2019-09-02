

def query_tolerableupperintake_of_mealplan(
    id_mealplan,
    mealplan,
    tolerable_upper_intake,
):

    """
    Query the related tolerable_upper_intake and store the results in
    dictionaries.
    """
    queryset_tolerableupperintake_of_mealplan = \
        mealplan.objects.filter(
            id=id_mealplan
        ).values('tolerable_upper_intake')

    tolerableupperintake_id = \
        list(queryset_tolerableupperintake_of_mealplan)[0][
            'tolerable_upper_intake']

    queryset_tolerableupperintake_data = tolerable_upper_intake.objects.filter(
        id=tolerableupperintake_id
    )

    tolerableupperintake_dict = \
        list(queryset_tolerableupperintake_data.values())[0]

    return tolerableupperintake_dict
