# this prints the object id number
# the results are appended to https://www.brooklynmuseum.org/opencollection/objects/
# which is the link to the object on the Brooklyn Museum website


import json

f = open('BKMobjects.json')
data = json.load(f)

for id in data['object']:
    print('https://www.brooklynmuseum.org/opencollection/objects/' + str(id['id']))

# down here is just a mess of attempts to do everything all toghether
# I want to only print objects if they had:
# copyright_restricted == 0 AND primary_image != "None"
# and then for those objects, I wanted to print:
# id, artists name, title, collection name, primary_image
# and maybe while doing that, alter the id to be the object url
# and the primary_image to be the image url
# and then put all that info into a csv
# then download image files, change into cross stitch patterns
# which would then have to change from SVG to PNG files
# then post a random selection based on collection name
# along with artists name, title, @brooklynmuseum, and object URL
# to @bkmuseum_xstitch


# object_count = 0
#
# f = open('objects.json')
# data = json.load(f)
#
# for object in data:
#     for rights_type in object:
#         for name in rights_type:
#             if "no known copyright restrictions" in name:
#                 print(object['id']+','+['title']+','+['artist']+','+['primary_image'])
#                 object_count = object_count+1
#
# print('Total objects:')
# print(object_count)
# print('------')

#this also just prints our total objects 0

# object_count = 0
#
# f = open('objects.json')
# data = json.load(f)
# # f.close()
#
# for object in data:
#     for rights_type in object:
#         for name in rights_type:
#             if name is "no known copyright restrictions":
#                 print('id:', object['id'])
#                 object_count = object_count+1
#
# print('Total objects:')
# print(object_count)
# print('------')

# this does something, but just prints out:
#Total objects
#0

# object_count = 0
#
# f = open('objects.json')
# data = json.load(f)
# # f.close()
#
# for object in data:
#     for copyright_restricted in object:
#             if copyright_restricted == "0":
#                 print('id:', object['id'])
#                 object_count = object_count+1
#
# print('Total objects:')
# print(object_count)
# print('------')


#this printed every id with every artist name
# object_count = 0
#
# f = open('objects5.json')
# data = json.load(f)
#
# for id in data['object']:
#     for key in data['object']:
#         print('id:', id['id'], 'artist:', key['artists'][0]['name'])
#         object_count = object_count+1
#
# print('Total objects:')
# print(object_count)
# print('------')

# object_count = 0

# -------
#this prints just the artist names:
# f = open('objects5.json')
# data = json.load(f)
#
# for key in data['object']:
#     print('artist:', key['artists'][0]['name'])
#
# -------


# if "object" in data:
#     if "artists" in data['object']:
#         print(artistname['name'])
#nothing printed

# for artistsname in data['object']['artists']:
#     print(artistsname['name'])
# #TypeError: list indices must be integers or slices, not str


# for artists in data['object']:
#     print(artists['name'])
#KeyError: 'name'

# for artists in data['object']:
#     print(artists(0['name']))
#TypeError: 'int' object is not subscriptable

# object_count = 0
#
# f = open('objects.json')
# data = json.load(f)
#
# for id in data['object']:
#     for artistname in data['object']['artists']:
#         print(id['id'],'\n',id['title'],'\n',artistname['name'],'\n',id['primary_image'],'\n')
#
#         object_count = object_count+1
#
# print('Total objects:')
# print(object_count)
# print('------')

#
# object_count = 0
#
# f = open('objects.json')
# data = json.load(f)
# # f.close()
#
# for id in data['object']:
#     print(id['id'],'\n',id['title'],'\n',id['primary_image'],'\n')
#
#     for artistname in data['object']['artists']['name']:
#         print(artistname['name']
#
#
# #I want to print(object[artists(0)[name]])
#         # for artists in data['object']:
#         #     for artists[0] in artists:
#         #     # for info[0] in data['object'][artists]:
#         #         #for names in artists[0]:
#         #         # for artists[0] in names:
#         #         print(artists['name'])
#         for id in data['object']:
#             print(id['primary_image'],'\n')
#
#             object_count = object_count+1
#
# print('Total objects:')
# print(object_count)
# print('------')

# object_count = 0
#
# f = open('objects.json')
# data = json.load(f)
# # f.close()
#
# for id in data['object']:
#     print(id['id'], '\n', id['title'])
#     for artists in data['object']:
#         for name in artists:
#             print(artists['name'], '\n')
#         #for artists['name'] in data['object']:
#             print(id['primary_image'], '\n')
# #'\n', artists('name')],
#             object_count = object_count+1
#
# print('Total objects:')
# print(object_count)
# print('------')

#this prints out the id, title, and primary image of all objects
# object_count = 0
#
# f = open('objects.json')
# data = json.load(f)
# # f.close()
#
# for id in data['object']:
#         print(id['id'],'\n',id['title'],'\n',id['primary_image'],'\n')
#
#         object_count = object_count+1
#
# print('Total objects:')
# print(object_count)
# print('------')

# this worked to print all ids and a count of them

# object_count = 0
#
# f = open('objects.json')
# data = json.load(f)
# # f.close()
#
# for id in data['object']:
#         print('id:', id['id'])
#
#         object_count = object_count+1
#
# print('Total objects:')
# print(object_count)
# print('------')


# this sort of worked except it didn't. it only printed the first id, but a bunch of times
# f = open('objects.json')
# data = json.load(f)
#
# for id in data:
#     print(data[0]['id'])

# for (k, v) in data.items():
#    print("id: " + k)
#    print("title: " + str(v))

# for objects in f:
#     for info in objects[id]:
#         print('id')
            # for
            # print(id)
