# Day 11: Cosmic Expansion
from itertools import combinations
import sys

sys.path.append("..")

from advent_of_code_2023 import read_input  # noqa: E402


def manhattan_distance(point_1, point_2):
    x1, y1 = point_1
    x2, y2 = point_2
    return abs(x2 - x1) + abs(y2 - y1)  #


def cols_of_empty_space(lines):
    return [i for i, col in enumerate(zip(*lines)) if all(x == "." for x in col)]


def rows_of_empty_space(lines):
    return [i for i, row in enumerate(lines) if all(x == "." for x in row)]


def get_galaxies(lines):
    return [
        (x, y) for x, row in enumerate(lines) for y, col in enumerate(row) if col == "#"
    ]


def sum_shortest_paths(file, *, expansion_size=2):
    lines = read_input(file)
    empty_cols = cols_of_empty_space(lines)
    empty_rows = rows_of_empty_space(lines)
    galaxies = get_galaxies(lines)
    galaxy_pairs = list(combinations(galaxies, 2))

    shortest_distance_sum = 0
    for galaxy_1, galaxy_2 in galaxy_pairs:
        min_x, max_x = sorted((galaxy_1[0], galaxy_2[0]))
        min_y, max_y = sorted((galaxy_1[1], galaxy_2[1]))
        horizontal_expansion = sum(x in range(min_x, max_x) for x in empty_rows) * (
            expansion_size - 1
        )
        vertical_expansion = sum(y in range(min_y, max_y) for y in empty_cols) * (
            expansion_size - 1
        )
        shortest_distance = (
            manhattan_distance(galaxy_1, galaxy_2)
            + horizontal_expansion
            + vertical_expansion
        )
        # print(f"{galaxy_1} -> {galaxy_2} -> {min_x, max_x} -> { min_y, max_y} = {manhattan_distance(galaxy_1, galaxy_2)} + {horizontal_expansion} + {vertical_expansion} = {shortest_distance}")
        shortest_distance_sum += shortest_distance

    return shortest_distance_sum


# # PART ONE
# print("PART ONE:")
# example_answer = sum_shortest_paths("./day_11/example_input")
# print(f"Example answer: {example_answer}")
# puzzle_answer = sum_shortest_paths("./day_11/puzzle_input")
# print(f"Puzzle answer: {puzzle_answer}")

# # PART TWO
# print("PART TWO:")
# example_answer_10 = sum_shortest_paths("./day_11/example_input", expansion_size=10)
# print(f"Example answer (10 times bigger): {example_answer_10}")
# example_answer_100 = sum_shortest_paths("./day_11/example_input", expansion_size=100)
# print(f"Example answer (100 times bigger): {example_answer_100}")
# puzzle_answer = sum_shortest_paths("./day_11/puzzle_input", expansion_size=1000000)
# print(f"Puzzle answer: {puzzle_answer}")
