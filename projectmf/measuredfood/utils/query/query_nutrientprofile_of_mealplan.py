

def query_nutrientprofile_of_mealplan(
    id_mealplan,
    mealplan,
    nutrient_profile,
):
    """
    Query the related nutrient_profile and store the results in dictionaries.
    """
    queryset_nutrientprofile_of_mealplan = \
        mealplan.objects.filter(
            id=id_mealplan
        ).values('nutrient_profile')
    nutrientprofile_id = \
        list(queryset_nutrientprofile_of_mealplan)[0]['nutrient_profile']

    queryset_nutrientprofile_data = nutrient_profile.objects.filter(
        id=nutrientprofile_id
    )

    nutrientprofile_dict = list(queryset_nutrientprofile_data.values())[0]

    return nutrientprofile_dict
