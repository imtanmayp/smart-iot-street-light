import boto3
import time

from botocore.client import Config



ACCESS_KEY_ID = 'AKIAJUPXKQDBAO5NTZHQ'

ACCESS_SECRET_KEY = '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'

BUCKET_NAME = 'iotstreetlight'

data = open("/home/pi/Desktop/Final/img.png", 'rb')
'''data1 = open("/home/pi/Desktop/Final/img2.png", 'rb')
data2 = open("/home/pi/Desktop/Final/img3.png", 'rb')
data3 = open("/home/pi/Desktop/Final/img4.png", 'rb')
data4 = open("/home/pi/Desktop/Final/img5.png", 'rb')
'''
#for i in range (1,3):
s3 = boto3.resource('s3',aws_access_key_id=ACCESS_KEY_ID,aws_secret_access_key=ACCESS_SECRET_KEY,config=Config(signature_version='s3v4'))

s3.Bucket(BUCKET_NAME).put_object(Key="img.png", Body=data)
'''s3.Bucket(BUCKET_NAME).put_object(Key="img1.png", Body=data)
s3.Bucket(BUCKET_NAME).put_object(Key="img2.png", Body=data1)
s3.Bucket(BUCKET_NAME).put_object(Key="img3.png", Body=data2)
s3.Bucket(BUCKET_NAME).put_object(Key="img4.png", Body=data3)
'''
print ("Done")

