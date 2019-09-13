class CustomError(Exception):
    """Base class for exceptions in this module."""
    pass


class Step1Error(CustomError):
    """
    """
    pass


# ==============================================================================

# It should be at the highest level.

# Try query_input_and_calculate_fulldayofeating except and then make an
# except clause for every exception that can come up.

# ==============================================================================

try:

    # Calculate fulldayofeating.

    # Calculate step 1: get the nutrient profile
    nutrient_profile_is_valid = False
    if nutrient_profile_is_valid:
        result_step_1_is_valid = True
    else:
        result_step_1_is_valid = False
        raise Step1Error

    # If something went wrong (error_step_1), stop the calculation and show the
    # user the error page.

    # Calculate step 2.
    # If something went wrong (error_step_2), stop the calculation and show the
    # user the error page.

    # Calculate step 3.
    # If something went wrong (error_step_3), stop the calculation and show the
    # user the error page.

    # Return the result.

except Step1Error:
    print('Step1Error')

