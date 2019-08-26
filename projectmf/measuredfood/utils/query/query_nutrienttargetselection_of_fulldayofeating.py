def query_nutrienttargetselection_of_fulldayofeating(
    id_fulldayofeating,
    FullDayOfEating,
    NutrientTargetSelection,
    nutrientprofile_dict,
):

    """
    Query the related NutrientTargetSelection and use it to select the targeted
    nutrients.
    """
    queryset_nutrienttargetselection_of_fulldayofeating = \
    FullDayOfEating.objects.filter(
        id = id_fulldayofeating
    ).values('nutrient_target_selection')
    nutrienttargetselection_id = \
    list(queryset_nutrienttargetselection_of_fulldayofeating)[0]\
    ['nutrient_target_selection']
    queryset_nutrienttargetselection_data = \
    NutrientTargetSelection.objects.filter(
        id = nutrienttargetselection_id
    )
    nutrienttargetselection_dict = \
    list(queryset_nutrienttargetselection_data.values())[0]

    # print('\n nutrienttargetselection_dict \n')
    # pprint.pprint(nutrienttargetselection_dict)

    # Rewrite the targeted_nutrients
    targeted_nutrients = {}
    for key, is_targeted in nutrienttargetselection_dict.items():
        # Only use the keys that end in '_is_targeted'. Otherwise, the keys
        # such as author_id can cause problems as their value, i.e. 1 will be
        # interpreted as True.
        if '_is_targeted' in key:
            if is_targeted:
                # Remove the "_is_targeted" at the end
                nutrient_field_name = key[:-12]
                targeted_nutrients.update(
                    {nutrient_field_name: nutrientprofile_dict[nutrient_field_name]}
                )

    return targeted_nutrients
