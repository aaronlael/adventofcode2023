#imports for solution setup
import boto3
import env
import json
import os
# imports for the days problem
import re


#problem url
#https://adventofcode.com/2023/day/4

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

winnings = 0
for i in inp:
    ticket_winnings = 0
    winning_numbers = [x for x in (i.split(" | ")[0].split(": ")[1].split(" ")) if x != ""]
    ticket_numbers = [x for x in (i.split(" | ")[1].split(" ")) if x != ""]
    for number in ticket_numbers:
        if number in winning_numbers:
            if ticket_winnings == 0:
                ticket_winnings += 1
            else:
                ticket_winnings *= 2
    winnings += ticket_winnings
print(winnings)



#part2
inp = data_formatter(INP)

card_count = 0
known_cards = {}
for n, i in enumerate(inp):
    ticket_winnings = 0
    winning_numbers = [x for x in (i.split(" | ")[0].split(": ")[1].split(" ")) if x != ""]
    ticket_numbers = [x for x in (i.split(" | ")[1].split(" ")) if x != ""]
    for number in ticket_numbers:
        if number in winning_numbers:
            ticket_winnings += 1
    if str(n+1) not in known_cards.keys():
        known_cards[str(n+1)] = 1
    else:
        known_cards[str(n+1)] += 1
    for j in range(n+2, n+2+ticket_winnings):
        if str(j) not in known_cards.keys():
            known_cards[str(j)] = 1 * known_cards[str(n+1)]
        else:
            known_cards[str(j)] += 1 * known_cards[str(n+1)]

print(sum([v for _, v in known_cards.items()]))
    








        





    






