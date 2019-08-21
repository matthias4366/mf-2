def calculate_percentage_of_tolerable_upper_intake(
    result_total_nutrition_fulldayofeating,
    id_fulldayofeating,
    pprint,
    FullDayOfEating,
    TolerableUpperIntake,
    set_to_zero_if_none,
):

    # Initialize result
    result_percentage_of_tolerable_upper_intake_str = {}
    for key, value in result_total_nutrition_fulldayofeating.items():
        result_percentage_of_tolerable_upper_intake_str[key] = ''

    # Also give the results in the form of numbers so I can use them for
    # the judgement of the total nutrition.
    result_percentage_of_tolerable_upper_intake_numbers = {}
    for key, value in result_total_nutrition_fulldayofeating.items():
        result_percentage_of_tolerable_upper_intake_numbers[key] = None

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

    for key, value in tolerableupperintake_dict.items():
        # pick out only the fields which represent a tolerable upper intake
        if '_tolerable_upper_intake' in key:
            # See if a value exists.
            # print('\n key \n')
            # pprint.pprint(key)
            # Get the name of the nutrient by removing '_upper_intake'.

            nutrient_name = key[:-len('_tolerable_upper_intake')]

            # print('\n nutrient_name \n')
            # pprint.pprint(nutrient_name)

            # If no value exists, save that as the result.
            str_value_exists = nutrient_name + '_value_exists'
            if tolerableupperintake_dict[str_value_exists]:

                percentage_tolerable_upper_intake = \
                (result_total_nutrition_fulldayofeating[nutrient_name] / value) * 100

                percentage_tolerable_upper_intake_rounded = \
                round(percentage_tolerable_upper_intake, 0)

                result_percentage_of_tolerable_upper_intake_numbers\
                [nutrient_name] = \
                percentage_tolerable_upper_intake_rounded

                percentage_tolerable_upper_intake_str = \
                str(percentage_tolerable_upper_intake_rounded)+' %'

                result_percentage_of_tolerable_upper_intake_str[nutrient_name] = \
                percentage_tolerable_upper_intake_str
            else:
                result_percentage_of_tolerable_upper_intake_str[nutrient_name] = \
                ''


    return result_percentage_of_tolerable_upper_intake_str,\
            result_percentage_of_tolerable_upper_intake_numbers
