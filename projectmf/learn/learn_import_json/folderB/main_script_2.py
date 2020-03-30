import json
import sys
from pathlib import Path

print('sys.path')
print(sys.path)

# /home/matthias/1_local_code/mf-2/projectmf/learn/learn_import_json/folderA/example_json1.json

with open('/home/matthias/1_local_code/mf-2/projectmf/learn/learn_import_json/folderA/example_json1.json', 'r') as fp:
    ALL_NUTRIENTS_AND_DEFAULT_UNITS = json.load(fp)

print('ALL_NUTRIENTS_AND_DEFAULT_UNITS')
print(ALL_NUTRIENTS_AND_DEFAULT_UNITS)
