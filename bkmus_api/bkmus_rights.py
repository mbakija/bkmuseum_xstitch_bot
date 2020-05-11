# this prints the collection name

import json

f = open('BKMobjects.json')
data = json.load(f)

for key in data['object']:
    print(key['rights_type']['name'])
