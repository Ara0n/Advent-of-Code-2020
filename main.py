import re
import numpy as np

# Day 1
day1_part1 = lambda: [int(open("inputs/day1 input", "r").readlines()[i]) * int(open("inputs/day1 input", "r").readlines()[j]) for i in list(range(1, int(len(open("inputs/day1 input", "r").readlines())))) for j in list(range(i)) if int(open("inputs/day1 input", "r").readlines()[i]) + int(open("inputs/day1 input", "r").readlines()[j]) == 2020][0]
day1_part2 = lambda: [int(open("inputs/day1 input", "r").readlines()[i]) * int(open("inputs/day1 input", "r").readlines()[j]) * int(open("inputs/day1 input", "r").readlines()[k]) for i in list(range(1, int(len(open("inputs/day1 input", "r").readlines())))) for j in list(range(i)) if int(open("inputs/day1 input", "r").readlines()[i]) for k in list(range(j)) if int(open("inputs/day1 input", "r").readlines()[i]) + int(open("inputs/day1 input", "r").readlines()[j]) + int(open("inputs/day1 input", "r").readlines()[k]) == 2020][0]

# Day 2
day2_part1 = lambda: len(["ok" for line in open("inputs/day2 input", "r").readlines() if re.match(".*: [^"+re.match(r'(\d+)-(\d+) (\w)', line).group(3)+"]*("+re.match(r'(\d+)-(\d+) (\w)', line).group(3)+"[^"+re.match(r'(\d+)-(\d+) (\w)', line).group(3)+"]*)"+"{"+re.match(r'(\d+)-(\d+) (\w)', line).group(1)+","+re.match(r'(\d+)-(\d+) (\w)', line).group(2)+"}$", line)])
day2_part2 = lambda: len(["ok" for line in open("inputs/day2 input", "r").readlines() if re.match("^.*: ((?=.{"+re.match(r'(\d+)-(\d+) (\w)', line).group(1)+"}(?<="+re.match(r'(\d+)-(\d+) (\w)', line).group(3)+"))(?=.{"+re.match(r'(\d+)-(\d+) (\w)', line).group(2)+"}(?<!"+re.match(r'(\d+)-(\d+) (\w)', line).group(3)+"))|(?=.{"+re.match(r'(\d+)-(\d+) (\w)', line).group(1)+"}(?<!"+re.match(r'(\d+)-(\d+) (\w)', line).group(3)+"))(?=.{"+re.match(r'(\d+)-(\d+) (\w)', line).group(2)+"}(?<="+re.match(r'(\d+)-(\d+) (\w)', line).group(3)+")))", line)])

# Day 3
day3_part1 = lambda: len(["bonk!" for i, row in enumerate(open("inputs/day3 input", "r")) if row.rstrip("\n")[3 * i % len(row.rstrip("\n"))] == "#"])
day3_part2 = lambda: np.prod([len(["bonk!" for i, row in enumerate(open("inputs/day3 input", "r")) if i%slope[1]==0 and row.rstrip("\n")[slope[0]*i//slope[1] % len(row.rstrip("\n"))] == "#"]) for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]])
