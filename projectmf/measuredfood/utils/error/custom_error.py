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


class CalculationResultIsNegativeError(Exception):
    """
    In the calculation of a full day of eating, it is possible to get
    negative results. For example, if the targets are 10,000 kcal and 10 g of
    protein and the independently scaling ingredients are beans and pea
    protein powder. Filling in the 10,000 kcal with beans already provides
    much more than 10 g of protein. Hence, the result for the pea protein
    powder will be negative, because that is the only way to get back down to
    the targeted amount of 10 g. Negative masses are not physically possible
    and hence the user must be advised on what went wrong and how to proceed.
    """

    def __init__(self, list_ingredient_negative_result):
        self.list_ingredient_negative_result = \
            list_ingredient_negative_result


class FixedIngredientExceedsNutrientProfileValueError(Exception):
    """
    For the calculation of a full day of eating to be possible, the linear
    equation system must be solveable without producing negative results.
    One error case that would produce negative results is that the fixed
    ingredients already provide nutrition in excess of the values stored in
    the nutrient profile. For example: someone adds 1000 g of bacon to a
    recipe with the scaling option 'fixed', adds eggs with a scaling option
    of 'indepent' and has a fat target of 70 g. It is not possible to add a
    positive amount of eggs so that the total fat amount gets to 70 g.
    """
    pass
