# this prints the collection name

import json

f = open('BKMobjects.json')
data = json.load(f)

for key in data['object']:
    print(key['collections'][0]['name'])
