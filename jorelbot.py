import tweepy
from tweepy import OAuthHandler
import time
import os
import datetime
import random
import cv2
import numpy as np

CONSUMER_KEY = 'T4nW5QPkQ1SMHeyibtA3Um94s'
CONSUMER_SECRET = 'ZpmWXAC0FSvUKhVWwj2gaAFnXycwdOcXRs547lXKNV58QoC8Ot'
ACCESS_KEY = '1134211442738176003-L9T9ANgGVRlmLwmujJdo7MLwr2aSSl'
ACCESS_SECRET = 'KiqHsXdqgce0yQnT27Hry8CwkICiNVFY4L4Trq2QFnXws'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def post_frame():
    path = '/home/zatta/Downloads/jorelito'
    files = os.listdir(path)
    index = random.randrange(0, len(files))
    path_new = '/home/zatta/Downloads/jorelito/'+str(files[index])
    #print("nome  "+path_new)
    cap = cv2.VideoCapture(path_new)

    amount_of_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_seq = random.randrange(500, amount_of_frames-700)

    cap.set(1, frame_seq-1)

    ret, frame = cap.read()
    name = '/home/zatta/Downloads/framesjo/jorel_no'+str(index)+ str(frame_seq) +'.png'

    cv2.imwrite(name, frame)

    #api.update_with_media(name)

    #os.remove(name)

    cap.release()
    cv2.destroyAllWindows()

x=0
while x<=4:
    post_frame()
    #time.sleep(15)
    x=x+1
