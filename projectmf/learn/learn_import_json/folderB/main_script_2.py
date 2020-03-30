import json
import sys
from pathlib import Path

print('sys.path')
print(sys.path)

print(f"Home directory: {Path.home()}")
print(f"Current directory: {Path.cwd()}")

path_to_json_file = Path.cwd().parent.joinpath('folderA').joinpath(
    'example_json1.json')
str_path_to_json_file = str(path_to_json_file)
print(f'str_path_to_json_file: {str_path_to_json_file}')

with open(path_to_json_file, 'r') as fp:
    ALL_NUTRIENTS_AND_DEFAULT_UNITS = json.load(fp)

# /home/matthias/1_local_code/mf-2/projectmf/learn/learn_import_json/folderA/example_json1.json

# with open('/home/matthias/1_local_code/mf-2/projectmf/learn/learn_import_json/folderA/example_json1.json', 'r') as fp:
#     ALL_NUTRIENTS_AND_DEFAULT_UNITS = json.load(fp)

print('ALL_NUTRIENTS_AND_DEFAULT_UNITS')
print(ALL_NUTRIENTS_AND_DEFAULT_UNITS)
