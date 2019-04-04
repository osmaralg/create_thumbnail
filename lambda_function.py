import json
from PIL import Image

import boto3
import os
import sys
import uuid
from PIL import Image
import PIL.Image

s3_client = boto3.client('s3')


def resize_image(image_path, resized_path):
    with Image.open(image_path) as image:
        image.thumbnail(tuple(x / 2 for x in image.size))
        image.save(resized_path)


def lambda_handler(event, context):

    val_1 = event["queryStringParameters"]['min']
    val_2 = event["queryStringParameters"]['max']
    # for record in records
    bucket = "skysset-platform-assets" # bucket name
    key = "test.png" #record['s3']['object']['key']
    download_path = key #'/tmp/{}{}'.format(uuid.uuid4(), key)
    upload_path = 'media/tmp/resized-{}'.format(key)

    s3_client.download_file(bucket, key, download_path)
    resize_image(download_path, upload_path)
    s3_client.upload_file(upload_path, '{}resized'.format(bucket), key)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!' + str(int(val_1)*int(val_2)))
    }

