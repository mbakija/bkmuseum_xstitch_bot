# print copyright restrictions: 0 = not restricted, 1 = in copyright
# that said, several pieces (particularly in Contemporary Art collection)
# do have copyright notices on them even if copyright restrictions == 0
# sorting by "rights_type": "name" might be more clarifying, but the number of 
# But I'd argue this use is tranformative and therefore fair use
# though I also might sort out and remove Contemporary Art from the final usage

import json

f = open('BKMobjects.json')
data = json.load(f)

for id in data['object']:
    print(id['copyright_restricted'])
