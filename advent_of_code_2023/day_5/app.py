# Day 5: If You Give A Seed A Fertilizer

import sys

sys.path.append("..")

# from advent_of_code_2023 import read_input  # noqa: E402



def parse_line(line):
    destination_start, source_start, range_length = (int(x) for x in line.split(" "))
    return (source_start, source_start + range_length - 1, destination_start - source_start)

def parse_title(title):
    return tuple(title.split(" map")[0].split("-to-"))

# def the_function(file):
#     lines = read_input(file)
    

# PART ONE
# example_answer = the_function("./day_4/example_input")
# print(f"Example answer: {example_answer}")
# puzzle_answer = the_function("./day_4/puzzle_input")
# print(f"Puzzle answer: {puzzle_answer}")

# PART TWO
# example_answer = the_function("./day_4/example_input")
# print(f"Example answer: {example_answer}")
# puzzle_answer = the_function("./day_4/puzzle_input")
# print(f"Puzzle answer: {puzzle_answer}")
