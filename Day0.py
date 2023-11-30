#imports
import boto3
import env
import json
import os


#problem url
"""this is just a test problem to get the workings of my repo down"""
"""part 1 - how many values are in the input"""
"""part 2 - how many characters are in the input"""

#globals - loading the input data
DAY = os.path.basename(__file__).replace('.py', '')
S3 = boto3.client(
    service_name='s3',
    region_name=os.environ["AWS_DEFAULT_REGION"],
    aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"]
)

OBJ = S3.get_object(Bucket=os.environ["AWS_BUCKET"], Key=os.environ["AWS_FILE"])
INP = json.loads(OBJ['Body'].read().decode("utf-8"))[DAY]
TEST_CASES = """"""
TEST_FLAG = True


#part1
print("part 1 is len of input vals!")
inp = INP.split("\n")
print(len(inp))


#part2
print("part 2 is number of characters in input!")
inp = INP.split("\n")
print(len(''.join(inp)))
