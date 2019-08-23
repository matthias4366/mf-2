def query_tolerableupperintake_of_mealplan(
    id_mealplan,
    Mealplan,
    TolerableUpperIntake,
    pprint,
):

    """
    Query the related TolerableUpperIntake and store the results in dictionaries.
    """
    queryset_tolerableupperintake_of_mealplan = \
    Mealplan.objects.filter(
        id=id_mealplan
    ).values('tolerable_upper_intake')

    # print('\n queryset_tolerableupperintake_of_mealplan \n')
    # pprint.pprint(queryset_tolerableupperintake_of_mealplan)

    tolerableupperintake_id = \
    list(queryset_tolerableupperintake_of_mealplan)\
    [0]['tolerable_upper_intake']

    # print('\n tolerableupperintake_id \n')
    # pprint.pprint(tolerableupperintake_id)

    queryset_tolerableupperintake_data = TolerableUpperIntake.objects.filter(
        id = tolerableupperintake_id
    )

    # print('\n queryset_tolerableupperintake_data \n')
    # pprint.pprint(queryset_tolerableupperintake_data)


    tolerableupperintake_dict = \
    list(queryset_tolerableupperintake_data.values())[0]

    # print('\n tolerableupperintake_dict \n')
    # pprint.pprint(tolerableupperintake_dict)

    return tolerableupperintake_dict
