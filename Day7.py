#imports for solution setup
import boto3
import env
import json
import os
# imports for the days problem



#problem url
#https://adventofcode.com/2023/day/7

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

val_map = {
    "A" : 14,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "T" : 10,
    "J" : 11,
    "Q" : 12,
    "K" : 13
    }


def data_formatter(inp: str) -> list:
    return [x.split(" ") for x in inp.split("\n")]

def card_strength_type(card: str) -> int:
    card, bid = card[0], card[1]
    card_set = list(set(list(card)))
    if len(card_set) == 1:
        return 7
    elif len(card_set) == 2:
        if card.count(card_set[0]) == 4 or card.count(card_set[1]) == 4:
            return 6
        else:
            return 5
    elif len(card_set) == 3:
        count_per_card = []
        for c in card_set:
            count_per_card.append(card.count(c))
        if max(count_per_card) == 3:
            return 4
        else:
            return 3
    elif len(card_set) == 5:
        return 1
    else:
        return 2

def card_sort_val(card) -> list:
    c = list(card[0])
    out = []
    for x in c:
        out.append(val_map[x])
    return out




inp = data_formatter(INP)
cards = []
for i in inp:
    card_type = card_strength_type(i)
    card_sort = card_sort_val(i)
    cards.append((int(i[1]), card_type, card_sort))

print(sum([y[0] * (x+1)  for x, y in enumerate(sorted(cards, key=lambda x: (x[1], x[2])))]))

 
#part2



val_map = {
    "A" : 14,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "T" : 10,
    "J" : 1,
    "Q" : 12,
    "K" : 13
    }


def data_formatter(inp: str) -> list:
    return [x.split(" ") for x in inp.split("\n")]

def card_strength_type(card: str) -> int:
    card_set = list(set(list(card)))
    if len(card_set) == 1:
        # five of a kind
        return 7
    elif len(card_set) == 2:
        if card.count(card_set[0]) == 4 or card.count(card_set[1]) == 4:
            # four of a kind
            return 6
        else:
            # full house
            return 5
    elif len(card_set) == 3:
        count_per_card = []
        for c in card_set:
            count_per_card.append(card.count(c))
        if max(count_per_card) == 3:
            return 4
        else:
            return 3
    elif len(card_set) == 5:
        return 1
    else:
        return 2

def card_sort_val(card) -> list:
    c = list(card[0])
    out = []
    for x in c:
        out.append(val_map[x])
    return out



inp = data_formatter(INP)
cards = []
for i in inp:
    counting_cards = []
    for x in list(set(i[0])):
        counting_cards.append((x, i[0].count(x)))
    hi_vals = sorted([x for x in counting_cards if x], key=lambda x: x[1])
    if hi_vals[-1] == ('J', 5):
        hi_val = ('2', 5)
    else:
        if hi_vals[-1][0] == "J":
            hi_val = hi_vals[-2]
        else:
            hi_val = hi_vals[-1]
    if "J" in i[0]:
        nu_val = i[0].replace("J", hi_val[0])
    else:
        nu_val = i[0]
    card_type = card_strength_type(nu_val)
    card_sort = card_sort_val(i)
    cards.append((int(i[1]), card_type, card_sort))
print(sum([y[0] * (x+1)  for x, y in enumerate(sorted(cards, key=lambda x: (x[1], x[2])))]))






        





    






