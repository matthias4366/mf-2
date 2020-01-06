

def make_nutrient_profile_dataframe_sheets_into_dict(
    life_stage_group_categories,
    sheet_names,
    pd,
):
    # First, the nutrient profiles from the national institute of health will be
    # put in a dictionary so they are easier to handle.
    list_nutrient_profiles_national_institute_of_health_raw = []

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
                # there are no nutrient values - hence,
                # continue to the next row.
                continue
            full_life_stage = current_life_stage_categorie + df.iat[
                row_index, 0]
            print('full_life_stage')
            print(full_life_stage)

            nutrient_profile_dict['full_life_stage'] = full_life_stage

            # The iteration starts at 1 in order to skip the
            # "Life Stage\nGroup" column.
            for col_index in range(1, n_columns):
                nutrient_amount_dri = df.iat[row_index, col_index]
                nutrient_name_dri = df.columns[col_index]
                print('nutrient_name_dri')
                print(nutrient_name_dri)
                print('nutrient_amount_dri')
                print(nutrient_amount_dri)

                nutrient_profile_dict[nutrient_name_dri] = \
                    nutrient_amount_dri

        list_nutrient_profiles_national_institute_of_health_raw.append(
            nutrient_profile_dict
        )

    return list_nutrient_profiles_national_institute_of_health_raw
