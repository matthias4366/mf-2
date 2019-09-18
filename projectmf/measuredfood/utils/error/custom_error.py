class CustomError(Exception):
    """Base class for exceptions in this module."""
    pass


class UserIsNotAuthorError(CustomError):
    """
    The User is trying to access another user's object. Access is to be
    denied and an explanatory error message is to be displayed.
    """
    pass


class NoSpecificIngredientInFullDayOfEatingError(Exception):
    """
    The User has created a FullDayOfEating but has not added a single
    SpecificIngredient.
    """
    pass

    # def __init__(self, *args):
    #     self.args = args


class NoValueForTargetedNutrientError(Exception):
    """
    When a nutrient is targeted for the calculation of the full day of
    eating, there must exist a value for that nutrient in the nutrient
    profile. If there is not, this error is thrown.
    """

    def __init__(self, nutrient_value_missing):
        self.nutrient_value_missing = nutrient_value_missing
