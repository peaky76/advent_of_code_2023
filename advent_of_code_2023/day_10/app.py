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


def get_continuous_ranges(y_values):
    continuous_ranges = []
    if y_values:
        range_start = y_values[0]
        range_end = y_values[0]
        if len(y_values) > 1:
            for i, y in enumerate(y_values[1:]):
                if y - y_values[i] > 1:
                    continuous_ranges.append((range_start, range_end + 1))
                    range_start = y
                range_end = y

        continuous_ranges.append((range_start, range_end + 1))

    return continuous_ranges


def is_connected(the_map, loc, other_loc):
    return loc in the_map[other_loc] and other_loc in the_map[loc]


def is_within_left_bounds(steps, test_loc):
    x, y = test_loc
    return any([loc for loc in steps if loc[0] == x and loc[1] < y])


def has_lower_link(the_map, loc):
    return (loc[0] + 1, loc[1]) in the_map.get(loc, [])


def has_upper_link(the_map, loc):
    return (loc[0] - 1, loc[1]) in the_map.get(loc, [])


def is_enclosed(the_map, steps, test_loc):
    x, y = test_loc
    map_locs_to_right = sorted([loc for loc in steps if loc[0] == x and loc[1] > y])

    num_of_crossing_pipes = 0
    looking_for = None
    for loc in map_locs_to_right:
        upper_link = has_upper_link(the_map, loc)
        lower_link = has_lower_link(the_map, loc)
        if upper_link and lower_link:
            num_of_crossing_pipes += 1
        elif upper_link:
            if looking_for == "upper":
                num_of_crossing_pipes += 1
                looking_for = None
            else:
                looking_for = "lower"
        elif lower_link:
            if looking_for == "lower":
                num_of_crossing_pipes += 1
                looking_for = None
            else:
                looking_for = "upper"

    return is_within_left_bounds(steps, test_loc) and num_of_crossing_pipes % 2 == 1


def create_map(lines):
    return {
        (i, j): convert_symbol_to_exits((i, j), symbol)
        for i, line in enumerate(lines)
        for j, symbol in enumerate(line)
    }


def follow_loop(the_map):
    start = next(key for key, value in the_map.items() if len(value) == 4)
    prev_loc = start
    current_loc = next(val for val in the_map[start] if start in the_map.get(val, []))
    steps = [current_loc]
    while current_loc != start:
        next_loc = next(val for val in the_map[current_loc] if val != prev_loc)
        steps.append(next_loc)
        prev_loc = current_loc
        current_loc = next_loc

    return steps


def count_furthest_point(file):
    lines = read_input(file)
    the_map = create_map(lines)
    return len(follow_loop(the_map)) // 2


def count_enclosed(file):
    lines = read_input(file)
    the_map = create_map(lines)
    steps = follow_loop(the_map)
    start = next(key for key, value in the_map.items() if len(value) == 4)

    x_max = len(lines)
    y_max = len(lines[0])

    enclosed_count = 0
    looking_for = None
    for x in range(0, x_max):
        in_loop = False
        for y in range(0, y_max):
            loc = (x, y)
            if loc in steps:
                if loc == start:
                    lower_link = has_upper_link(the_map, (loc[0] + 1, loc[1]))
                    upper_link = has_lower_link(the_map, (loc[0] - 1, loc[1]))
                else:
                    lower_link = has_lower_link(the_map, loc)
                    upper_link = has_upper_link(the_map, loc)
                is_pipe = loc != start and lower_link and upper_link
                switch = (
                    is_pipe
                    or (looking_for == "lower" and lower_link)
                    or (looking_for == "upper" and upper_link)
                )

                if switch:
                    in_loop = not in_loop
                    looking_for = None
                else:
                    if looking_for == "lower":
                        looking_for = None if upper_link else "lower"
                    elif looking_for == "upper":
                        looking_for = None if lower_link else "upper"
                    else:
                        looking_for = "lower" if upper_link else "upper"

            else:
                if in_loop:
                    enclosed_count += 1

    return enclosed_count

    # TODO: Figure out why this does not work
    # possibles = [(x, y) for x in range(0, x_max) for y in range(0, y_max) if (x, y) not in steps]
    # return sum([is_enclosed(the_map, steps, possible) for possible in possibles])


# # PART ONE
# print("PART ONE:")
# example_1_answer = count_furthest_point("./day_10/example_input_1")
# print(f"Example 1 answer: {example_1_answer}")
# example_2_answer = count_furthest_point("./day_10/example_input_2")
# print(f"Example 2 answer: {example_2_answer}")
# puzzle_answer = count_furthest_point("./day_10/puzzle_input")
# print(f"Puzzle answer: {puzzle_answer}")

# # PART TWO
# print("PART TWO:")
# example_3_answer = count_enclosed("./day_10/example_input_3")
# print(f"Example 3 answer: {example_3_answer}")
# example_4_answer = count_enclosed("./day_10/example_input_4")
# print(f"Example 4 answer: {example_4_answer}")
# example_5_answer = count_enclosed("./day_10/example_input_5")
# print(f"Example 5 answer: {example_5_answer}")
# puzzle_answer = count_enclosed("./day_10/puzzle_input")
# print(f"Puzzle answer: {puzzle_answer}")
