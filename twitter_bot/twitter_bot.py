# This is from https://github.com/MarkEEaton/bot-tutorial-ala
# Twitter Bot Starter Kit: Bot 3

# This bot tweets a text file line by line, waiting a
# given period of time between tweets.

# Housekeeping: do not edit
import tweepy, time
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# What the bot will tweet
filename = open('bkmus_obj_twitter.txt', 'r')
tweet_text = filename.readlines()
filename.close()

# loop through the tweet_text
for line in tweet_text[0:36]: # Will write first 36 (all)
    api.update_status(status=line, media_ids=media_list)
    print(line)
    time.sleep(15) # Sleep for 1 week

print("All done!")

# -----
# Here I was trying to upload images with the tweet

# trying to straight upload images
# single image fine (but of course, same image with every text line/tweet)
# but multiple images got error
# media_list = []
# response = api.media_upload('CROSS-STITCH.png', 'CROSS-STITCH_key.png')
# media_list.append(response.media_id_string)

# trying to use file with img paths as source for media
# # What the bot will tweet
# filename = open('bkmuseum_obj_twitter.txt', 'r')
# tweet_text = filename.readlines()
# filename.close()
#
# #image sources
# imgfilename = open('bkmuseum_obj_img.txt', 'r')
# tweet_imgs = imgfilename.readlines()
# filename.close()
#
# media_list = []
# for imgs in tweet_imgs[0:36]:
#     response = api.media_upload('tweet_imgs')
#     media_list.append(response.media_id_string)
#
# # loop through the tweet_text
# for line in tweet_text[0:36]: # Will write first 36 (all)
#     api.update_status(status=line, media_ids=media_list)
#     print(line)
#     time.sleep(15) # Sleep for 1 week
#
# -----

# this works to post each line from text file

# # What the bot will tweet
# filename = open('bkmuseum_obj_twitter.txt', 'r')
# tweet_text = filename.readlines()
# filename.close()
#
# # loop through the tweet_text
# for line in tweet_text[0:36]: # Will write first 36 (all)
#     api.update_status(status=line)
#     print(line)
#     time.sleep(604800) # Sleep for 1 week
