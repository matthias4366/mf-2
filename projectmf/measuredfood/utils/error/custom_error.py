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


class NumberTargetedNutrientsNotEqualNumberScalingEntitiesError(Exception):
    """
    For the calculation of a full day of eating, it is necessary that the
    linear equation system is solvable. For this purpose, the number of
    targeted nutrients must equal the number of independently scaling
    ingredients or ingredient groups.
    """

    def __init__(
            self,
            n_targeted_nutrient,
            list_targeted_nutrient,
            n_independently_scaling_entity,
            list_independently_scaling_entity,

    ):
        self.n_targeted_nutrient = n_targeted_nutrient
        self.list_targeted_nutrient = list_targeted_nutrient
        self.n_independently_scaling_entity = n_independently_scaling_entity
        self.list_independently_scaling_entity = \
            list_independently_scaling_entity
