# Day 8: Haunted Wasteland
from math import lcm
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

def follow_multi_path(lr_instructions, wasteland_map):
    start_locations = [key for key in wasteland_map.keys() if key[-1] == "A"]
    destination_locations = [key for key in wasteland_map.keys() if key[-1] == "Z"]
    
    moves_dictionary = {key: {key: [] for key in destination_locations} for key in start_locations}
    
    for location in start_locations:
        steps = 0
        instruction_index = 0  
        current_location = location
        while not any(len(val) == 2 for val in moves_dictionary[location].values()):
            steps += 1
            move = int(lr_instructions[instruction_index % len(lr_instructions)])
            current_location = wasteland_map[current_location][move]
            if current_location in destination_locations:
                moves_dictionary[location][current_location].append(steps)
            instruction_index += 1
  
    loops = [moves[0] for val in moves_dictionary.values() for moves in val.values() if len(moves) == 2]  

    return lcm(*loops)

def get_step_count(file, *, use_ghosts=False):
    lines = read_input(file)
    lr_instructions = lr_to_binary_str(lines[0])
    wasteland_map = { k: v for line in lines[2:] for k, v in map_line_to_dict(line).items() }
    follow_fn = follow_multi_path if use_ghosts else follow_path
    steps = follow_fn(lr_instructions, wasteland_map)
    return steps

# PART ONE
example_1_answer = get_step_count("./day_8/example_input_1")
print(f"Part 1 Example 1 answer: {example_1_answer}")
example_2_answer = get_step_count("./day_8/example_input_2")
print(f"Part 1 Example 2 answer: {example_2_answer}")
puzzle_answer = get_step_count("./day_8/puzzle_input")
print(f"Part 1 Puzzle answer: {puzzle_answer}")

# # PART TWO
example_answer = get_step_count("./day_8/example_input_3", use_ghosts=True)
print(f"Part 2 Example answer: {example_answer}")
puzzle_answer = get_step_count("./day_8/puzzle_input", use_ghosts=True)
print(f"Part 2 Puzzle answer: {puzzle_answer}")

# lines = read_input("./day_8/puzzle_input")
# wasteland_map = { k: v for line in lines[2:] for k, v in map_line_to_dict(line).items() }
# print([key for key in wasteland_map.keys() if key[-1] == "A"])
# print([key for key in wasteland_map.keys() if key[-1] == "Z"])