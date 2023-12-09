# Day 9: Mirage Maintenance

import sys

sys.path.append("..")

from advent_of_code_2023 import read_input  # noqa: E402

def get_diffs(line):
    return [n - line[i] for i, n in enumerate(line[1:])]

def extrapolate_backwards(line):
    if all(diff == 0 for diff in get_diffs(line)):
        return line[0] - 0
    else:
        return line[0] - extrapolate_backwards(get_diffs(line))

def extrapolate_forwards(line):
    if all(diff == 0 for diff in get_diffs(line)):
        return line[-1] + 0
    else:
        return line[-1] + extrapolate_forwards(get_diffs(line))

def sum_extrapolate_values(file, *, forwards = True):
    lines = read_input(file)
    extrapolate_fn = extrapolate_forwards if forwards else extrapolate_backwards
    return sum(extrapolate_fn([int(x) for x in line.split(" ")]) for line in lines) 

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
