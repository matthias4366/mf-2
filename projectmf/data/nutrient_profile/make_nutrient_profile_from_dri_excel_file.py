"""
It is a chore to add the nutrient profile manually.

The daily recommended intakes for all life stages are found at
https://ods.od.nih.gov/Health_Information/Dietary_Reference_Intakes.aspx.

From this website, the information was copy pasted into an excel file called
daily_recommended_intake.xlsx.

The script make_nutrient_profile_from_dri_excel_file takes in that excel file
and makes nutrient profile dictionaries out of it, which will then be added
to measuredfood using
add_national_institute_of_health_nutrient_profiles_selenium.py.
"""
import pandas as pd
import json
import re
from match_nutrient_dri_to_measuredfood_dict import \
    match_nutrient_dri_to_measuredfood_dict
from match_nutrient_dri_to_measuredfood import \
    match_nutrient_dri_to_measuredfood
from make_nutrient_profile_dataframe_into_python_dict import \
    make_nutrient_profile_dataframe_into_python_dict
from merge_dataframe import merge_dataframe
from make_number_from_national_institute_of_health_str import \
    make_number_from_national_institute_of_health_str

sheet_names = [
    'dri_elements',
    'dri_vitamins',
    'dri_macronutrients',
]

# Think about the tolerable upper intakes later.
sheet_names_max = [
    'tolerable_upper_intake_vitamins',
    'tolerable_upper_intake_elements',
]

# Create nutrient profile names based on the Life Stage\nGroup column.
# In the Life Stage\nGroup column.
life_stage_group_categories = [
    'Infants',
    'Children',
    'Males',
    'Females',
    'Pregnancy',
    'Lactation',
]

# Merge all the dataframe sheets into one.
merged_dataframe = merge_dataframe(
    pd,
)

# merged_dataframe.to_excel("merged_dataframe.xlsx")

# Make the merged dataframe into a python dictionary, so it is easier to handle.
list_nutrient_profile_dict_national_institute_of_health = \
    make_nutrient_profile_dataframe_into_python_dict(
        merged_dataframe,
        life_stage_group_categories,
        re,
        make_number_from_national_institute_of_health_str,
        match_nutrient_dri_to_measuredfood,
        match_nutrient_dri_to_measuredfood_dict,
    )

# From the dictionary from the national institute of health, make a
# transformed dictionary that can be used in the measuredfood app.

with open('nutrient_profiles_from_national_institute_of_health.json', 'w') as\
        fp:
    json.dump(
        list_nutrient_profile_dict_national_institute_of_health, fp, indent=4
    )
