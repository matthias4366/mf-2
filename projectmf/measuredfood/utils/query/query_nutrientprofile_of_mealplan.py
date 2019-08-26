def query_nutrientprofile_of_mealplan(
    id_mealplan,
    Mealplan,
    NutrientProfile,
):
    """
    Query the related NutrientProfile and store the results in dictionaries.
    """
    queryset_nutrientprofile_of_mealplan = \
    Mealplan.objects.filter(
        id=id_mealplan
    ).values('nutrient_profile')
    nutrientprofile_id = \
    list(queryset_nutrientprofile_of_mealplan)[0]['nutrient_profile']

    queryset_nutrientprofile_data = NutrientProfile.objects.filter(
        id = nutrientprofile_id
    )

    nutrientprofile_dict = list(queryset_nutrientprofile_data.values())[0]

    # print('\n nutrientprofile_dict \n')
    # pprint.pprint(nutrientprofile_dict)

    return nutrientprofile_dict
