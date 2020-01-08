

def merge_dataframe(
    pd,
):
    """
    The data for the nutrition profile is scattered over multiple sheets.
    In a first step, the sheets are merged.

    Since merging with pandas took too long, the sheets were manually merged
    in open office calc.

    The daily recommended intakes (DRI) and the tolerable upper intakes (TUI)
    have been merged into the same excel sheet.

    :param pd:
    :return:
    """
    df_list = []

    df = pd.read_excel(
        '/home/matthias/1_local_code/mf-2/projectmf/'
        'data/daily_recommended_intake.xlsx',
        sheet_name='dri_and_max_all_in_one'
    )
    df_list.append(df)

    merged_dataframe = pd.concat(df_list)

    return merged_dataframe
