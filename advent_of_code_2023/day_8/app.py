# Day 8: Haunted Wasteland

import sys

sys.path.append("..")

from advent_of_code_2023 import read_input  # noqa: E402

# def the_function(file):
#     lines = read_input(file)


def lr_to_binary_str(lr):
    return lr.replace("L", "0").replace("R", "1")

def map_line_to_dict(line): 
    key, val = line.split(" = ")
    return {key: val.replace("(","").replace(")","").split(", ")}

def follow_path(lr_instructions, wasteland_map):
    current_location = "AAA"
    steps = 0
    instruction_index = 0
    while current_location != "ZZZ":    
        steps += 1
        move = int(lr_instructions[instruction_index % len(lr_instructions)])
        current_location = wasteland_map[current_location][move]
        instruction_index += 1

    return steps

def get_step_count(file):
    lines = read_input(file)
    lr_instructions = lr_to_binary_str(lines[0])
    wasteland_map = { k: v for line in lines[2:] for k, v in map_line_to_dict(line).items() }
    steps = follow_path(lr_instructions, wasteland_map)
    return steps

# PART ONE
example_1_answer = get_step_count("./day_8/example_input_1")
print(f"Example 1 answer: {example_1_answer}")
example_2_answer = get_step_count("./day_8/example_input_2")
print(f"Example 1 answer: {example_2_answer}")
puzzle_answer = get_step_count("./day_8/puzzle_input")
print(f"Puzzle answer: {puzzle_answer}")

# # PART TWO
# example_answer = the_function("./day_8/example_input")
# print(f"Example answer: {example_answer}")
# puzzle_answer = the_function("./day_8/puzzle_input")
# print(f"Puzzle answer: {puzzle_answer}")
