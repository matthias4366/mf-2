def query_tolerableupperintake_of_fulldayofeating(
    id_fulldayofeating,
    FullDayOfEating,
    TolerableUpperIntake,
):

    """
    Query the related TolerableUpperIntake and store the results in dictionaries.
    """
    queryset_tolerableupperintake_of_fulldayofeating = \
    FullDayOfEating.objects.filter(
        id=id_fulldayofeating
    ).values('tolerable_upper_intake')

    tolerableupperintake_id = \
    list(queryset_tolerableupperintake_of_fulldayofeating)\
    [0]['tolerable_upper_intake']

    queryset_tolerableupperintake_data = TolerableUpperIntake.objects.filter(
        id = tolerableupperintake_id
    )

    tolerableupperintake_dict = list(queryset_tolerableupperintake_data.values())[0]

    # print('\n tolerableupperintake_dict \n')
    # pprint.pprint(tolerableupperintake_dict)

    return tolerableupperintake_dict
