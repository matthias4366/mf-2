

def query_specificnutrienttarget_of_fulldayofeating(
    id_fulldayofeating,
    specific_nutrient_target,
    nutrientprofile_dict,
    no_value_for_targeted_nutrient_error,
):

    # Initialize result.
    targeted_nutrients = {}

    queryset_specificnutrienttarget_of_fulldayofeating = \
        specific_nutrient_target.objects.filter(
            fulldayofeating=id_fulldayofeating
        )

    specificnutrienttarget_list = \
        list(queryset_specificnutrienttarget_of_fulldayofeating.values(
            'nutrient_target'
            ))

    nutrient_without_value_in_nutrientprofile = []

    for dict_k in specificnutrienttarget_list:
        nutrient_target_name = dict_k['nutrient_target']
        if nutrientprofile_dict[nutrient_target_name] is None:

            nutrient_without_value_in_nutrientprofile.append(
                nutrient_target_name
            )

            nutrient_target_amount = None
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

    # Raise the error outside the for loop so all nutrients for which there
    # is no value in the nutrient profile are collected.

    if len(nutrient_without_value_in_nutrientprofile) > 0:
        raise (no_value_for_targeted_nutrient_error(
            nutrient_without_value_in_nutrientprofile
        ))

    return targeted_nutrients
