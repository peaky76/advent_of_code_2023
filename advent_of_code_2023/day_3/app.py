# Day 3: Gear Ratios

from math import prod
import re
import sys

sys.path.append("..")

from advent_of_code_2023 import read_input  # noqa: E402


def get_part_numbers(lines):
    part_numbers = []
    current_number = ""
    x = None
    y = None
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if not char.isdigit():
                if current_number != "":
                    part_numbers.append((int(current_number), x, y))
                    current_number = ""
                    x, y = None, None
                continue
            if current_number == "":
                x, y = i, j
            current_number += char

    return part_numbers
        
def get_part_indicators(lines):
    return [(i, j) for i, line in enumerate(lines) for j, char in enumerate(line) if not char.isdigit() and not char == '.']

def has_adjacent_indicator(part_loc_and_len, part_indicators):
    x, y, length = part_loc_and_len
    coords = [(x, i) for i in range(y, y + length)]
    if any(is_adjacent(part_bit, part_indicator) for part_bit in coords for part_indicator in part_indicators):        
        return True
    return False

def is_adjacent(coord_1, coord_2):
    x_1, y_1 = coord_1
    x_2, y_2 = coord_2
    return abs(x_1 - x_2) <= 1 and abs(y_1 - y_2) <= 1

def find_valid_part_numbers(file):
    lines = read_input(file)
    part_numbers = get_part_numbers(lines)
    print(part_numbers)
    part_indicators = get_part_indicators(lines)
    print(part_indicators)
    return [part_number[0] for part_number in part_numbers if has_adjacent_indicator((part_number[1], part_number[2], len(str(part_number[0]))), part_indicators)]

# PART ONE
example_answer = sum(find_valid_part_numbers("./day_3/example_input"))
print(f"Example answer: {example_answer}")
puzzle_answer = sum(find_valid_part_numbers("./day_3/puzzle_input"))
print(f"Puzzle answer: {puzzle_answer}")

# # # PART TWO
# example_answer = the_function(read_input("./day_3/example_input"))
# print(f"Example answer: {example_answer}")
# puzzle_answer = the_function(read_input("./day_3/puzzle_input"))
# print(f"Puzzle answer: {puzzle_answer}")
