# Day 10: Pipe Haze

import sys

sys.path.append("..")

from advent_of_code_2023 import read_input  # noqa: E402

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

def convert_symbol_to_exits(loc, symbol):
    x, y = loc
    return {
        ".": [],
        "|": [(x - 1, y), (x + 1, y)],
        "-": [(x, y - 1), (x, y + 1)],
        "L": [(x - 1, y), (x, y + 1)],  
        "J": [(x - 1, y), (x, y - 1)],
        "7": [(x + 1, y), (x, y - 1)],
        "F": [(x + 1, y), (x, y + 1)],
        "S": [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)],
    }[symbol]

def is_connected(map, loc, other_loc):
    return loc in map[other_loc] and other_loc in map[loc]

def create_map(lines):
    return {(i, j): convert_symbol_to_exits((i,j), symbol) for i, line in enumerate(lines) for j, symbol in enumerate(line)}

def follow_loop(file):
    lines = read_input(file)
    the_map = create_map(lines)
    start = next(key for key, value in the_map.items() if len(value) == 4)
    steps = 1
    prev_loc = start
    current_loc = next(val for val in the_map[start] if start in the_map[val])
    while current_loc != start:
        steps += 1
        next_loc = next(val for val in the_map[current_loc] if val != prev_loc)
        prev_loc = current_loc
        current_loc = next_loc
    return steps // 2

    
# PART ONE
print("PART ONE:")
example_1_answer = follow_loop("./day_10/example_input_1")
print(f"Example 1 answer: {example_1_answer}")
example_2_answer = follow_loop("./day_10/example_input_2")
print(f"Example 2 answer: {example_2_answer}")
puzzle_answer = follow_loop("./day_10/puzzle_input")
print(f"Puzzle answer: {puzzle_answer}")

# PART TWO
# print("PART TWO:")
# example_answer = the_function("./day_10/example_input")
# print(f"Example answer: {example_answer}")
# puzzle_answer = the_function("./day_10/puzzle_input")
# print(f"Puzzle answer: {puzzle_answer}")
