def calculate_percentage_of_target_amount(
    result_total_nutrition_fulldayofeating,
    pprint,
    id_fulldayofeating,
    FullDayOfEating,
    NutrientProfile,
    set_to_zero_if_none,
):

    # Initialize the result
    result_percentage_of_target_amount_str = {}
    result_percentage_of_target_amount_numbers = {}

    """
    Query the related NutrientProfile and store the results in dictionaries.
    """
    queryset_nutrientprofile_of_fulldayofeating = \
    FullDayOfEating.objects.filter(
        id=id_fulldayofeating
    ).values('nutrient_profile')
    nutrientprofile_id = \
    list(queryset_nutrientprofile_of_fulldayofeating)[0]['nutrient_profile']

    queryset_nutrientprofile_data = NutrientProfile.objects.filter(
        id = nutrientprofile_id
    )

    nutrientprofile_dict = list(queryset_nutrientprofile_data.values())[0]
    # print('\n nutrientprofile_dict \n')
    # pprint.pprint(nutrientprofile_dict)
    #
    # print('\n result_total_nutrition_fulldayofeating \n')
    # pprint.pprint(result_total_nutrition_fulldayofeating)

    for key, value in result_total_nutrition_fulldayofeating.items():
        if nutrientprofile_dict[key] is None:
            result_percentage_of_target_amount_str[key] = ''
            result_percentage_of_target_amount_numbers[key] = None
        elif nutrientprofile_dict[key] == 0:
            result_percentage_of_target_amount_str[key] = 'target amount is zero'
            result_percentage_of_target_amount_numbers[key] = None
        else:
            percentage_target_amount = \
            set_to_zero_if_none(value)\
            / set_to_zero_if_none(nutrientprofile_dict[key])\
            * 100
            percentage_target_amount_rounded = \
            round(percentage_target_amount, 0)
            result_percentage_of_target_amount_numbers[key] = \
            percentage_target_amount_rounded
            result_percentage_of_target_amount_str[key] = \
            str(percentage_target_amount_rounded) + ' ' + '%'

    return result_percentage_of_target_amount_str, result_percentage_of_target_amount_numbers
