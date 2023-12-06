#imports for solution setup
import boto3
import env
import json
import os
# imports for the days problem
import re


#problem url
#https://adventofcode.com/2023/day/6

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

tINP = """Time:      7  15   30
Distance:  9  40  200"""



#part1
def data_formatter(inp: str) -> list:
    inp = inp.split("\n")
    times = [int(x) for x in inp[0].split(":")[1].split(" ") if x != ""]
    distances = [int(x) for x in inp[1].split(":")[1].split(" ") if x != ""]
    return list(zip(times, distances))

def winning_press(race: tuple, time: int) -> int:   
    return ((race[0] - time) * time)


inp = data_formatter(INP)
result = 1
for race in inp:
    winning_presses = 0
    last_dist = 0
    for press in range(1,race[0]):
        dist = winning_press(race, press)
        if dist > race[1]:
            winning_presses += 1
            last_dist = dist
        elif dist >= last_dist:
                last_dist = dist
                continue
        else:
            result *= winning_presses
            break
print(result)
            
        

 
#part2
def data_formatter(inp: str) -> list:
    inp = inp.split("\n")
    times = int(''.join([x for x in inp[0].split(":")[1].split(" ") if x != ""]))
    distances = int(''.join([x for x in inp[1].split(":")[1].split(" ") if x != ""]))
    return [(times, distances)]


inp = data_formatter(INP)
result = 1
for race in inp:
    winning_presses = 0
    last_dist = 0
    for press in range(1,race[0]):
        dist = winning_press(race, press)
        if dist > race[1]:
            winning_presses += 1
            last_dist = dist
        elif dist >= last_dist:
                last_dist = dist
                continue
        else:
            result *= winning_presses
            break
print(result)






        





    






