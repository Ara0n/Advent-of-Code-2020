import re
import numpy as np

# Day 1
day1_part1 = lambda input=open("inputs/day1 input", "r"): [int(input.readlines()[i]) * int(input.readlines()[j]) for i in list(range(1, int(len(input.readlines())))) for j in list(range(i)) if int(input.readlines()[i]) + int(input.readlines()[j]) == 2020][0]
day1_part2 = lambda input=open("inputs/day1 input", "r"): [int(input.readlines()[i]) * int(input.readlines()[j]) * int(input.readlines()[k]) for i in list(range(1, int(len(input.readlines())))) for j in list(range(i)) if int(input.readlines()[i]) for k in list(range(j)) if int(input.readlines()[i]) + int(input.readlines()[j]) + int(input.readlines()[k]) == 2020][0]

# Day 2
day2_part1 = lambda input=open("inputs/day2 input", "r"): len(["ok" for line in input.readlines() if re.match(".*: [^"+re.match(r'(\d+)-(\d+) (\w)', line).group(3)+"]*("+re.match(r'(\d+)-(\d+) (\w)', line).group(3)+"[^"+re.match(r'(\d+)-(\d+) (\w)', line).group(3)+"]*)"+"{"+re.match(r'(\d+)-(\d+) (\w)', line).group(1)+","+re.match(r'(\d+)-(\d+) (\w)', line).group(2)+"}$", line)])
day2_part2 = lambda input=open("inputs/day2 input", "r"): len(["ok" for line in input.readlines() if re.match("^.*: ((?=.{"+re.match(r'(\d+)-(\d+) (\w)', line).group(1)+"}(?<="+re.match(r'(\d+)-(\d+) (\w)', line).group(3)+"))(?=.{"+re.match(r'(\d+)-(\d+) (\w)', line).group(2)+"}(?<!"+re.match(r'(\d+)-(\d+) (\w)', line).group(3)+"))|(?=.{"+re.match(r'(\d+)-(\d+) (\w)', line).group(1)+"}(?<!"+re.match(r'(\d+)-(\d+) (\w)', line).group(3)+"))(?=.{"+re.match(r'(\d+)-(\d+) (\w)', line).group(2)+"}(?<="+re.match(r'(\d+)-(\d+) (\w)', line).group(3)+")))", line)])

# Day 3
day3_part1 = lambda input=open("inputs/day3 input", "r"): len(["bonk!" for i, row in enumerate(input) if row.rstrip("\n")[3 * i % len(row.rstrip("\n"))] == "#"])
day3_part2 = lambda input=open("inputs/day3 input", "r"): np.prod([len(["bonk!" for i, row in enumerate(input) if i%slope[1]==0 and row.rstrip("\n")[slope[0]*i//slope[1] % len(row.rstrip("\n"))] == "#"]) for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]])

# Day 4
day4_part1 = lambda input=open("inputs/day4 input", "r"): len(["ok" for doc in input.read().split("\n\n") if re.match("^(?=.*byr)(?=.*iyr)(?=.*eyr)(?=.*hgt)(?=.*hcl)(?=.*ecl)(?=.*pid).*$", doc.replace("\n", " "))])
day4_part2 = lambda input=open("inputs/day4 input", "r"): len(["ok" for doc in input.read().split("\n\n") if re.match("^(?=.*byr:(19[2-9]\d|200[0-2])( |$))(?=.*iyr:(201\d|2020)( |$))(?=.*eyr:(202\d|2030)( |$))(?=.*hgt:((1[5-8]\d|19[0-3])cm|(59|6\d|7[0-6])in)( |$))(?=.*hcl:#[\da-f]{6}( |$))(?=.*ecl:(amb|blu|brn|gry|grn|hzl|oth)( |$))(?=.*pid:\d{9}( |$)).*$", doc.replace("\n", " "))])

# Day 5
def day5_long():
    with open("inputs/day5 input", "r") as f:
        data = f.readlines()
    seat_id = []

    for boardpass in data:
        row = [i for i in range(128)]
        seat = [i for i in range(8)]

        for letter in boardpass:
            if letter == "F":
                row = row[:len(row)//2]
            elif letter == "B":
                row = row[len(row)//2:]
            elif letter == "L":
                seat = seat[:len(seat)//2]
            elif letter == "R":
                seat = seat[len(seat)//2:]

        seat_id.append(row[0] * 8 + seat[0])

    return seat_id

def day5_part1_long():
    return max(day5_long())

def day5_part2_long():
    boardpasses = day5_long()
    valid_ids = [id for id in boardpasses if id > (0*8+7) and id < (127*8+0)]
    valid_ids.sort()

    for i in range(len(valid_ids)-1):
        if valid_ids[i]+1 != valid_ids[i+1]:
            return valid_ids[i]+1


# Day 6
day6_part1 = lambda input=open("inputs/day6 input", "r"): sum([len(set(string.replace("\n", ""))) for string in input.read().split("\n\n")])
day6_part2 = lambda input=open("inputs/day6 input", "r"): sum([len([set(sheet) for sheet in group.splitlines()][0].intersection(*[set(sheet) for sheet in group.splitlines()])) for group in input.read().split("\n\n")])
