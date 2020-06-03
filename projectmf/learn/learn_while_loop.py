import pprint

n_iterations_max = 20
n = 0

specificingredient2_dict_template = [
    {
        'ingredient_name': None,
        'calculated_amount': None,
        'amount_is_variable': None,
        'is_positive': None,
        'max_amount': None,
        'is_lower_than_maximum': None,
        'min_amount': None,
        'is_higher_than_minimum_amount': None,
        'step_size': None,
        'is_multiple_of_step_size': None,
    },
]

specificingredient2_dict_list = [
    {
        'ingredient_name': '1 negative result',
        'calculated_amount': -12,
        'amount_is_variable': None,
        'is_positive': False,
        'max_amount': None,
        'is_lower_than_maximum': None,
        'min_amount': None,
        'is_higher_than_minimum_amount': None,
        'step_size': None,
        'is_multiple_of_step_size': None,
    },
    {
        'ingredient_name': '2 exceeds Maximum',
        'calculated_amount': 250,
        'amount_is_variable': None,
        'is_positive': None,
        'max_amount': 200,
        'is_lower_than_maximum': False,
        'min_amount': None,
        'is_higher_than_minimum_amount': None,
        'step_size': None,
        'is_multiple_of_step_size': None,
    },
    {
        'ingredient_name': '3 undercuts minimum',
        'calculated_amount': 73,
        'amount_is_variable': None,
        'is_positive': None,
        'max_amount': None,
        'is_lower_than_maximum': None,
        'min_amount': 100,
        'is_higher_than_minimum_amount': False,
        'step_size': None,
        'is_multiple_of_step_size': None,
    },
    {
        'ingredient_name': '4 not multiple of step size',
        'calculated_amount': 143,
        'amount_is_variable': None,
        'is_positive': None,
        'max_amount': None,
        'is_lower_than_maximum': None,
        'min_amount': None,
        'is_higher_than_minimum_amount': None,
        'step_size': 40,
        'is_multiple_of_step_size': False,
    },
]

