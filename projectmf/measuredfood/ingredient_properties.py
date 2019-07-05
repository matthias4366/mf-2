import copy

# I am using https://nutritiondata.self.com
# as a model for the all the information that goes into the ingredients.

# INGREDIENT_FIELDS_NUTRITION. Names of the fields of the RawIngredient model.
# These names are related to fields related to the nutritional values.
# Do not fill this out with everything from nutritiondata.self.com. It will
# be changed later anyways.
INGREDIENT_FIELDS_NUTRITION = [
    'calories_kcal',
    # The 'calories from fat' etc. stuff is redundant.
    'total_carbohydrates_g',
    'dietary_fiber_g',
    'starch_g',
    'sugars_g',
    'total_fat_g',
    'saturated_fat_g',
    'monounsaturated_fat_g',
    'polyunsaturated_fat_g',
    'total_trans_fatty_acids_g',
    'total_omega_3_fatty_acids_mg',
    'total_omega_6_fatty_acids_mg',
    'protein_g',
    # Vitamins
    'vitamin_a_iu',
    'vitamin_c_mg',
    'vitamin_d_iu',
    'vitamin_e_alpha_tocopherol_mg',
    'vitamin_k_mcg',
    'thiamin_mg',
    'riboflavin_mg',
    'niacin_mg',
    'vitamin_b6_mg',
    'folate_mcg',
    'vitamin_b12_mcg',
    'pantothenic_acid_mg',
    'choline_mg',
    'betaine_mg',
    # Minerals
    'calcium_mg',
    'iron_mg',
    'magnesium_mg',
    'phosphorus_mg',
    'potassium_mg',
    'sodium_mg',
    'zinc_mg',
    'copper_mg',
    'manganese_mg',
    'selenium_mcg',
    'fluoride_mcg',
    # Sterols
    'cholesterol_mg',
    'phytosterols',
    # Other
    'alcohol_g',
    'water_g',
    'ash_g',
    'caffeine_mg',
    'theobromine_mg'
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
