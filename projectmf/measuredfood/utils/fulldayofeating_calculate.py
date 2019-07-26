def calculate_fulldayofeating(
    id_fulldayofeating,
    SpecificIngredient,
    FullDayOfEating,
    NutrientProfile,
    RawIngredient,
    pprint,
    copy,
    INGREDIENT_FIELDS_NUTRITION,
    np
    ):
    """
    This function should be independent of everything else.
    It should be a PURE function, i.e. work solely with inputs and outputs.
    It is given an id_fulldayofeating. Based on that, it retrieves the
    SpecificIngredients belonging to that FullDayOfEating and the
    NutrientProfile. It then calculates the final amounts and saves them to the
    fields "calculated_amount".

    Calculate the fulldayofeating, i.e. calculate the calculated_amount
    values for the SpecificIngredient instances associated with a
    FullDayOfEating, which is associated with a NutrientProfile.
    """

    """
    Query the related SpecificIngredients and store the results in dictionaries.
    """
    queryset_specificingredient_0 = SpecificIngredient.objects.filter(
        fulldayofeating_id=id_fulldayofeating
        )
    queryset_specificingredient_1 = SpecificIngredient.objects.filter(
        fulldayofeating_id=id_fulldayofeating
        )

    # 0 is not to be changed.
    specificingredient_dict_list_0 = list(
        queryset_specificingredient_0.values()
        )

    # 1 will be used for calculations, i.e. the fixed values will be removed.
    specificingredient_dict_list_1 = list(
        queryset_specificingredient_1.values()
        )

    # Add the RawIngredient dictionaries to the SpecificIngredient dictionaries
    # to make the nutrition values (kcal etc.) accessible for calculation.
    for k in range(len(specificingredient_dict_list_1)):
        rawingredient_k_queryset = RawIngredient.objects.filter(
            id = specificingredient_dict_list_1[k]['rawingredient_id']
        ).values()
        rawingredient_k_dict = list(rawingredient_k_queryset)[0]
        specificingredient_dict_list_1[k].update(
            raw_ingredient = rawingredient_k_dict
            )

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
    # print('\nnutrientprofile_dict \n')
    # pprint.pprint(nutrientprofile_dict)

    # Collect all the nutrition goals that are actually targeted.
    targeted_nutrients = {}
    for nutrient_field_name in INGREDIENT_FIELDS_NUTRITION:
        if nutrientprofile_dict[nutrient_field_name+'_is_targeted']:
            targeted_nutrients.update(
                {nutrient_field_name: nutrientprofile_dict[nutrient_field_name]}
            )
    # print('\ntargeted_nutrients \n')
    # pprint.pprint(targeted_nutrients)

    """
    Iterate through the dictionaries representing the SpecificIngredients
    and sort them by their 'scaling_option' property.
    """
    specificingredient_scalingoption_fixed = []
    specificingredient_scalingoption_independent = []

    # Create a dictionary where the keys are the group names and the fields
    # are lists of SpecificIngredients as dictionaries belonging to that group.
    specificingredient_scalingoption_group_dict = {}

    counter_added_to_existing_group = 0

    for dict_k in specificingredient_dict_list_1:
        if dict_k['scaling_option'] == 'FIXED':
            specificingredient_scalingoption_fixed.append(dict_k)
        elif dict_k['scaling_option'] == 'INDEPENDENT':
            specificingredient_scalingoption_independent.append(dict_k)
        elif len(dict_k['scaling_option']) == 1:
            # If the group already exists in
            # specificingredient_scalingoption_group_dict, add dict_k to it.
            if dict_k['scaling_option'] in specificingredient_scalingoption_group_dict:
                # Check that the new SpecificIngredient has the same units as
                # the first SpecificIngredient in the group.
                if dict_k['base_amount_unit'] == \
                specificingredient_scalingoption_group_dict[
                                    dict_k['scaling_option']
                                    ][0]['base_amount_unit']:
                    specificingredient_scalingoption_group_dict[
                        dict_k['scaling_option']
                        ].append(dict_k)
                else:
                    # TODO: Make this into a proper error message and show it
                    # to the user.
                    print('\nERROR: All specific ingredients belonging to the'\
                           ' same group'\
                          ' must have the same units.\n')
                    return None
            # If the group does not exist
            # specificingredient_scalingoption_group_dict, create it an add
            # dict_k to it.
            else:
                specificingredient_scalingoption_group_dict.update(
                    {dict_k['scaling_option'] : [dict_k]}
                    )
        else:
            # This case is impossible, since the user is only presented
            # with valid selections for the scaling_option. It's still good
            # practice to have this piece of code.
            print('\nERROR. The value given for scaling_group option was' \
                  ' not valid.\n')
            return None

    # print('\n specificingredient_scalingoption_fixed')
    # pprint.pprint(specificingredient_scalingoption_fixed)
    # print('\n specificingredient_scalingoption_independent')
    # pprint.pprint(specificingredient_scalingoption_independent)
    # print('\n specificingredient_scalingoption_group_dict')
    # pprint.pprint(specificingredient_scalingoption_group_dict)

    list_averaged_specificingredients = calculate_average_of_specificingredient_group(
        INGREDIENT_FIELDS_NUTRITION,
        specificingredient_scalingoption_group_dict,
        copy,
        pprint,
        targeted_nutrients
    )
    print('\n list_averaged_specificingredients \n')
    pprint.pprint(list_averaged_specificingredients)

    # group the averaged SpecificIngredients together with the
    # SpecificIngredients whose scaling_option was set to independent.
    list_independently_scaling_entities = []
    list_independently_scaling_entities.extend(
        specificingredient_scalingoption_independent
        )
    list_independently_scaling_entities.extend(
        list_averaged_specificingredients
        )
    # print('\n list_independently_scaling_entities \n')
    # pprint.pprint(list_independently_scaling_entities)

    # Initialize fulldayofeating_nutrition_so_far
    fulldayofeating_nutrition_so_far = {}
    for nutrient_field_name in INGREDIENT_FIELDS_NUTRITION:
        fulldayofeating_nutrition_so_far.update(
            {nutrient_field_name: 0}
        )
    # print('\n fulldayofeating_nutrition_so_far \n')
    # pprint.pprint(fulldayofeating_nutrition_so_far)

    # Sum up the nutrition from the SpecificIngredients with the scaling_option
    # set to 'FIXED'.
    for dict_k in specificingredient_scalingoption_fixed:
         for nutrient_field_name in INGREDIENT_FIELDS_NUTRITION:
             if dict_k['raw_ingredient'][nutrient_field_name] == None:
                 dict_k['raw_ingredient'][nutrient_field_name] = \
                 0
             fulldayofeating_nutrition_so_far[nutrient_field_name]=\
             fulldayofeating_nutrition_so_far[nutrient_field_name]\
             + dict_k['base_amount'] \
             / dict_k['raw_ingredient']['reference_amount_g'] \
             * dict_k['raw_ingredient'][nutrient_field_name]
    # print('\n fulldayofeating_nutrition_so_far \n')
    # pprint.pprint(fulldayofeating_nutrition_so_far)

    # For the targeted nutrients, calculate the remaining values.
    targeted_nutrients_remainder = copy.deepcopy(targeted_nutrients)
    for key_k in targeted_nutrients:
        targeted_nutrients_remainder[key_k] = \
        targeted_nutrients[key_k] \
        - fulldayofeating_nutrition_so_far[key_k]
        # Check if the 'FIXED' SpecificIngredients already run over the
        # nutrition goal.
        if targeted_nutrients_remainder[key_k] <= 0:
            print('ERROR: The ingredients with the \'FIXED\' scaling_options '\
                  'already provide too much nutrition.')
            return None
    # print('\n targeted_nutrients_remainder \n')
    # pprint.pprint(targeted_nutrients_remainder)

    # Prepare the arrays for the linear equation solver.
    b = []
    for key_k in targeted_nutrients_remainder:
        b.append(targeted_nutrients_remainder[key_k])
    b = np.asarray(b)
    print('\nb \n')
    pprint.pprint(b)

    a = np.zeros(shape=(len(b),len(b)))
    column_index = 0
    for dict_k in list_independently_scaling_entities:
        row_index = 0
        for key_k in targeted_nutrients_remainder:
            a[row_index][column_index] = dict_k['raw_ingredient'][key_k]
            row_index = row_index + 1
        column_index = column_index + 1
    print('\na \n')
    pprint.pprint(a)

    # Solve the linear equation.
    x = np.linalg.solve(a, b)
    print('\nx \n')
    pprint.pprint(x)

    # Multiply the entries in x with the reference_amount_g of each
    # SpecificIngredient
    print('\n list_independently_scaling_entities \n')
    pprint.pprint(list_independently_scaling_entities)

    """
    Return the values to make this a PURE function
    """
    # return

