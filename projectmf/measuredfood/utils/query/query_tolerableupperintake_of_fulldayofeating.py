

def query_tolerableupperintake_of_fulldayofeating(
    id_fulldayofeating,
    full_day_of_eating,
    tolerable_upper_intake,
):

    """
    Query the related tolerable_upper_intake and store the results in
    dictionaries.
    """
    queryset_tolerableupperintake_of_fulldayofeating = \
        full_day_of_eating.objects.filter(
            id=id_fulldayofeating
        ).values('tolerable_upper_intake')

    tolerableupperintake_id = \
        list(queryset_tolerableupperintake_of_fulldayofeating)[0][
            'tolerable_upper_intake']

    queryset_tolerableupperintake_data = tolerable_upper_intake.objects.filter(
        id=tolerableupperintake_id
    )

    tolerableupperintake_dict = \
        list(queryset_tolerableupperintake_data.values())[0]

    return tolerableupperintake_dict
