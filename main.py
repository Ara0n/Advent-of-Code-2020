# Day 1
day1_part1 = lambda: [int(open("day1 input", "r").readlines()[i]) * int(open("day1 input", "r").readlines()[j]) for i in list(range(1, int(len(open("day1 input", "r").readlines())))) for j in list(range(i)) if int(open("day1 input", "r").readlines()[i]) + int(open("day1 input", "r").readlines()[j]) == 2020][0]
day1_part2 = lambda: [int(open("day1 input", "r").readlines()[i]) * int(open("day1 input", "r").readlines()[j]) * int(open("day1 input", "r").readlines()[k]) for i in list(range(1, int(len(open("day1 input", "r").readlines())))) for j in list(range(i)) if int(open("day1 input", "r").readlines()[i]) for k in list(range(j)) if int(open("day1 input", "r").readlines()[i]) + int(open("day1 input", "r").readlines()[j]) + int(open("day1 input", "r").readlines()[k]) == 2020][0]

