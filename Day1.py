#imports for solution setup
import boto3
import env
import json
import os
# imports for the days problem
import re


#problem url
#https://adventofcode.com/2023/day/1

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


#part1
inp = INP.split("\n")
vals = 0
for i in inp:
    v = [x for x in list(i) if x in '1234567890']
    vals += int(v[0] + v[-1])
print(vals)


#part2
inp = INP.split("\n")
number_wang = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9,
    }


val = 0
pattern = r'(?=(one|two|three|four|five|six|seven|eight|nine|[1234567890]))'
for i in inp:
    nums = re.findall(pattern, i)
    start, end = nums[0], nums[-1]
    try:
        start = int(start)
    except ValueError:
        start = number_wang[start]
    try:
        end = int(end)
    except ValueError:
        end = number_wang[end]
    val += int(str(start) + str(end))
print(val)


    






