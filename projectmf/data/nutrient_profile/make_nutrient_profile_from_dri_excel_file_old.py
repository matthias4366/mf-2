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
from match_nutrient_dri_to_measuredfood_dict import \
    match_nutrient_dri_to_measuredfood_dict
from match_nutrient_dri_to_measuredfood import \
    match_nutrient_dri_to_measuredfood

sheet_names = [
    'dri_elements',
    'dri_vitamins',
    'dri_macronutrients',
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

# All the nutrient_profile_dict are stored in the following list
# list_nutrient_profiles_national_institute_of_health.
list_nutrient_profiles_national_institute_of_health = []

for sheet_name in sheet_names:

    # Read the excel sheet.

    df = pd.read_excel(
        '/home/matthias/1_local_code/mf-2/projectmf/'
        'data/daily_recommended_intake.xlsx',
        sheet_name=sheet_name
    )

    print('df:')
    print(df)

    # Returns tuple of shape (Rows, columns) of dataframe/series.
    df_dimensions = df.shape
    n_rows = df_dimensions[0]
    n_columns = df_dimensions[1]

    cell_content = df.iat[1, 3]

    # Start with the first few rows to keep things simpler.
    for row_index in range(0, 5):
        # for row_index in range(0, n_rows):  # proper code

        # The nutrient_profile_dict is the dictionary in which the resulting
        # nutrient profile is stored.
        nutrient_profile_dict = {}

        # Get the category of the current life stage.
        if df.iat[row_index, 0] in life_stage_group_categories:
            current_life_stage_categorie = df.iat[row_index, 0]
            # In the rows where the category of the life stage is listed,
            # there are no nutrient values - hence, continue to the next row.
            continue
        full_life_stage = current_life_stage_categorie + df.iat[row_index, 0]
        print('full_life_stage')
        print(full_life_stage)

        nutrient_profile_dict['name'] = full_life_stage

        # The iteration starts at 1 in order to skip the
        # "Life Stage\nGroup" column.
        for col_index in range(1, n_columns):
            nutrient_amount_dri = df.iat[row_index, col_index]
            nutrient_name_dri = df.columns[col_index]
            print('nutrient_name_dri')
            print(nutrient_name_dri)
            print('nutrient_amount_dri')
            print(nutrient_amount_dri)

            nutrient_amount_measuredfood, nutrient_name_measuredfood = \
                match_nutrient_dri_to_measuredfood(
                    match_nutrient_dri_to_measuredfood_dict,
                    nutrient_name_dri,
                    nutrient_amount_dri,
                )

            nutrient_profile_dict[nutrient_name_measuredfood] = \
                nutrient_amount_measuredfood

        list_nutrient_profiles_national_institute_of_health.append(
            nutrient_profile_dict
        )

    # Transform the values from the dataframe to floats or None.
    # Map NaN to None.
    # Remove non numbers, such as *, a, b etc.

with open('nutrient_profiles_from_national_institute_of_health.json', 'w') as\
        fp:
    json.dump(list_nutrient_profiles_national_institute_of_health, fp, indent=4)
