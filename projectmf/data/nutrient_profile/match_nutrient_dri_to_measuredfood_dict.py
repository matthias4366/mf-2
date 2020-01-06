# Map the nutrient names from the dataframe which was made from
# daily_recommended_intake.xlsx to the nutrient name as it is
# stored in measuredfood.
# For example "Calcium\n(mg/d)" in the dataframe maps to
# "calcium_ca-name-1087-id" in the measuredfood app.

# The matching_name_in_measuredfood is the respective name of the nutrients
# under which it is stored in the measuredfood database.
# The unit_conversion_factor is used for the following calculation:
# amount_in_measuredfooddatabase = unit_conversion_factor * amount_in_dri
match_nutrient_dri_to_measuredfood_dict = {
    'Arsenica':
        {
            'matching_name_in_measuredfood': None,
            'unit_conversion_factor': 1,
        },
    'Boron\n(mg/d)':
        {
            'matching_name_in_measuredfood': 'boron_b-name-1137-id',
            'unit_conversion_factor': 1/1000,
        },
    'Calcium\n(mg/d)':
        {
            'matching_name_in_measuredfood': 'calcium_ca-name-1087-id',
            'unit_conversion_factor': 1,
        },
    # Chromium
    # Copper
    # (μg/d)
    # Fluoride
    # (mg/d)
    # Iodine
    # (μg/d)
    # Iron
    # (mg/d)
    # Magnesium
    # (mg/d)b
    # Manganese
    # (mg/d)
    # Molybdenum
    # (μg/d)
    # Nickel
    # (mg/d)
    # Phosphorus
    # (g/d)
    # Selenium
    # (μg/d)
    # Siliconc
    # Vanadium
    # (mg/d)d
    # Zinc
    # (mg/d)
    # Sodium
    # (g/d)
    # Chloride
    # (g/d)
}
