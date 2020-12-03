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
