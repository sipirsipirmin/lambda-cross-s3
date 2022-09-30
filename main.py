import json
import boto3
import os
import uuid

def lambda_handler(event, context):
    client = boto3.client('sts')
    response = client.assume_role(RoleArn=os.getenv("ROLE_ARN"),RoleSessionName="{}-s3".format(str(uuid.uuid4())[:5]))
    session = boto3.Session(aws_access_key_id=response['Credentials']['AccessKeyId'],aws_secret_access_key=response['Credentials']['SecretAccessKey'],aws_session_token=response['Credentials']['SessionToken'])
    
    s3 = session.client('s3')
    #s3 = boto3.resource('s3')
    my_bucket = s3.get_object(Bucket=os.getenv("BUCKET_NAME"), Key="blank")
    print(my_bucket)
    return "ok"

