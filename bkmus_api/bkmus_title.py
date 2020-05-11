# this prints the objects' titles
# however, it prints too long a list; not sure where the extras came from...
# it's possible some title entries have a return in the text, pushing some content to
# a new line, but trying to figure that out could be... annoying

import json

f = open('BKMobjects.json')
data = json.load(f)

for id in data['object']:
    print(id['title'])
