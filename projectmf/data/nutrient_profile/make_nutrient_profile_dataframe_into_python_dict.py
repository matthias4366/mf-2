

def make_nutrient_profile_dataframe_into_python_dict(
    df,
    life_stage_group_categories,
    re,
    make_number_from_national_institute_of_health_str,
):
    list_nutrient_profile_dict_national_institute_of_health = []

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

        nutrient_profile_dict['name'] = full_life_stage
        # dri stands for 'daily recommended intake.
        nutrient_profile_dict['dri'] = {}

        # The iteration starts at 1 in order to skip the
        # "Life Stage\nGroup" column.
        for col_index in range(1, n_columns):
            nutrient_amount_dri = df.iat[row_index, col_index]
            nutrient_name_dri = df.columns[col_index]

            nutrient_amount_measuredfood = \
                make_number_from_national_institute_of_health_str(
                    str(nutrient_amount_dri),
                    re,
                )

            nutrient_profile_dict['dri'][nutrient_name_dri] = \
                nutrient_amount_measuredfood

        list_nutrient_profile_dict_national_institute_of_health.append(
            nutrient_profile_dict
        )

    return list_nutrient_profile_dict_national_institute_of_health
