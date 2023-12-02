#imports for solution setup
import boto3
import env
import json
import os
# imports for the days problem
import re


#problem url
#https://adventofcode.com/2023/day/2

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

def data_formatter(inp: str) -> list:
    return inp.split("\n")

#part1
inp = data_formatter(INP)
max_cubes = {
    'red' : 12,
    'green': 13,
    'blue' : 14
}
val = 0
for game in inp:
    valid = True
    game_id, game = game.split(": ")
    game_id = int(game_id.split(" ")[-1])
    games = game.split("; ")
    for g in games:
        split_g = g.split(", ")
        for indiv_g in split_g:
            val_g, color = indiv_g.split(" ")
            val_g = int(val_g)
            if int(val_g) > max_cubes[color]:
                valid = False
    if valid:
        val += game_id
print(val)



#part2
inp = data_formatter(INP)

val = 0
for game in inp:
    min_color = {
    'red' : 0,
    'green': 0,
    'blue' : 0
    }
    games = game.split(": ")[-1].split("; ")
    for g in games:
        split_g = g.split(", ")
        for indiv_g in split_g:
            val_g, color = indiv_g.split(" ")
            if min_color[color] < int(val_g):
                min_color[color] = int(val_g)
    val += (min_color['red'] * min_color['green'] * min_color['blue'])
print(val)

    






