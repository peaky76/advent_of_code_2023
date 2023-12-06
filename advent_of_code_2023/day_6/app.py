# Day 6: Wait For It
from math import prod
import sys

sys.path.append("..")

from advent_of_code_2023 import read_input  # noqa: E402

def get_times_and_distances(lines, *, bad_kerning = False):
    to_zip = []
    to_replace = " " if bad_kerning else "  "
    replacement = "" if bad_kerning else " "
    split_char = ":" if bad_kerning else " "
    for line in lines:
        while "  " in line:
            line = line.replace(to_replace, replacement)
        to_zip.append([int(x) for x in line.split(split_char)[1:]])
    return list(zip(*to_zip))

def possible_distances(time):
    return [i * (time - i) for i in range(time + 1)]

def num_ways_to_win(time, record):
    return len([x for x in possible_distances(time) if x > record])

def calculate_margin_of_error(file, *, bad_kerning = False):
    lines = read_input(file)
    return prod([num_ways_to_win(time, distance) for time, distance in get_times_and_distances(lines, bad_kerning=bad_kerning)])

# PART ONE
example_answer = calculate_margin_of_error("./day_6/example_input")
print(f"Example answer: {example_answer}")
puzzle_answer = calculate_margin_of_error("./day_6/puzzle_input")
print(f"Puzzle answer: {puzzle_answer}")

# PART TWO
example_answer = calculate_margin_of_error("./day_6/example_input", bad_kerning=True)
print(f"Example answer: {example_answer}")
puzzle_answer = calculate_margin_of_error("./day_6/puzzle_input", bad_kerning=True)
print(f"Puzzle answer: {puzzle_answer}")
