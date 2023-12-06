#imports for solution setup
import boto3
import env
import json
import os
# imports for the days problem
from operator import itemgetter


#problem url
#https://adventofcode.com/2023/day/5

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

tINP = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""



def data_formatter(inp: str) -> dict:
    data = {}
    sections = inp.split("\n\n")
    # seeds
    data["seeds"] = [int(x) for x in sections[0].split(": ")[1].split(" ") if x != ""]
    # seed-to-soil map
    data["seed-to-soil"] = [[int(y) for y in x.split(" ") if y != ""] for x in sections[1].split("\n")[1:]]
    # soil-to-fertilizer map
    data["soil-to-fertilizer"] = [[int(y) for y in x.split(" ") if y != ""] for x in sections[2].split("\n")[1:]]
    # fertilizer-to-water
    data["fertilizer-to-water"] = [[int(y) for y in x.split(" ") if y != ""] for x in sections[3].split("\n")[1:]]
    # water-to-light
    data["water-to-light"] = [[int(y) for y in x.split(" ") if y != ""] for x in sections[4].split("\n")[1:]]
    # light-to-temperature
    data["light-to-temperature"] = [[int(y) for y in x.split(" ") if y != ""] for x in sections[5].split("\n")[1:]]
    # temperature-to-humidity
    data["temperature-to-humidity"] = [[int(y) for y in x.split(" ") if y != ""] for x in sections[6].split("\n")[1:]]
    # humidity-to-location
    data["humidity-to-location"] = [[int(y) for y in x.split(" ") if y != ""] for x in sections[7].split("\n")[1:]]
    return data

def data_map(val: int, topic: str, data: dict) -> int:
    for map in data[topic]:
        if val in range(map[1], map[1] + map[2]):
            diff = val - map[1]
            return map[0] + diff
    return val

    

#part1
inp = data_formatter(INP)
locations = []
for seed in inp['seeds']:
    for key in list(inp.keys())[1:]:
        seed = data_map(seed, key, inp)
    locations.append(seed)

print(min(locations))



#part2
def conversion(inp: dict) -> dict:
    for key in list(inp.keys())[1:]:
        out = []
        for map in inp[key]:
            m_range = (map[1], map[1] + map[2] - 1)
            m_offset = map[0] - map[1]
            out.append((m_offset, m_range))
        inp[key] = out
    return inp

            


inp = conversion(data_formatter(INP))
inp['seeds'] = [((inp['seeds'][x],inp['seeds'][x] + inp['seeds'][x+1] -1)) for x in range(0,len(inp['seeds']),2)]
lowest = []
for seed_bound in inp['seeds']:
    analyze_this = [seed_bound]
    
    for key in list(inp.keys())[1:]:
        carry_this = []
        while len(analyze_this) > 0:
            current_seed = analyze_this.pop(0)
            for map in inp[key]:

                if map[1][0] > current_seed[1]:
                    # entire map range above seed range
                    continue
                elif map[1][1] < current_seed[0]:
                    # entire map range below seed range
                    continue
                elif map[1][0] <= current_seed[0]:
                    if map[1][1] >= current_seed[1]:
                        # carry entire seed
                        carry_this.append((current_seed[0] + map[0], current_seed[1] + map[0]))
                        break
                    else:
                        # carry left bound seed to right bound map, with map offset added
                        carry_this.append((current_seed[0] + map[0], map[1][1] + map[0]))
                        # put right bound map + 1 to current seed right bound back into the 'analyze' list
                        analyze_this.append((map[1][1] + 1, current_seed[1]))
                        break
                elif map[1][1] >= current_seed[1]:
                    if map[1][0] <= current_seed[0]:
                        # carry entire seed
                        carry_this.append((current_seed[0] + map[0], current_seed[1] + map[0]))
                        break
                    else:
                        # carry left bound of map to right bound of seed, with map offset added
                        carry_this.append((map[1][0] + map[0], current_seed[1] + map[0]))
                        # put left bound seed to left bound map minus 1 back into the 'analyze' list
                        analyze_this.append((current_seed[0], map[1][0] - 1))
                        break
            else:
                # this feels wrong 
                carry_this.append(current_seed)

        analyze_this = [x for x in carry_this]
    lowest.append(sorted(list(set(analyze_this)), key=itemgetter(0))[0])
print(sorted(lowest, key=itemgetter(0))[0][0])


        

    

    










        





    






