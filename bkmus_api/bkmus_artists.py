#this prints the artist names

import json

f = open('BKMobjects.json')
data = json.load(f)

for key in data['object']:
    print(key['artists'][0]['name'])
