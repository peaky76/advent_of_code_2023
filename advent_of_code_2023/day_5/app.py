# Day 5: If You Give A Seed A Fertilizer

import sys

sys.path.append("..")

from advent_of_code_2023 import read_input  # noqa: E402

def create_map_function(mappings):
    def map_function(seed):
        for mapping in mappings:
            if mapping[0] <= seed <= mapping[1]:
                return seed + mapping[2]
        return seed

    return map_function

def get_paras(lines):
    paras = []
    para = []
    for line in lines:
        if line is None:
            paras.append(parse_para(para))
            para = []
        else:
            para.append(line)
    paras.append(parse_para(para))
    return paras

def parse_input(file):
    lines = read_input(file)
    starter_seeds = [int(x) for x in lines[0].split('seeds: ')[1].split(" ")]
    paras = get_paras(lines[2:])
    mapping_dictionary = {para[0]: (para[1], para[2]) for para in paras}

    function_chain = []
    dictionary_key = 'seed'
    while dictionary_key != 'location':
        function_chain.append(mapping_dictionary[dictionary_key][1])
        dictionary_key = mapping_dictionary[dictionary_key][0]

    locations = []
    for seed in starter_seeds:
        for function in function_chain:
            seed = function(seed)
        locations.append(seed)

    return locations

def parse_line(line):
    destination_start, source_start, range_length = (int(x) for x in line.split(" "))
    return (source_start, source_start + range_length - 1, destination_start - source_start)

def parse_para(para):
    title = parse_title(para[0])
    map_function = create_map_function([parse_line(line) for line in para[1:]])
    return (*title, map_function)

def parse_title(title):
    return tuple(title.split(" map")[0].split("-to-"))

# def the_function(file):
#     lines = read_input(file)
    

# PART ONE
example_answer = min(parse_input("./day_5/example_input"))
print(f"Example answer: {example_answer}")
puzzle_answer = min(parse_input("./day_5/puzzle_input"))
print(f"Puzzle answer: {puzzle_answer}")

# PART TWO
# example_answer = the_function("./day_5/example_input")
# print(f"Example answer: {example_answer}")
# puzzle_answer = the_function("./day_5/puzzle_input")
# print(f"Puzzle answer: {puzzle_answer}")
