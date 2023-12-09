import boto3
import env
import json
import os

day = "Day10"
new_inp = """"""


S3 = boto3.client(
    service_name='s3',
    region_name=os.environ["AWS_DEFAULT_REGION"],
    aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"]
)

OBJ = S3.get_object(Bucket=os.environ["AWS_BUCKET"], Key=os.environ["AWS_FILE"])
INP = json.loads(OBJ['Body'].read().decode("utf-8"))

INP[day] = new_inp
with open(os.environ["AWS_FILE"], 'w') as file:
    json.dump(INP, file)

S3.upload_file(os.environ["AWS_FILE"] ,os.environ["AWS_BUCKET"], os.environ["AWS_FILE"])

os.remove(os.environ["AWS_FILE"])