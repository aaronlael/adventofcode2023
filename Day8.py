#imports for solution setup
import boto3
import env
import json
import os
# imports for the days problem
import re
from math import lcm

#problem url
#https://adventofcode.com/2023/day/8
#credit to this comment for teaching me about LCM -> https://www.reddit.com/r/adventofcode/comments/18dfpub/comment/kcgyhfi/?utm_source=share&utm_medium=web2x&context=3

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



def formatter(inp: str) -> dict:
    out = {}
    left_right, nodes = inp.split("\n\n")
    out['directions'] = list(left_right)
    nodes = nodes.split("\n")
    for node in nodes:
        node, paths = node.split(" = ")
        paths = paths[1:-1].split(", ")
        out[node] = (paths[0], paths[1])
    return out


#part1
nodes = formatter(INP)
steps = 0
node_len = len(nodes['directions'])
current_key = 'AAA'
while current_key != 'ZZZ':
    index = steps % node_len
    steps += 1
    if nodes['directions'][index] == "L":
        current_key = nodes[current_key][0]
    else:
        current_key = nodes[current_key][1]
print(steps)

 
#part2
nodes = formatter(INP)
steps = 0
node_len = len(nodes['directions'])
end_keys = [x for x in list(nodes.keys())[1:] if x[-1] == "Z"]
current_keys = [x for x in list(nodes.keys())[1:] if x[-1] == "A"]
path_lengths = []
for key in current_keys:
    while True:
        index = steps % node_len
        steps += 1
        if nodes['directions'][index] == "L":
            key = nodes[key][0]
        else:
            key = nodes[key][1]
        if key in end_keys:
            path_lengths.append(steps)
            steps = 0
            break    
print(lcm(*path_lengths))


        





    






