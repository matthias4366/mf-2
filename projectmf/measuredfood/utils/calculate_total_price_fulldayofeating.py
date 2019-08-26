def calculate_total_price_fulldayofeating(
    specificingredient_dict_list,
    pprint,
):

    # print('\n specificingredient_dict_list in calculate_total_price_fulldayofeating \n')
    # pprint.pprint(specificingredient_dict_list)

    # Initialize result values
    total_price = 0

    # It is assumed that all SpecificIngredients have the same currency.
    # The currency of the first SpecificIngredient will be displayed.
    total_price_currency = \
    specificingredient_dict_list[0]['raw_ingredient']\
    ['currency_of_price_per_reference_amount']

    # The bad case was chosen as the default to make the application more
    # secure.
    # Put, from a programming perspective, it makes more sense to start with
    # False. It is enough for one ingredient to not have price data to make
    # it True.
    total_price_possibly_higher = False

    for specificingredient_dict_k in specificingredient_dict_list:

        # Check if there is a value for the price.
        # It is assumed that a price of 0 can not be valid.
        # TODO: the user needs to be told that.

        price_is_valid = \
        (specificingredient_dict_k\
        ['raw_ingredient']['price_per_reference_amount'] is not None) and\
        (specificingredient_dict_k\
        ['raw_ingredient']['price_per_reference_amount'] != 0)

        if price_is_valid:
            total_price = total_price +\
            specificingredient_dict_k['calculated_amount']\
            / specificingredient_dict_k['raw_ingredient']['reference_amount']\
            * specificingredient_dict_k['raw_ingredient']['price_per_reference_amount']
        elif not price_is_valid:
            total_price_possibly_higher = True
        else:
            print('\n Something went wrong, this case should not be possible.')
            print('Location in code: calculate_total_price_fulldayofeating. \n')

    total_price_rounded = round(total_price, 2)



    # Write the code before this line

    total_price_fulldayofeating_result_dict = {
        'total_price': total_price,
        'total_price_rounded': total_price_rounded,
        'total_price_currency': total_price_currency,
        'total_price_possibly_higher': total_price_possibly_higher,
    }

    # print('\n total_price_fulldayofeating_result_dict in calculate_total_price_fulldayofeating \n')
    # pprint.pprint(total_price_fulldayofeating_result_dict)

    return total_price_fulldayofeating_result_dict
