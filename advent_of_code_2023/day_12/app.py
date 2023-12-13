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

    do_it = False
    if len(chunks) < len(contiguous_groups):
        the_break = 1
        while the_break < len(contiguous_groups):             
            after = number_of_arrangements('.'.join(chunks[1:]), contiguous_groups[the_break:])
            print("====")
            print(chunks[1:])
            print(contiguous_groups[the_break:])
            print(after)
            if after:
                do_it = True
                break
            else:            
                the_break += 1
            
    if do_it:
        print(f"ok for break at {the_break} for {condition_list} and {contiguous_groups}")
        print(the_break)
        print(f"I'm calculating for {chunks[0]} and {contiguous_groups[:the_break]}")
        before = number_of_arrangements(chunks[0], contiguous_groups[:the_break])
        return prod([before, after])

    # i = 1
    # print(chunks)
    # print(contiguous_groups)
    # while len(chunks) > 1 and not number_of_arrangements('.'.join(chunks[1:]), contiguous_groups[i:]):
        # print(chunks[1:])
        # print(contiguous_groups[i:])
    #     i += 1
    #     print("-----")
    #     print(i)
    
   
    # if i > 1 and (x:= number_of_arrangements(chunks[0], contiguous_groups[:i])):
    #     print("EXITING---")
    #     print(chunks[0])
    #     print(contiguous_groups[:i])
    #     return prod([x, number_of_arrangements('.'.join(chunks[1:]), contiguous_groups[i:])]) 
    # return prod([number_of_arrangements(chunks[0], contiguous_groups[:i]), number_of_arrangements(''.join(chunks[1:]), contiguous_groups[i:])])


    # print(chunks)
    # print(contiguous_groups)
    

    # i = 0
    # while (x:= number_of_arrangements(chunks[0], contiguous_groups[:i+1])) and (y:= number_of_arrangements(''.join(chunks[1:]), contiguous_groups[i+1:])):
    #     print(chunks[0])
    #     print(''.join(chunks[1:]))# print(x)
    #     # print(y)
    #     i += 1


    # if (x := number_of_arrangements(chunks[0], contiguous_groups[:i - 1])):
    #     return prod([x, number_of_arrangements(''.join(chunks[1:]), contiguous_groups[i - 1:])])
    print("I'm doon here noo")

    for i in range(0, len(chunks[0]) + 1):  
        new_chunk = chunks[0][:i]
        print(new_chunk)
        if '#' in new_chunk and len(new_chunk) - new_chunk.index('#') == contiguous_groups[0]:
            if new_chunk == chunks[0]:
                if len(contiguous_groups) > 1 and sum(contiguous_groups[1:]) <= sum(x in ['?', '#'] for x in condition_list[i+1:]):
                    return 1
            return number_of_arrangements(condition_list[i+1:], contiguous_groups[1:])

    return 0 

def get_answer(file):
    lines = read_input(file)
    the_sum = 0
    for line in lines:
        print(line)
        answer = number_of_arrangements(line.split(' ')[0], [int(x) for x in line.split(' ')[1].split(',')])
        print(answer)
        the_sum += answer
    return the_sum
    # return sum([number_of_arrangements(line.split(' ')[0], [int(x) for x in line.split(' ')[1].split(',')]) for line in lines])

# PART ONE
print("PART ONE:")
example_answer = get_answer("./day_12/example_input")
print(f"Example answer: {example_answer}")
puzzle_answer = get_answer("./day_12/puzzle_input")
print(f"Puzzle answer: {puzzle_answer}")

# PART TWO
# print("PART TWO:")
# example_answer = the_function("./day_12/example_input")
# print(f"Example answer: {example_answer}")
# puzzle_answer = the_function("./day_12/puzzle_input")
# print(f"Puzzle answer: {puzzle_answer}")
