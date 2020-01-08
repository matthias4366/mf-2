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
            'unit_conversion_factor': 1000,
        },
    'Calcium (mg/d)':
        {
            'matching_name_in_measuredfood': 'calcium_ca-name-1087-id',
            'unit_conversion_factor': 1,
        },
    'Chromium (μg/d)':
        {
            'matching_name_in_measuredfood': 'chromium_cr-name-1096-id',
            'unit_conversion_factor': 1,
        },
    'Copper (μg/d)':
        {
            'matching_name_in_measuredfood': 'copper_cu-name-1098-id',
            'unit_conversion_factor': 1/1000,
        },
    'Fluoride (mg/d)':
        {
            'matching_name_in_measuredfood': 'fluoride_f-name-1099-id',
            'unit_conversion_factor': 1/1000,
        },
    'Iodine (μg/d)':
        {
          'matching_name_in_measuredfood': 'iodine_i-name-1100-id',
          'unit_conversion_factor': 1,
        },
    'Iron (mg/d)':
        {
            'matching_name_in_measuredfood': 'iron_fe-name-1089-id',
            'unit_conversion_factor': 1,
        },
    'Magnesium (mg/d)':
        {
            'matching_name_in_measuredfood': 'magnesium_mg-name-1090-id',
            'unit_conversion_factor': 1,
        },
    'Manganese (mg/d)':
        {
            'matching_name_in_measuredfood': 'manganese_mn-name-1101-id',
            'unit_conversion_factor': 1,
        },
    'Molybdenum (μg/d)':
        {
            'matching_name_in_measuredfood': 'molybdenum_mo-name-1102-id',
            'unit_conversion_factor': 1,
        },
    'Phosphorus (mg/d)':
        {
            'matching_name_in_measuredfood': 'phosphorus_p-name-1091-id',
            'unit_conversion_factor': 1,
        },
    'Selenium (μg/d)':
        {
            'matching_name_in_measuredfood': 'selenium_se-name-1103-id',
            'unit_conversion_factor': 1,
        },
    'Zinc (mg/d)':
        {
            'matching_name_in_measuredfood': 'zinc_zn-name-1095-id',
            'unit_conversion_factor': 1,
        },
    'Potassium (g/d)':
        {
            'matching_name_in_measuredfood': 'potassium_k-name-1092-id',
            'unit_conversion_factor': 1000,
        },
    'Sodium (g/d)':
        {
            'matching_name_in_measuredfood': 'sodium_na-name-1093-id',
            'unit_conversion_factor': 1000,
        },
    'Chloride (g/d)':  # checked unit_conversion_factor for dri and max until
    # here.
        {
            'matching_name_in_measuredfood': 'chlorine_cl-name-1088-id',
            'unit_conversion_factor': 1000,
        },
    'Vitamin A (μg/d)a':
        {
            'matching_name_in_measuredfood': 'vitamin_a_iu-name-1104-id',
            'unit_conversion_factor': 1/0.3,
        },
    'Vitamin C (mg/d)':
        {
            'matching_name_in_measuredfood':
                'vitamin_c_total_ascorbic_acid-name-1162-id',
            'unit_conversion_factor': 1,
        },
    'Vitamin D (μg/d)b,c':
        {
            'matching_name_in_measuredfood': 'vitamin_d-name-1110-id',
            'unit_conversion_factor': 40,
        },
    'Vitamin E (mg/d)d':
        {
            'matching_name_in_measuredfood':
                'vitamin_e_(label_entry_primarily)-name-1124-id',
            'unit_conversion_factor': 2.22,
            # Source:
            # https://ods.od.nih.gov/factsheets/VitaminE-HealthProfessional/
        },
    'Vitamin K (μg/d)':
        {
            'matching_name_in_measuredfood':
                'vitamin_k_(phylloquinone)-name-1185-id',
            'unit_conversion_factor': 1,
        },
    'Thiamin (mg/d)':
        {
            'matching_name_in_measuredfood': 'thiamin-name-1165-id',
            'unit_conversion_factor': 1,
        },
    'Riboflavin (mg/d)':
        {
            'matching_name_in_measuredfood': 'riboflavin-name-1166-id',
            'unit_conversion_factor': 1,
        },
    'Niacin (mg/d)e':
        {
            'matching_name_in_measuredfood': 'niacin-name-1167-id',
            'unit_conversion_factor': 1,
        },
    'Vitamin B6 (mg/d)':
        {
            'matching_name_in_measuredfood': 'vitamin_b-6-name-1175-id',
            'unit_conversion_factor': 1,
        },
    'Folate (μg/d)f':
        {
            'matching_name_in_measuredfood': 'folate_total-name-1177-id',
            'unit_conversion_factor': 1,
        },
    'Vitamin B12 (μg/d)':
        {
            'matching_name_in_measuredfood': 'vitamin_b-12-name-1178-id',
            'unit_conversion_factor': 1,
        },
    'Pantothenic Acid (mg/d)':
        {
            'matching_name_in_measuredfood': 'pantothenic_acid-name-1170-id',
            'unit_conversion_factor': 1,
        },
    'Biotin (μg/d)':
        {
            'matching_name_in_measuredfood': 'biotin-name-1176-id',
            'unit_conversion_factor': 1,
        },
    'Choline (mg/d)g':
        {
            'matching_name_in_measuredfood': 'choline_total-name-1180-id',
            'unit_conversion_factor': 1,
        },
    'Total Watera (L/d)':
        {
            'matching_name_in_measuredfood': None,
            'unit_conversion_factor': 1,
        },
    'Carbohydrate (g/d)':
        {
            'matching_name_in_measuredfood':
                'carbohydrate_without_fiber-name-1-id',
            'unit_conversion_factor': 1,
        },
    'Total Fiber (g/d)':
        {
            'matching_name_in_measuredfood': 'fiber_total_dietary-name-1079-id',
            'unit_conversion_factor': 1,
        },
    'Fat (g/d)':
        {
            'matching_name_in_measuredfood': 'total_lipid_(fat)-name-1004-id',
            'unit_conversion_factor': 1,
        },
    # Linoleic acid is the essential omega 6 fatty acid, according to wikipedia
    # https://en.wikipedia.org/wiki/Linoleic_acid.
    # Other names:
    # cis,cis-9,12-octadecadienoic acid
    # C18:2 (Lipid numbers)
    # Sandor thinks the equivalent fatty acid is 18:2 n-6 c,c
    'Linoleic Acid (g/d)':
        {
            'matching_name_in_measuredfood': '18:2_n-6_cc-name-1316-id',
            'unit_conversion_factor': 1,
        },
    'α-Linolenic Acid (g/d)':
        {
            'matching_name_in_measuredfood': '18:3_n-3_ccc_(ala)-name-1404-id',
            'unit_conversion_factor': 1,
        },
    'Proteinb (g/d)':
        {
            'matching_name_in_measuredfood': 'protein-name-1003-id',
            'unit_conversion_factor': 1,
        },
}

