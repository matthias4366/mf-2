def query_specificnutrienttarget_of_fulldayofeating(
    id_fulldayofeating,
    SpecificNutrientTarget,
    nutrientprofile_dict,
    pprint,
):

    # Initialize result.
    targeted_nutrients = {}

    targeted_nutrients_errors = {
        'missing_nutrientprofile_value': False,
        'nutrients_missing_nutrientprofile_value': [],
    }

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
        nutrient_target_name = dict_k['nutrient_target']
        if nutrientprofile_dict[nutrient_target_name] is None:
            nutrient_target_amount = 0
            targeted_nutrients_errors['missing_nutrientprofile_value'] = True
            targeted_nutrients_errors\
            ['nutrients_missing_nutrientprofile_value'].append(
                nutrient_target_name
            )
        elif nutrientprofile_dict[nutrient_target_name] is not None:
            nutrient_target_amount = nutrientprofile_dict[nutrient_target_name]
        else:
            print('\n This case should not be possible.')
            print('Occured in query_specificnutrienttarget_of_fulldayofeating. \n')
            return

        new_dict = {nutrient_target_name: nutrient_target_amount}
        targeted_nutrients.update(new_dict)

    return targeted_nutrients, targeted_nutrients_errors
