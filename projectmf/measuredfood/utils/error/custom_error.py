class CustomError(Exception):
    """Base class for exceptions in this module."""
    pass


class UserIsNotAuthorError(CustomError):
    """
    The User is trying to access another user's object. Access is to be
    denied and an explanatory error message is to be displayed.
    """
    pass


class NoSpecificIngredientInFullDayOfEatingError(CustomError):
    """
    The User has created a FullDayOfEating but has not added a single
    SpecificIngredient.
    """

    def __init__(self):
        # self.expression = expression
        self.message = 'Before attempting to calculate a FullDayOfEating, ' \
                       'the User must add at least one SpecificIngredient.'

