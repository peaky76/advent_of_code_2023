# Day 12: Hot Springs
import functools
from math import prod
import sys

sys.path.append("..")

from advent_of_code_2023 import read_input  # noqa: E402


# @functools.cache
def number_of_arrangements(condition_list, contiguous_groups):
    if not contiguous_groups:
        if "#" not in condition_list:
            # This will return true even if record is empty, which is valid
            return 1
        else:
            # More damaged springs that we can't fit
            return 0
        # return int("#" not in condition_list)

    if not condition_list:
        return 0

    next_char = condition_list[0]
    next_group = contiguous_groups[0]

    def dot():
        return number_of_arrangements(condition_list[1:], contiguous_groups)

    def hash():
        # If the first is a pound, then the first n characters must be
        # able to be treated as a pound, where n is the first group number
        this_group = condition_list[:next_group]
        this_group = this_group.replace("?", "#")

        # If the next group can't fit all the damaged springs, then abort
        if this_group != next_group * "#":
            return 0

        # If the rest of the record is just the last group, then we're
        # done and there's only one possibility
        if len(condition_list) == next_group:
            # Make sure this is the last group
            if len(contiguous_groups) == 1:
                # We are valid
                return 1
            else:
                # There's more groups, we can't make it work
                return 0

        # Make sure the character that follows this group can be a seperator
        if condition_list[next_group] in "?.":
            # It can be seperator, so skip it and reduce to the next group
            return number_of_arrangements(
                condition_list[next_group + 1 :], contiguous_groups[1:]
            )

        # Can't be handled, there are no possibilites
        return 0

    if next_char == "#":
        # Test pound logic
        out = hash()

    elif next_char == ".":
        # Test dot logic
        out = dot()

    elif next_char == "?":
        # This character could be either character, so we'll explore both
        # possibilities
        out = dot() + hash()

    else:
        raise RuntimeError

    # Help with debugging
    print(condition_list, contiguous_groups, "->", out)
    return out

    # if len(contiguous_groups) == 1 and all(x in ["?", "#"] for x in condition_list):
    #     return sum(
    #         condition_list.count("#") == condition_list[i : i + size].count("#")
    #         for i in range(0, len(condition_list) - size + 1)
    #     )

    # chunks = [x for x in condition_list.split(".") if x]

    # if len(chunks) == len(contiguous_groups):
    #     return prod(
    #         number_of_arrangements(chunk, [group])
    #         for chunk, group in list(zip(chunks, contiguous_groups))
    #     )

    # if len(contiguous_groups) == 1:
    #     return sum(
    #         number_of_arrangements(chunk, [contiguous_groups[0]]) for chunk in chunks
    #     )

    # if all(x == "?" for x in condition_list):
    #     return sum(
    #         number_of_arrangements(condition_list[i + 1 :], contiguous_groups[1:])
    #         for i in range(size, len(condition_list) - size + 1)
    #     )

    # do_it = False
    # if len(chunks) < len(contiguous_groups):
    #     the_break = 1
    #     while the_break < len(contiguous_groups):
    #         after = number_of_arrangements(
    #             ".".join(chunks[1:]), contiguous_groups[the_break:]
    #         )
    #         # print("====")
    #         # print(chunks[1:])
    #         # print(contiguous_groups[the_break:])
    #         # print(after)
    #         if after:
    #             do_it = True
    #             break
    #         else:
    #             the_break += 1

    # if do_it:
    #     # print(
    #     #     f"ok for break at {the_break} for {condition_list} and {contiguous_groups}"
    #     # )
    #     # print(the_break)
    #     # print(f"I'm calculating for {chunks[0]} and {contiguous_groups[:the_break]}")
    #     before = number_of_arrangements(chunks[0], contiguous_groups[:the_break])
    #     return prod([before, after])

    # # i = 1
    # # print(chunks)
    # # print(contiguous_groups)
    # # while len(chunks) > 1 and not number_of_arrangements('.'.join(chunks[1:]), contiguous_groups[i:]):
    # # print(chunks[1:])
    # # print(contiguous_groups[i:])
    # #     i += 1
    # #     print("-----")
    # #     print(i)

    # # if i > 1 and (x:= number_of_arrangements(chunks[0], contiguous_groups[:i])):
    # #     print("EXITING---")
    # #     print(chunks[0])
    # #     print(contiguous_groups[:i])
    # #     return prod([x, number_of_arrangements('.'.join(chunks[1:]), contiguous_groups[i:])])
    # # return prod([number_of_arrangements(chunks[0], contiguous_groups[:i]), number_of_arrangements(''.join(chunks[1:]), contiguous_groups[i:])])

    # # print(chunks)
    # # print(contiguous_groups)

    # # i = 0
    # # while (x:= number_of_arrangements(chunks[0], contiguous_groups[:i+1])) and (y:= number_of_arrangements(''.join(chunks[1:]), contiguous_groups[i+1:])):
    # #     print(chunks[0])
    # #     print(''.join(chunks[1:]))# print(x)
    # #     # print(y)
    # #     i += 1

    # # if (x := number_of_arrangements(chunks[0], contiguous_groups[:i - 1])):
    # #     return prod([x, number_of_arrangements(''.join(chunks[1:]), contiguous_groups[i - 1:])])
    # # print("I'm doon here noo")

    # the_sum = 0
    # print(f"I'm doon here with {condition_list} and {contiguous_groups}")
    # for number_of_spaces in range(0, len(condition_list)):
    #     the_break = number_of_spaces + contiguous_groups[0]
    #     print(f"Trying {the_break - 1} spaces")
    #     has_gap_in_it = any(x == "." for x in condition_list[:the_break])
    #     has_match_afterwards = (
    #         len(condition_list) > the_break and condition_list[the_break] == "#"
    #     )
    #     already_done = (the_break - 1) - condition_list.index("#") == contiguous_groups[
    #         0
    #     ]
    #     chars_left_to_find = sum(contiguous_groups[1:]) + len(contiguous_groups[1:])
    #     chars_left_in_list = len(condition_list) - (
    #         number_of_spaces + contiguous_groups[0]
    #     )
    #     enough_left = chars_left_to_find <= chars_left_in_list
    #     print(f"Has gap in it? {has_gap_in_it}")
    #     print(f"Has match afterwards? {has_match_afterwards}")
    #     print(f"Already done? {already_done}")
    #     print(
    #         f"Enough left? {enough_left} - {chars_left_to_find} vs {chars_left_in_list}"
    #     )
    #     # if already_done:
    #     #     print("Already done")
    #     #     break
    #     if not has_gap_in_it and not has_match_afterwards and enough_left:
    #         # increment = number_of_arrangements(
    #         #     condition_list[the_break + 1 :], contiguous_groups[1:]
    #         # )
    #         increment = 1
    #         print(
    #             f"I'm breaking at {condition_list[:the_break]} vs {contiguous_groups} with {increment} because I'm comparing {condition_list[the_break + 1:]} with {contiguous_groups[1:]}"
    #         )
    #         the_sum += increment

    # return the_sum


def get_answer(file):
    lines = read_input(file)
    the_sum = 0
    for line in lines:
        print(line)
        answer = number_of_arrangements(
            line.split(" ")[0], tuple(int(x) for x in line.split(" ")[1].split(","))
        )
        print(answer)
        the_sum += answer
    return the_sum
    # return sum([number_of_arrangements(line.split(' ')[0], [int(x) for x in line.split(' ')[1].split(',')]) for line in lines])


# PART ONE
print("PART ONE:")
example_answer = get_answer("./day_12/example_input")
print(f"Example answer: {example_answer}")
# puzzle_answer = get_answer("./day_12/puzzle_input")
# print(f"Puzzle answer: {puzzle_answer}")

# PART TWO
# print("PART TWO:")
# example_answer = the_function("./day_12/example_input")
# print(f"Example answer: {example_answer}")
# puzzle_answer = the_function("./day_12/puzzle_input")
# print(f"Puzzle answer: {puzzle_answer}")
