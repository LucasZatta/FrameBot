import tweepy
from tweepy import OAuthHandler
import time
import os
import datetime
import random
import cv2
import numpy as np

CONSUMER_KEY = 'APIKEY'
CONSUMER_SECRET = 'APICONSUMERKEY'
ACCESS_KEY = 'ACESSTOKEN'
ACCESS_SECRET = 'ACESSTOKENSECRET'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def post_frame():
    path = 'episodes folder path' #the bot will search through a database of episodes, in this case
                                  #"irmao do jorel" episodes.
    files = os.listdir(path)
    index = random.randrange(0, len(files)) #radomly it selects an episode from the file
    path_new = 'episodes folder path' +str(files[index])#then it creates a new path to the selected episode
    #print("nome  "+path_new)
    cap = cv2.VideoCapture(path_new) #creating a cv2obj

    amount_of_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) #saving the total frames of the episode
    frame_seq = random.randrange(500, amount_of_frames-700) #and radomly selecting a frame within the frame span of the episode

    cap.set(1, frame_seq-1) #now we set the obj to the selected frame

    ret, frame = cap.read() #read the frame
    name = 'Frames saved folder path '+str(index)+ str(frame_seq) +'.png' #create a path to the new image we want to save

    cv2.imwrite(name, frame)

    api.update_with_media(name)  #this will post the image we saved on the twitter account

    os.remove(name) #then, after its posted, the algorithm removes it to avoid unnecessary memory use.

    cap.release()
    cv2.destroyAllWindows()

x=0
while x<=4:         #the script is hosted in a site where it runs daily, it posts 4 frames with a 15 seconds time span within each frame posted
    post_frame()
    time.sleep(15)
    x=x+1
