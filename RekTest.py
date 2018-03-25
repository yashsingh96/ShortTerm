import requests
import boto3
import json
from PIL import Image
from flask import request
import boto3
from botocore.client import Config
ACCESS_KEY_ID = 'AKIAJKUDZGRNMODF4SDA'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'hackuva'
filename = 'DrPepper.jpg' 
image_file = 'DrPepper.jpg'
	
s3 = boto3.resource('s3',aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=ACCESS_SECRET_KEY, config=Config(signature_version='s3'))
s3.Bucket(BUCKET_NAME).put_object(Key=filename, Body=image_file)

bucket='hackuva'
fileName = filename
    
client=boto3.client('rekognition','us-east-1')

s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version='s3')
    )

#response = client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':fileName}})

#print json.dumps(response)
#print('Detected Text for ' + fileName)   
    
#print json.dumps(response)
    
#data = []
    
#for label in response['TextDetections']:
    #print (label['DetectedText'] + ' : ' + str(label['Confidence']))
 #   output = str(label['DetectedText'])
  #  output = output.split()
    	
   # for item in output:
    #    if len(item) > 1 and item not in data:
     #       data.append(item)
            
                