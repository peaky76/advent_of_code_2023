# Day 5: If You Give A Seed A Fertilizer

import sys

sys.path.append("..")

from advent_of_code_2023 import read_input  # noqa: E402

def create_map_function(lines):
    def map_function(seed):
        for line in lines:
            if line[1] <= seed < line[1] + line[2]:
                diff = line[0] - line[1]
                return seed + diff
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
    
def parse_line(line):
    return [int(x) for x in line.split(" ")]
    
def parse_para(para):
    title = parse_title(para[0])
    lines = [parse_line(line) for line in para[1:]]
    return [*title, lines]

def parse_seeds_line(line, *, as_range=False):
    nums = [int(x) for x in line.split('seeds: ')[1].split(" ")]
    if as_range:
        pairs = zip(nums[::2], nums[1::2])
        return [i + pair[0] for pair in pairs for i in range(pair[1])]
    return nums

def parse_title(title):
    return tuple(title.split(" map")[0].split("-to-"))

def get_min_for_individual_seeds(file):
    lines = read_input(file)
    paras = get_paras(lines[2:])
    mapping_dictionary = {}
    for para in paras:
        mapping_dictionary[para[0]] = (para[1], create_map_function(para[2]))

    function_chain = []
    dictionary_key = 'seed'
    while dictionary_key != 'location':
        function_chain.append(mapping_dictionary[dictionary_key][1])
        dictionary_key = mapping_dictionary[dictionary_key][0]

    locations = []
    for seed in parse_seeds_line(lines[0]):
        for function in function_chain:
            seed = function(seed)
        locations.append(seed)

    return min(locations)

def get_min_for_range_of_seeds(file):
    lines = read_input(file)
    paras = get_paras(lines[2:])
    mapping_dictionary = {}
    for para in paras:
        mapping_dictionary[para[0]] = (para[1], create_map_function(para[2]))

    function_chain = []
    dictionary_key = 'seed'
    while dictionary_key != 'location':
        function_chain.append(mapping_dictionary[dictionary_key][1])
        dictionary_key = mapping_dictionary[dictionary_key][0]

    locations = []
    for seed in parse_seeds_line(lines[0], as_range=True):
        for function in function_chain:
            seed = function(seed)
        locations.append(seed)

    return min(locations)
    
# PART ONE
example_answer = get_min_for_individual_seeds("./day_5/example_input")
print(f"Example answer: {example_answer}")
puzzle_answer = get_min_for_individual_seeds("./day_5/puzzle_input")
print(f"Puzzle answer: {puzzle_answer}")

# PART TWO
example_answer = get_min_for_range_of_seeds("./day_5/example_input")
print(f"Example answer: {example_answer}")
# puzzle_answer = get_min_for_range_of_seeds("./day_5/puzzle_input")
# print(f"Puzzle answer: {puzzle_answer}")
