#imports for solution setup
import boto3
import env
import json
import os
# imports for the days problem
from itertools import pairwise

#problem url
#https://adventofcode.com/2023/day/9


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



def formatter(inp: str) -> list:
    return [x.split(" ") for x in inp.split("\n")]


#part1
sequences = formatter(INP)
next_vals = 0
pad_val = 0
for orig_seq in sequences:
    sequence = [int(x) for x in orig_seq]
    sub_sequences = []
    while True:
        interim = []
        for a, b in pairwise(sequence):
            interim.append(int(b) - int(a))
        if len(set(interim)) == 1:
            pad_val += interim[-1]
            for seq in sub_sequences:
                pad_val = seq[-1] + pad_val
            else:
                break
        else:
            sub_sequences.append([x for x in interim])
            sequence = sub_sequences[-1]
    next_vals += int(orig_seq[-1]) + pad_val
    pad_val = 0
print(next_vals)


 
#part2
# put my thing down flip it and reverse it
sequences = formatter(INP)
next_vals = 0
pad_val = 0
for orig_seq in sequences:
    sequence = [int(x) for x in orig_seq]
    sub_sequences = []
    while True:
        interim = []
        for a, b in pairwise(sequence):
            interim.append(int(b) - int(a))
        if len(set(interim)) == 1:
            pad_val += interim[-1]
            for seq in sub_sequences[::-1]:
                pad_val = seq[0] - pad_val
            else:
                break
        else:
            sub_sequences.append([x for x in interim])
            sequence = sub_sequences[-1]
    next_vals += int(orig_seq[0]) - pad_val
    pad_val = 0
print(next_vals)


        





    






