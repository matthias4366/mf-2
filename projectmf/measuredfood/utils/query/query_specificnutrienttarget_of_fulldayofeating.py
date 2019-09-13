

def query_specificnutrienttarget_of_fulldayofeating(
    id_fulldayofeating,
    specific_nutrient_target,
    nutrientprofile_dict,
):

    # Initialize result.
    targeted_nutrients = {}

    targeted_nutrients_errors = {
        'missing_nutrientprofile_value': False,
        'nutrients_missing_nutrientprofile_value': [],
    }

    queryset_specificnutrienttarget_of_fulldayofeating = \
        specific_nutrient_target.objects.filter(
            fulldayofeating=id_fulldayofeating
        )

    specificnutrienttarget_list = \
        list(queryset_specificnutrienttarget_of_fulldayofeating.values(
            'nutrient_target'
            ))

    for dict_k in specificnutrienttarget_list:
        nutrient_target_name = dict_k['nutrient_target']
        if nutrientprofile_dict[nutrient_target_name] is None:
            nutrient_target_amount = 0
            targeted_nutrients_errors['missing_nutrientprofile_value'] = True
            targeted_nutrients_errors[
                'nutrients_missing_nutrientprofile_value'].append(
                nutrient_target_name
            )
        elif nutrientprofile_dict[nutrient_target_name] is not None:
            nutrient_target_amount = nutrientprofile_dict[nutrient_target_name]
        else:
            print('\n This case should not be possible.')
            print('Occured in query_specificnutrienttarget_'
                  'of_fulldayofeating. \n')
            return

        new_dict = {nutrient_target_name: nutrient_target_amount}
        # Because the tarteged_nutrients gets update with a new dictionary,
        # it does not matter if the users add calories twice as a
        # SpecificIngredient.
        targeted_nutrients.update(new_dict)

    # print('\n targeted_nutrients \n')
    # pprint.pprint(targeted_nutrients)

    return targeted_nutrients, targeted_nutrients_errors
