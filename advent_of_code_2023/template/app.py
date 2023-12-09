# Day X:

import sys

sys.path.append("..")

from advent_of_code_2023 import read_input  # noqa: E402


def the_function(file):
    lines = read_input(file)


# PART ONE
print("PART ONE:")
example_answer = the_function("./day_x/example_input")
print(f"Example answer: {example_answer}")
puzzle_answer = the_function("./day_x/puzzle_input")
print(f"Puzzle answer: {puzzle_answer}")

# PART TWO
print("PART TWO:")
example_answer = the_function("./day_x/example_input")
print(f"Example answer: {example_answer}")
puzzle_answer = the_function("./day_x/puzzle_input")
print(f"Puzzle answer: {puzzle_answer}")
