# Day 6: Wait For It
from math import prod
import sys

sys.path.append("..")

from advent_of_code_2023 import read_input  # noqa: E402

def get_times_and_distances(lines):
    to_zip = []
    for line in lines:
        while "  " in line:
            line = line.replace("  ", " ")
        to_zip.append([int(x) for x in line.split(" ")[1:]])
    return list(zip(*to_zip))

def possible_distances(time):
    return [i * (time - i) for i in range(time + 1)]

def num_ways_to_win(time, record):
    return len([x for x in possible_distances(time) if x > record])

def calculate_margin_of_error(file):
    lines = read_input(file)
    return prod([num_ways_to_win(time, distance) for time, distance in get_times_and_distances(lines)])

# PART ONE
example_answer = calculate_margin_of_error("./day_6/example_input")
print(f"Example answer: {example_answer}")
puzzle_answer = calculate_margin_of_error("./day_6/puzzle_input")
print(f"Puzzle answer: {puzzle_answer}")

# PART TWO
example_answer = calculate_margin_of_error("./day_6/example_input")
print(f"Example answer: {example_answer}")
puzzle_answer = calculate_margin_of_error("./day_6/puzzle_input")
print(f"Puzzle answer: {puzzle_answer}")
