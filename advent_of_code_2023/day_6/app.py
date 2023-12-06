# Day 6: Wait For It

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

# PART ONE
example_answer = get_times_and_distances(read_input("./day_6/example_input"))
print(f"Example answer: {example_answer}")
puzzle_answer = get_times_and_distances(read_input("./day_6/puzzle_input"))
print(f"Puzzle answer: {puzzle_answer}")

# PART TWO
example_answer = get_times_and_distances(read_input("./day_6/example_input"))
print(f"Example answer: {example_answer}")
puzzle_answer = get_times_and_distances(read_input("./day_6/puzzle_input"))
print(f"Puzzle answer: {puzzle_answer}")
