#TODO:
# checks the content of the dats.json file:
#  - Loads json as a python dictionary
#  - Extracts and matches REQUIRED, RECOMMENDED and OPTIONAL keys
#  - Notifies as Error if REQUIRED keys are missing and what they are, returns False
#  - Notifies with Warning if RECOMMENDED keys are missing and what they are, returns True
#  - else returns True


import json
import os.path as op

required = []
recommended = []
optional = []

json_file = 'dataset.json'

# get current path for the dataset.json DATS file
json_path = op.join(op.dirname(__file__), json_file)

with open(json_path) as file:
    data = json.load(file)

print(data)

# We have a list of required and a list of recommended. For each of the elements we check if they are contained in data
# We do not need to search through nested data structures as the terms we are checking for are 1st level
# e.g. data['@type']

