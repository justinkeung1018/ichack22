import json

import sys
import argparse

import cv2
print(cv2.__version__)

def extractImages(path_in, path_out):
    count = 0
    vidcap = cv2.VideoCapture(path_in)
    success,image = vidcap.read()
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000)) 
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        try:
            cv2.imwrite(path_out + "frame%d.jpg" % count, image)
        except:
            return
        print(path_out + "\\frame%d.jpg" % count)
        count = count + 1

if __name__=="__main__":
    extractImages("IMG_0473.mov", "") # Add // after path_out if using different directory

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
