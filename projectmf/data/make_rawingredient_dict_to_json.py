from ingredients_data import ingredient_dict_list

import json
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(ingredient_dict_list, f, ensure_ascii=False, indent=4)
