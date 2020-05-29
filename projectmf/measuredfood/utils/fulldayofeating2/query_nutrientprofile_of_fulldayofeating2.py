

def query_nutrientprofile_of_fulldayofeating2(
    id_fulldayofeating2,
    fulldayofeating2,
    nutrientprofile,
):
    """
    Query the related NutrientProfile and store the results in dictionaries.
    """
    queryset_nutrientprofile_of_fulldayofeating = \
        fulldayofeating2.objects.filter(
            id=id_fulldayofeating2
        ).values('nutrient_profile')
    nutrientprofile_id = \
        list(queryset_nutrientprofile_of_fulldayofeating)[0]['nutrient_profile']

    queryset_nutrientprofile_data = nutrientprofile.objects.filter(
        id=nutrientprofile_id
    )

    nutrientprofile_dict = list(queryset_nutrientprofile_data.values())[0]

    return nutrientprofile_dict
