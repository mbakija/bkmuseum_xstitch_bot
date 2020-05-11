# print end of URL for image
# (some objects do not have an image, those are noted as NONE)
# the results are appended to https://d1lfxha3ugu3d4.cloudfront.net/images/opencollection/objects/size4/
# which is the URL for the large-size image the museum makes available to download

import json

f = open('BKMobjects.json')
data = json.load(f)

for id in data['object']:
    print('https://d1lfxha3ugu3d4.cloudfront.net/images/opencollection/objects/size4/' + str(id['primary_image']))
