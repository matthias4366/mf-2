import copy

ALL_INGREDIENT_FIELD_NAMES = [
    'name',
    'calories',
    'fat',
    'protein',
    'carbohydrates'
]


# TODO interim code. Apply or delete.
INGREDIENT_ATTRIBUTE_NAMES = [
    'calories',
    'fat',
    'protein',
    'carbohydrates',
    'magnesium'
]


# INGREDIENT_FIELDS_NUTRITION. Names of the fields of the RawIngredient model.
# These names are related to fields related to the nutritional values.
INGREDIENT_FIELDS_NUTRITION = [
    'calories',
    'fat',
    'protein',
    'carbohydrates',
    'magnesium'
]

# INGREDIENT_FIELDS_SCALING_PROPERTIES: Ingredients is the basic model,
# i.e. RawIngredient. Of that model, some field names are defined. This variable
# defines the names for the fields with properties that scale with the amount
# of the ingredient.
INGREDIENT_FIELDS_SCALING_PROPERTIES = copy.deepcopy(
    INGREDIENT_FIELDS_NUTRITION
)
INGREDIENT_FIELDS_SCALING_PROPERTIES.append(
    # Price of the ingredient per reference amount
    'price'
)

INGREDIENT_FIELDS_NUMBERS = copy.deepcopy(
    INGREDIENT_FIELDS_SCALING_PROPERTIES
)
INGREDIENT_FIELDS_NUMBERS.append(
    # Reference amount to which all the nutrition amounts related, e.g.
    # 370 kcal / 100 g => 100 is the reference amount.
    'reference_amount'
)
INGREDIENT_FIELDS_NUMBERS.append(
    'amount_in_package'
)

# This variable does not include the 'name' field, which can't be empty.
INGREDIENT_FIELDS_STRINGS = [
    'where_to_buy',
    'source_nutritional_information'
]

INGREDIENT_FIELDS_ALL = ['name'] \
    + INGREDIENT_FIELDS_NUMBERS\
    + INGREDIENT_FIELDS_STRINGS