def calculate_average_of_specificingredient_group(
    INGREDIENT_FIELDS_NUTRITION,
    specificingredient_scalingoption_group_dict,
    copy,
    pprint,
    targeted_nutrients
):
    """
    For each group of ingredients, create an average ingredient representing
    the group. Use the base_amounts to set the ratios.
    """

    # Add all the averaged ingredients to a list.
    list_averaged_specificingredients = []

    for key_k in specificingredient_scalingoption_group_dict:
        group_k = specificingredient_scalingoption_group_dict[key_k]
        # Create an initial state for the averaged_specificingredient. Start from the
        # first SpecificIngredient dict in the list.
        # Make a copy.
        averaged_specificingredient_initial = copy.deepcopy(group_k[0])
        # Simply ignore the unimportant fields, no need to remove them.
        # Set the values of the remaining fields to None.
        for key_l in averaged_specificingredient_initial['raw_ingredient']:
            averaged_specificingredient_initial['raw_ingredient'][key_l] = \
            0
        # print('\n averaged_specificingredient_initial \n')
        # pprint.pprint(averaged_specificingredient_initial)

        # Name the averaged ingredient using the group name.
        averaged_specificingredient = copy.deepcopy(averaged_specificingredient_initial)
        averaged_specificingredient['raw_ingredient']['name'] = \
        'average_group_' + key_k
        # print('\n averaged_specificingredient \n')
        # pprint.pprint(averaged_specificingredient)

        # Average the SpecificIngredients in group_k

        # Initialise the sum of the base_amounts
        total_base_amount = 0
        for m in range(len(group_k)):
            total_base_amount = total_base_amount + group_k[m]['base_amount']
        # Add the total base amount to the averaged_specificingredient
        # so it is available later when it is needed.
        averaged_specificingredient['total_base_amount'] = total_base_amount
        # print('\n type_total_base_amount \n')
        # print(type(total_base_amount))

        # Go through the SpecificIngredients belonging to a certain group
        # and add them to the averaged_specificingredient.
        for m in range(len(group_k)):
            for nutrient_field_name in INGREDIENT_FIELDS_NUTRITION:
                # Change field values to supported values, i.e. None to 0.
                if group_k[m]['raw_ingredient'][nutrient_field_name] == None:
                    group_k[m]['raw_ingredient'][nutrient_field_name] = \
                    0
                averaged_specificingredient['raw_ingredient'][nutrient_field_name] = \
                averaged_specificingredient['raw_ingredient'][nutrient_field_name] \
                + (group_k[m]['base_amount'] / total_base_amount) \
                * group_k[m]['raw_ingredient'][nutrient_field_name]

            # print('\nm\n')
            # print(m)
            # print('\n averaged_specificingredient \n ')
            # pprint.pprint(averaged_specificingredient)

        # Add all the averaged ingredients to a list.
        list_averaged_specificingredients.append(averaged_specificingredient)

    return list_averaged_specificingredients
