# import pprint


def calculate_specificingredient2_amount_try(
    all_nutrients_and_default_units,
    set_to_zero_if_none,
    # in the old code, this is called specificingredient_scalingoption_fixed
    specificingredient2_list_fixed,
    specificingredient2_dict_list,
    nutrientprofile_dict,
    copy,
    np,
):
    """
    Try to calculate the amounts of the SpecificIngredient2 objects. This
    function will be run multiple times.
    :return:
    """

    # Calculate the nutrition already present in the FullDayOfEating2 because
    # of the SpecificIngredient2 objects whose amounts are not variable.
    fulldayofeating_nutrition_so_far = {}
    for nutrient_dict in all_nutrients_and_default_units:
        nutrient_field_name = nutrient_dict['nutrient_name_measuredfood']
        fulldayofeating_nutrition_so_far.update(
            {nutrient_field_name: 0}
        )

    # print('specificingredient2_list_fixed')
    # pprint.pprint(specificingredient2_list_fixed)

    for dict_k in specificingredient2_list_fixed:
        for nutrient_dict in all_nutrients_and_default_units:
            nutrient_field_name = nutrient_dict['nutrient_name_measuredfood']
            if dict_k['raw_ingredient'][nutrient_field_name] is None:
                dict_k['raw_ingredient'][nutrient_field_name] = 0
            fulldayofeating_nutrition_so_far[nutrient_field_name] = \
                fulldayofeating_nutrition_so_far[nutrient_field_name]\
                + float(dict_k['base_amount']) \
                / float(dict_k['raw_ingredient']['reference_amount']) \
                * set_to_zero_if_none(
                    dict_k['raw_ingredient'][nutrient_field_name]
                )

    # print('fulldayofeating_nutrition_so_far')
    # pprint.pprint(fulldayofeating_nutrition_so_far)

    # Set up b for the linalg solver, i.e.

    # Rebuild the targeted_nutrients exactly as they were in the old code (
    # calculate_fulldayofeating). The coupling of ingredients to a nutrient
    # target is not relevant at this point. It is relevant later,
    # when SpecificIngredient2 objects are removed from the calculation,
    # and the nutrient target is removed with them.

    targeted_nutrients = {}

    for specificingredient2_k in specificingredient2_dict_list:
        if specificingredient2_k['nutrient_target'] is not None:
            if specificingredient2_k['nutrient_target'] not in \
                    targeted_nutrients:
                targeted_nutrient_daily_amount = \
                    nutrientprofile_dict[
                        specificingredient2_k['nutrient_target']
                    ]
                targeted_nutrients.update(
                    {
                        specificingredient2_k['nutrient_target']:
                        targeted_nutrient_daily_amount
                    }
                )

    # print('targeted_nutrients in 2')
    # print(targeted_nutrients)

    # calculate the remaining amounts that need to be filled for each
    # targeted nutrient.
    # E.g., the Energy (kcal) target is 2500 and the non
    # variable SpecificIngredient2 already provide 1000 kcal. There are
    # 1500 kcal remaining that need to be filled with the variable
    # SpecificIngredient2.

    # For the targeted nutrients, calculate the remaining values.
    targeted_nutrients_remainder = copy.deepcopy(targeted_nutrients)
    for key_k in targeted_nutrients:
        targeted_nutrients_remainder[key_k] = \
            targeted_nutrients[key_k] \
            - fulldayofeating_nutrition_so_far[key_k]
        # It's okay if some results are negative. Then, some ingredient
        # amounts will be negative later on. Then, the ingredient amount will
        # be set to zero and the SpecificIngredient2 will be set to
        # non-variable.

    # Prepare the arrays for the linear equation solver.
    b = []
    for key_k in targeted_nutrients_remainder:
        b.append(targeted_nutrients_remainder[key_k])
    b = np.asarray(b)

    print('b in 2')
    print(b)

    return None
