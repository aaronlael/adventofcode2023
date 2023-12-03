#imports for solution setup
import boto3
import env
import json
import os
# imports for the days problem
import re


#problem url
#https://adventofcode.com/2023/day/3

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
def check_symbols(num: tuple, inp_len: int, inp_width: int, inp: list) -> bool:
    """takes a tuple of (value, (span_start, span_end), index) and the length of the input"""
    # i got the list of symbols by ''.join([x for x in list(set(INP)) if x not in '0123456789.\\n'])
    symbols = "*/+#@$-&=%"
    rows = [num[2]]
    cols = [x for x in range(num[1][0], num[1][1])]
    
    if num[2] > 0:
        rows = [num[2] - 1] + rows
    if num[2] < (inp_len - 1):
        rows.append(num[2] + 1)
    if cols[0] > 0:
        cols = [(cols[0] - 1)] + cols
    if cols[-1] < inp_width - 1:
        cols.append(cols[-1] + 1)
    coords = []
    for y in cols:
        for x in rows:
            coords.append((x, y))
    for coord in coords:
        if inp[coord[0]][coord[1]] in symbols:
            return True
    else:
        return False


val = 0
num_locs = []
inp = data_formatter(INP)
l = len(inp)
w = len(inp[0])
for i in range(len(inp)):
    match_generator = re.finditer(r"\d+", inp[i])
    for match in match_generator:
        num_locs.append((match.group(), match.span(), i))
for num in num_locs:
    if check_symbols(num, l, w, inp):
        val += int(num[0])
print(val)




#part2
def gear_ratio(gear_loc: tuple, num_locs: list) -> int:
    possible_nums = [x for x in num_locs if x[2] in range(gear_loc[1] - 1, gear_loc[1] + 2)]
    touch_count = 0
    touching_nums = []
    for num in possible_nums:

        if gear_loc[0] in range(num[1][0] - 1, num[1][1] + 1):
            touch_count += 1
            touching_nums.append(int(num[0]))
    if touch_count == 2:
        return touching_nums[0] * touching_nums[1]
    else:
        return 0


val = 0
num_locs = []
gear_locs = []
inp = data_formatter(INP)
l = len(inp)
w = len(inp[0])
for i in range(len(inp)):
    match_generator = re.finditer(r"\d+", inp[i])
    for match in match_generator:
        num_locs.append((match.group(), match.span(), i))
    gear_match_generator = re.finditer(r"\*", inp[i])
    for match in gear_match_generator:
        gear_locs.append((match.start(), i))
for gear in gear_locs:
    val += gear_ratio(gear, num_locs)
print(val)




    






