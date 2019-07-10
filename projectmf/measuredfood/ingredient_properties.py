import copy

# I am using www.completefoods.co
# as a model for the all the information that goes into the ingredients.
INGREDIENT_FIELDS_NUTRITION_COMPLETEFOODS = [
    'calories_kcal',
    'carbohydrates_g',
    'protein_g',
    'total_fat_g',
    'saturated_fat_g',
    'monounsaturated_fat_g',
    'polyunsaturated_fat_g',
    'omega_3_fatty_acids_g',
    'omega_6_fatty_acids_g',
    'total_fiber_g',
    'soluble_fiber_g',
    'insoluble_fiber_g',
    'cholesterol_mg',
    # vitamins
    'vitamin_A_iu',  # check
    'vitamin_b6_mg',  # check
    'vitamin_b12_ug',  #check
    'vitamin_c_mg',  # check
    'vitamin_d_IU',  # check
    'vitamin_e_iu',  # check
    'vitamin_k_ug',  # check
    'thiamin_mg',  # check
    'riboflavin_mg',  # check
    'niacin_mg',  # check
    'folate_ug',  # check
    'pantothenic_acid_mg'  # check
    'biotin_ug',  # added to missing
    'choline_mg',  # added to missing
    # minerals
    'calcium_g',  # check
    'chloride_g',  # added to missing
    'chromium_ug',  # added to missing
    'copper_mg',  # check
    'iodine_ug',  # added to missing
    'iron_mg',  # check
    'magnesium_mg',  # check
    'manganese_mg',  # check
    'molybdenum_ug',  # check
    'phosphorus_g',  # check
    'potassium_g',  # check
    'selenium_ug',  # check
    'sodium_g',  # check
    'sulfur_g',  # added to missing
    'zinc_mg'  # check
]


# INGREDIENT_FIELDS_NUTRITION. Names of the fields of the RawIngredient model.
# These names are related to fields related to the nutritional values.
INGREDIENT_FIELDS_NUTRITION_NUTRITION_DATA = [
    'calories_kcal',
    # The 'calories from fat' etc. stuff is redundant.
    'total_carbohydrates_g',
    'dietary_fiber_g',
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
    # Sterols
    'cholesterol_mg',
]

INGREDIENT_FIELDS_NUTRITION_MISSING_FROM_NUTRITION_DATA = [
    'biotin_ug',
    'choline_mg',
    'chloride_g',
    'chromium_ug',
    'iodine_ug',
    'molybdenum_ug',
    'sulfur_g',
]

INGREDIENT_FIELDS_NUTRITION = INGREDIENT_FIELDS_NUTRITION_NUTRITION_DATA \
    + INGREDIENT_FIELDS_NUTRITION_MISSING_FROM_NUTRITION_DATA

# INGREDIENT_FIELDS_SCALING_PROPERTIES: Ingredients is the basic model,
# i.e. RawIngredient. Of that model, some field names are defined. This variable
# defines the names for the fields with properties that scale with the amount
# of the ingredient.
INGREDIENT_FIELDS_SCALING_PROPERTIES = copy.deepcopy(
    INGREDIENT_FIELDS_NUTRITION
)
INGREDIENT_FIELDS_SCALING_PROPERTIES.append(
    # Price of the ingredient per reference amount
    'price_eur_per_reference_amount'
)

INGREDIENT_FIELDS_NUMBERS = copy.deepcopy(
    INGREDIENT_FIELDS_SCALING_PROPERTIES
)
INGREDIENT_FIELDS_NUMBERS.append(
    # Reference amount to which all the nutrition amounts related, e.g.
    # 370 kcal / 100 g => 100 is the reference amount.
    'reference_amount_g'
)
INGREDIENT_FIELDS_NUMBERS.append(
    'amount_in_package_g'
)

# This variable does not include the 'name' field, which can't be empty.
INGREDIENT_FIELDS_LINKS = [
    'buy_here_link',
    'source_nutritional_information_link'
]

INGREDIENT_FIELDS_ALL = ['name'] \
    + INGREDIENT_FIELDS_NUMBERS\
    + INGREDIENT_FIELDS_LINKS
