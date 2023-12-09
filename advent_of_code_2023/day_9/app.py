# Day 9: Mirage Maintenance

import sys

sys.path.append("..")

from advent_of_code_2023 import read_input  # noqa: E402

def extrapolate_value(line):
    pass

def extrapolate_values(lines):
    return [extrapolate_value(line) for line in lines]

def sum_extrapolate_values(file):
    lines = read_input(file)
    return sum(extrapolate_values(lines)) 

# PART ONE
print("PART ONE:")
example_answer = sum_extrapolate_values("./day_9/example_input")
print(f"Example answer: {example_answer}")
puzzle_answer = sum_extrapolate_values("./day_9/puzzle_input")
print(f"Puzzle answer: {puzzle_answer}")

# PART TWO
print("PART TWO:")
example_answer = sum_extrapolate_values("./day_9/example_input")
print(f"Example answer: {example_answer}")
puzzle_answer = sum_extrapolate_values("./day_9/puzzle_input")
print(f"Puzzle answer: {puzzle_answer}")