match_nutrient_max_to_measuredfood_dict = {
    'Arsenica_max':
        {
            'matching_name_in_measuredfood': None,
            'unit_conversion_factor': 1,
        },
    'Boron (mg/d)_max':
        {
            'matching_name_in_measuredfood': 'max_boron_b-name-1137-id',
            'unit_conversion_factor': 1000,
        },
    'Calcium (mg/d)_max':
        {
            'matching_name_in_measuredfood': 'max_calcium_ca-name-1087-id',
            'unit_conversion_factor': 1,
        },
    'Chromium_max':
        {
            'matching_name_in_measuredfood': 'max_chromium_cr-name-1096-id',
            'unit_conversion_factor': 1,
        },
    'Copper (μg/d)_max':
        {
            'matching_name_in_measuredfood': 'max_copper_cu-name-1098-id',
            'unit_conversion_factor': 1/1000,
        },
    'Fluoride (mg/d)_max':
        {
            'matching_name_in_measuredfood': 'max_fluoride_f-name-1099-id',
            'unit_conversion_factor': 1/1000,
        },
    'Iodine (μg/d)_max':
        {
          'matching_name_in_measuredfood': 'max_iodine_i-name-1100-id',
          'unit_conversion_factor': 1,
        },
    'Iron (mg/d)_max':
        {
            'matching_name_in_measuredfood': 'max_iron_fe-name-1089-id',
            'unit_conversion_factor': 1,
        },
    'Magnesium (mg/d)_max':
        {
            'matching_name_in_measuredfood': 'max_magnesium_mg-name-1090-id',
            'unit_conversion_factor': 1,
        },
    'Manganese (mg/d)_max':
        {
            'matching_name_in_measuredfood': 'max_manganese_mn-name-1101-id',
            'unit_conversion_factor': 1,
        },
    'Molybdenum (μg/d)_max':
        {
            'matching_name_in_measuredfood': 'max_molybdenum_mo-name-1102-id',
            'unit_conversion_factor': 1,
        },
    'Phosphorus (g/d)_max':
        {
            'matching_name_in_measuredfood': 'max_phosphorus_p-name-1091-id',
            'unit_conversion_factor': 1000,
        },
    'Selenium (μg/d)_max':
        {
            'matching_name_in_measuredfood': 'max_selenium_se-name-1103-id',
            'unit_conversion_factor': 1,
        },
    'Zinc (mg/d)_max':
        {
            'matching_name_in_measuredfood': 'max_zinc_zn-name-1095-id',
            'unit_conversion_factor': 1,
        },
    'Potassium (g/d)_max':
        {
            'matching_name_in_measuredfood': 'max_potassium_k-name-1092-id',
            'unit_conversion_factor': 1000,
        },
    'Sodium (g/d)_max':
        {
            'matching_name_in_measuredfood': 'max_sodium_na-name-1093-id',
            'unit_conversion_factor': 1000,
        },
    'Chloride (g/d)_max':
        {
            'matching_name_in_measuredfood': 'max_chlorine_cl-name-1088-id',
            'unit_conversion_factor': 1000,
        },
    'Vitamin A (μg/d)_max':
        {
            'matching_name_in_measuredfood': 'max_vitamin_a_iu-name-1104-id',
            'unit_conversion_factor': 1/0.3,
        },
    'Vitamin C (mg/d)_max':
        {
            'matching_name_in_measuredfood':
                'max_vitamin_c_total_ascorbic_acid-name-1162-id',
            'unit_conversion_factor': 1,
        },
    'Vitamin D (μg/d)_max':
        {
            'matching_name_in_measuredfood': 'max_vitamin_d-name-1110-id',
            'unit_conversion_factor': 40,
        },
    'Vitamin E (mg/d)_max':
        {
            'matching_name_in_measuredfood':
                'max_vitamin_e_(label_entry_primarily)-name-1124-id',
            'unit_conversion_factor': 2.22,
            # Source:
            # https://ods.od.nih.gov/factsheets/VitaminE-HealthProfessional/
        },
    'Vitamin K_max':
        {
            'matching_name_in_measuredfood':
                'max_vitamin_k_(phylloquinone)-name-1185-id',
            'unit_conversion_factor': 1,
        },
    'Thiamin_max':
        {
            'matching_name_in_measuredfood': 'max_thiamin-name-1165-id',
            'unit_conversion_factor': 1,
        },
    'Riboflavin_max':
        {
            'matching_name_in_measuredfood': 'max_riboflavin-name-1166-id',
            'unit_conversion_factor': 1,
        },
    'Niacin (mg/d)_max':
        {
            'matching_name_in_measuredfood': 'max_niacin-name-1167-id',
            'unit_conversion_factor': 1,
        },
    'Vitamin B6 (mg/d)_max':
        {
            'matching_name_in_measuredfood': 'max_vitamin_b-6-name-1175-id',
            'unit_conversion_factor': 1,
        },
    'Folate (μg/d)_max':
        {
            'matching_name_in_measuredfood': 'max_folate_total-name-1177-id',
            'unit_conversion_factor': 1,
        },
    'Vitamin B12_max':
        {
            'matching_name_in_measuredfood': 'max_vitamin_b-12-name-1178-id',
            'unit_conversion_factor': 1,
        },
    'Pantothenic Acid_max':
        {
            'matching_name_in_measuredfood':
                'max_pantothenic_acid-name-1170-id',
            'unit_conversion_factor': 1,
        },
    'Biotin_max':
        {
            'matching_name_in_measuredfood': 'max_biotin-name-1176-id',
            'unit_conversion_factor': 1,
        },
    'Choline (g/d)_max':
        {
            'matching_name_in_measuredfood': 'max_choline_total-name-1180-id',
            'unit_conversion_factor': 1000,
        },
    'Total Watera (L/d)_max':
        {
            'matching_name_in_measuredfood': None,
            'unit_conversion_factor': 1,
        },
    'Carbohydrate (g/d)_max':
        {
            'matching_name_in_measuredfood':
                'max_carbohydrate_without_fiber-name-1-id',
            'unit_conversion_factor': 1,
        },
    'Total Fiber (g/d)_max':
        {
            'matching_name_in_measuredfood':
                'max_fiber_total_dietary-name-1079-id',
            'unit_conversion_factor': 1,
        },
    'Fat (g/d)_max':
        {
            'matching_name_in_measuredfood':
                'max_total_lipid_(fat)-name-1004-id',
            'unit_conversion_factor': 1,
        },
    # Linoleic acid is the essential omega 6 fatty acid, according to wikipedia
    # https://en.wikipedia.org/wiki/Linoleic_acid.
    # Other names:
    # cis,cis-9,12-octadecadienoic acid
    # C18:2 (Lipid numbers)
    # Sandor thinks the equivalent fatty acid is 18:2 n-6 c,c
    'Linoleic Acid (g/d)_max':
        {
            'matching_name_in_measuredfood': 'max_18:2_n-6_cc-name-1316-id',
            'unit_conversion_factor': 1,
        },
    'α-Linolenic Acid (g/d)_max':
        {
            'matching_name_in_measuredfood':
                'max_18:3_n-3_ccc_(ala)-name-1404-id',
            'unit_conversion_factor': 1,
        },
    'Proteinb (g/d)_max':
        {
            'matching_name_in_measuredfood': 'max_protein-name-1003-id',
            'unit_conversion_factor': 1,
        },
    'Carotenoids_max':
        {
            'matching_name_in_measuredfood': None,
            'unit_conversion_factor': None,
        },
    'Nickel (mg/d)_max':
        {
            'matching_name_in_measuredfood': None,
            'unit_conversion_factor': None,
        },
    'Silicon_max':
        {
            'matching_name_in_measuredfood': None,
            'unit_conversion_factor': None,
        },
    'Vanadium (mg/d)_max':
        {
            'matching_name_in_measuredfood': None,
            'unit_conversion_factor': None,
        },
}

match_nutrient_dri_to_measuredfood_dict.update(
    match_nutrient_max_to_measuredfood_dict
)
