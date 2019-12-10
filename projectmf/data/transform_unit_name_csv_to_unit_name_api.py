

def transform_unit_name_csv_to_unit_name_api(
        unit_name_csv
):
    mapping_dict = {
        'G': 'g',
        'KCAL': 'kcal',
        'SP_GR': 'sp gr',
        'MG': 'mg',
        'kJ': 'kJ',
        'UG': '\u00b5g',
        'IU': 'IU',
        'MG_ATE': 'mg',

    }
    if unit_name_csv in mapping_dict.keys():
        unit_name_api = mapping_dict[unit_name_csv]
    else:
        unit_name_api = unit_name_csv
        print('Unit name not found in mapping_dict:')
        print(unit_name_csv)
    return unit_name_api
