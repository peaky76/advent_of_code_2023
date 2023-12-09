# Day 9: Mirage Maintenance

import sys
from operator import add, sub

sys.path.append("..")

from advent_of_code_2023 import read_input  # noqa: E402

def get_diffs(line):
    return [n - line[i] for i, n in enumerate(line[1:])]

def extrapolate(line, *, forwards=True):
    idx = -1 if forwards else 0
    op = add if forwards else sub
    diffs = get_diffs(line)
    return op(line[idx], 0 if not sum(diffs) else extrapolate(diffs, forwards=forwards))

def sum_extrapolate_values(file, *, forwards = True):
    lines = read_input(file)
    return sum(extrapolate([int(x) for x in line.split(" ")], forwards=forwards) for line in lines) 

# # PART ONE
print("PART ONE:")
example_answer = sum_extrapolate_values("./day_9/example_input")
print(f"Example answer: {example_answer}")
puzzle_answer = sum_extrapolate_values("./day_9/puzzle_input")
print(f"Puzzle answer: {puzzle_answer}")

# # PART TWO
print("PART TWO:")
example_answer = sum_extrapolate_values("./day_9/example_input", forwards = False)
print(f"Example answer: {example_answer}")
puzzle_answer = sum_extrapolate_values("./day_9/puzzle_input", forwards = False)
print(f"Puzzle answer: {puzzle_answer}")
