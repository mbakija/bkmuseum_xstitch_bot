#this code is from https://towardsdatascience.com/how-to-download-an-image-using-python-38a75cfa21c
# it downloads an image from a url

## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally

# paste image url here
image_url = "YOUR_IMAGE_URL_GOES_HERE"
filename = image_url.split("/")[-1]

# Open the url image, set stream to True, this will return the stream content.
r = requests.get(image_url, stream = True)

# Check if the image was retrieved successfully
if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True

    # Open a local file with wb ( write binary ) permission.
    with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)

    print('Image sucessfully Downloaded: ',filename)
else:
    print('Image Couldn\'t be retreived')


#Here I tried to bulk download images from urls in a csv
# this pulled the last image url in the col in the file, and just that one.
# import csv
# with open('bkmuseum_obj_tweet.csv','r') as image_source:
#     parsed_csv = csv.reader(image_source)
#
#     for a_row in parsed_csv:
#         #print(a_row[4])
#         url_name = a_row[4]
#
# image_url = url_name
# filename = image_url.split("/")[-1]
