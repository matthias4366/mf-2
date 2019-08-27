def query_specificnutrienttarget_of_fulldayofeating(
    id_fulldayofeating,
    SpecificNutrientTarget,
    nutrientprofile_dict,
    pprint,
):

    # Initialize result.
    targeted_nutrients = {}

    queryset_specificnutrienttarget_of_fulldayofeating = \
    SpecificNutrientTarget.objects.filter(
        fulldayofeating = id_fulldayofeating
    )

    # print('\n queryset_specificnutrienttarget_of_fulldayofeating \n')
    # pprint.pprint(queryset_specificnutrienttarget_of_fulldayofeating)

    specificnutrienttarget_list = \
    list(queryset_specificnutrienttarget_of_fulldayofeating.values(
        'nutrient_target'
        ))

    # print('\n specificnutrienttarget_list \n')
    # pprint.pprint(specificnutrienttarget_list)

    # print('\n nutrientprofile_dict \n')
    # pprint.pprint(nutrientprofile_dict)

    for dict_k in specificnutrienttarget_list:
        nutrient_target = dict_k['nutrient_target']
        new_dict = {nutrient_target: nutrientprofile_dict[nutrient_target]}
        targeted_nutrients.update(new_dict)

    # print('\n targeted_nutrients \n')
    # pprint.pprint(targeted_nutrients)

    return targeted_nutrients
