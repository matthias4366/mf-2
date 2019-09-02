

def query_nutrientprofile_of_fulldayofeating(
    id_fulldayofeating,
    full_day_of_eating,
    nutrient_profile,
):
    """
    Query the related NutrientProfile and store the results in dictionaries.
    """
    queryset_nutrientprofile_of_fulldayofeating = \
        full_day_of_eating.objects.filter(
            id=id_fulldayofeating
        ).values('nutrient_profile')
    nutrientprofile_id = \
        list(queryset_nutrientprofile_of_fulldayofeating)[0]['nutrient_profile']

    queryset_nutrientprofile_data = nutrient_profile.objects.filter(
        id=nutrientprofile_id
    )

    nutrientprofile_dict = list(queryset_nutrientprofile_data.values())[0]

    return nutrientprofile_dict
