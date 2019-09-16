class CustomError(Exception):
    """Base class for exceptions in this module."""
    pass


class UserIsNotAuthorError(CustomError):
    """
    The User is trying to access another user's object. Access is to be
    denied and an explanatory error message is to be displayed.
    """
    pass
