import json

with open('folderA/example_json1.json', 'r') as fp:
    ALL_NUTRIENTS_AND_DEFAULT_UNITS = json.load(fp)

print('ALL_NUTRIENTS_AND_DEFAULT_UNITS')
print(ALL_NUTRIENTS_AND_DEFAULT_UNITS)
