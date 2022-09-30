import json
import boto3
import os
import uuid

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    my_bucket = s3.get_object(Bucket="tabiicom-config-bucket", Key="blank")
    print(my_bucket)
    return "ok"

