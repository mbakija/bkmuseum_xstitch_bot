# via https://github.com/Pyython/brooklyn-museum-mediachain

import requests, json, config

url = 'https://www.brooklynmuseum.org/api/v2/object/'
headers = {'api_key': config.API_KEY}


# this created a 300MB json file, but it seems that the formatting is fucked up
def main():
    objects = []
    payload = {'total_count_only': 1}
    num_objects = int(requests.get(url, headers=headers, params=payload).json()['data'])

    # API limits responses to 35 items at a time.
    # While loop fetches the next 35 items and
    # adds each item to a new JSON array until dataset is exhausted.
    while(len(objects) < num_objects):
        payload = {'offset': len(objects), 'limit': 35}
        r = requests.get(url, headers=headers, params=payload)
        #print "Fetching: {} records".format(len(r.json()['data']))
        for item in r.json()['data']:
            objects.append(item)
    #print "Total records: {}".format(len(objects))
    with open('objects.json', 'w') as f:
        json.dump(objects, f)

if __name__ == '__main__':
    main()


# this via me, but it created a json file with only 12 objects

# r = requests.get(url, headers=headers)
#
# results = json.loads(r.text)
#
# json.dump(results, open("objects2.json",'w'),indent=2)
#
# print(r.status_code)