while n < n_iterations_max:

    n += 1

    print(f"Iteration number {n}")
    print('specificingredient2_dict_list')
    pprint.pprint(specificingredient2_dict_list)

    # calculate_specificingredient2_amount_try

    calculated_amount_fullfill_all_criteria = True

    for specificingredient2_dict_k in specificingredient2_dict_list:
        if specificingredient2_dict_k['calculated_amount'] < 0:
            print('Calculated amount smaller than 0.')
            calculated_amount_fullfill_all_criteria = False
            specificingredient2_dict_k['calculated_amount'] = 0
            specificingredient2_dict_k['amount_is_variable'] = False
            specificingredient2_dict_k['is_positive'] = True
            continue
        else:
            specificingredient2_dict_k['is_positive'] = True

    if not calculated_amount_fullfill_all_criteria:
        continue

    for specificingredient2_dict_k in specificingredient2_dict_list:
        if specificingredient2_dict_k['max_amount'] is None:
            specificingredient2_dict_k['is_lower_than_maximum'] = True
        else:
            if specificingredient2_dict_k['calculated_amount'] > \
                    specificingredient2_dict_k['max_amount']:
                print('Calculated amount greater than maximum.')
                calculated_amount_fullfill_all_criteria = False
                specificingredient2_dict_k['calculated_amount'] = \
                    specificingredient2_dict_k['max_amount']
                specificingredient2_dict_k['is_lower_than_maximum'] = True
                continue
            else:
                specificingredient2_dict_k['is_lower_than_maximum'] = True

    if not calculated_amount_fullfill_all_criteria:
        continue

    for specificingredient2_dict_k in specificingredient2_dict_list:
        if specificingredient2_dict_k['min_amount'] is None:
            specificingredient2_dict_k['is_higher_than_minimum_amount'] = True
        else:
            if specificingredient2_dict_k['calculated_amount'] < \
                    specificingredient2_dict_k['min_amount']:
                print('Calculated amount less than minimum.')
                calculated_amount_fullfill_all_criteria = False
                specificingredient2_dict_k['calculated_amount'] = \
                    specificingredient2_dict_k['min_amount']
                specificingredient2_dict_k[
                    'is_higher_than_minimum_amount'] = True
                continue
            else:
                specificingredient2_dict_k[
                    'is_higher_than_minimum_amount'] = True

    if not calculated_amount_fullfill_all_criteria:
        continue

    for specificingredient2_dict_k in specificingredient2_dict_list:

        if specificingredient2_dict_k['step_size'] is None:
            specificingredient2_dict_k['is_multiple_of_step_size'] = True
            print('No step size is defined, all good.')
            continue

        tolerance = 0.01
        remainder = \
            specificingredient2_dict_k['calculated_amount'] \
            % specificingredient2_dict_k['step_size']
        print('remainder')
        print(remainder)
        relative_remainder = \
            remainder / specificingredient2_dict_k['calculated_amount']
        print('relative_remainder')
        print(relative_remainder)
        amount_is_multiple_of_step_size = \
            relative_remainder < tolerance

        # TODO: Continue here.

        if amount_is_multiple_of_step_size:
            specificingredient2_dict_k['is_multiple_of_step_size'] = True
            print('Calculated amount was multiple of step size.')
            continue

        if not amount_is_multiple_of_step_size:
            print('Calculated amount was not multiple of step size.')
            calculated_amount_fullfill_all_criteria = False
            r_floor_division = \
                specificingredient2_dict_k['calculated_amount'] \
                // specificingredient2_dict_k['step_size']
            print('r_floor_division')
            print(r_floor_division)
            difference_to_next_higher_step = \
                abs(
                    (r_floor_division+1)
                    * specificingredient2_dict_k['step_size']
                    - specificingredient2_dict_k['calculated_amount']
                )
            difference_to_next_lower_step = \
                abs(
                    r_floor_division
                    * specificingredient2_dict_k['step_size']
                    - specificingredient2_dict_k['calculated_amount']
                )
            r_is_closer_to_next_higher_step = \
                difference_to_next_higher_step \
                < difference_to_next_lower_step

            calculated_amount_fit_to_higher_step = \
                (r_floor_division + 1) \
                * specificingredient2_dict_k['step_size']
            calculated_amount_fit_to_lower_step = \
                r_floor_division \
                * specificingredient2_dict_k['step_size']

            if r_is_closer_to_next_higher_step:
                calculated_amount_fit_to_closest_step = \
                    calculated_amount_fit_to_higher_step
            else:
                calculated_amount_fit_to_closest_step = \
                    calculated_amount_fit_to_lower_step

            if specificingredient2_dict_k['round_step'] == 'round down':
                specificingredient2_dict_k['calculated_amount'] = \
                    calculated_amount_fit_to_lower_step
            elif specificingredient2_dict_k['round_step'] == 'closest value':
                specificingredient2_dict_k['calculated_amount'] = \
                    calculated_amount_fit_to_closest_step
            elif specificingredient2_dict_k['round_step'] == 'round up':
                specificingredient2_dict_k['calculated_amount'] = \
                    calculated_amount_fit_to_higher_step
            else:
                # This case should not be possible
                print('Invalid round_step property on SpecificIngredient2.')
                pass

            specificingredient2_dict_k['is_multiple_of_step_size'] = True
            continue

    if not calculated_amount_fullfill_all_criteria:
        continue

    # Check if all 4 criteria for correction are fullfilled. If so, exit the
    # while loop.

    if calculated_amount_fullfill_all_criteria:
        break

print('specificingredient2_dict_list')
pprint.pprint(specificingredient2_dict_list)

"""
while n < n_iterations_max and "Not all calculation results are valid.":
    
    calculate_specificingredient2_amount_try()
    
    go through the list of calculation results and check if a calculation 
    result is negative. If that is the case, set the calculated amount to 0, 
    the amount_is_variable property to False and go back to the start of the 
    while loop.
        use continue to get back to the start of the while loop
    
    if "all calculation results are valid"
        break out of the while loop
        
    For each specificingredient, add the following 4 properties to it:
    - is_positive
    - is_lower_than_maximum
    - is_higher_than_minimum_amount
    - is_multiple_of_step_size
    
"""