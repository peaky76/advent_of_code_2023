# Day 12: Hot Springs
from math import prod
import sys

sys.path.append("..")

from advent_of_code_2023 import read_input  # noqa: E402

def number_of_arrangements(condition_list, contiguous_groups):
    size = contiguous_groups[0]
        
    if len(contiguous_groups) == 1 and all(x in ['?', '#'] for x in condition_list):
        return sum(condition_list.count('#') == condition_list[i:i+size].count('#') for i in range(0, len(condition_list) - size + 1))

    chunks = [x for x in condition_list.split('.') if x]
    if len(chunks) == len(contiguous_groups):
        return prod(number_of_arrangements(chunk, [group]) for chunk, group in list(zip(chunks, contiguous_groups)))
    
    if len(contiguous_groups) == 1:
        return sum(number_of_arrangements(chunk, [contiguous_groups[0]]) for chunk in chunks)
    
    if all(x == '?' for x in condition_list):
        return sum(number_of_arrangements(condition_list[i+1:], contiguous_groups[1:]) for i in range(size, len(condition_list) - size + 1))

    for i in range(0, len(chunks[0]) + 1):
        new_chunk = chunks[0][:i]
        if '#' in new_chunk and len(new_chunk) - new_chunk.index('#') == contiguous_groups[0] + 1:
            return number_of_arrangements(condition_list[i:], contiguous_groups[1:])

    i = 1
    while (x:= number_of_arrangements(chunks[0], contiguous_groups[:i])):
        i += 1

    if (x := number_of_arrangements(chunks[0], contiguous_groups[:i - 1])):
        return prod([x, number_of_arrangements(''.join(chunks[1:]), contiguous_groups[i - 1:])])

    return 0 

def get_answer(file):
    lines = read_input(file)
    return sum([number_of_arrangements(line.split(' ')[0], [int(x) for x in line.split(' ')[1].split(',')]) for line in lines])

# PART ONE
print("PART ONE:")
example_answer = get_answer("./day_12/example_input")
print(f"Example answer: {example_answer}")
# puzzle_answer = the_function("./day_12/puzzle_input")
# print(f"Puzzle answer: {puzzle_answer}")

# PART TWO
# print("PART TWO:")
# example_answer = the_function("./day_12/example_input")
# print(f"Example answer: {example_answer}")
# puzzle_answer = the_function("./day_12/puzzle_input")
# print(f"Puzzle answer: {puzzle_answer}")
