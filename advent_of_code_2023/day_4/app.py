# Day 4: Scratchcards

import sys

sys.path.append("..")

# from advent_of_code_2023 import read_input  # noqa: E402

def parse_line(line):
    return {
        "card": int(line.split(":")[0].split("Card ")[1]),
        "winning_nums": [int(num) for num in line.split(":")[1].split("|")[0].split()],
        "selected_nums": [int(num) for num in line.split(":")[1].split("|")[1].split()],
    }    

# PART ONE
# example_answer = the_function("./day_4/example_input")
# print(f"Example answer: {example_answer}")
# puzzle_answer = the_function("./day_4/puzzle_input")
# print(f"Puzzle answer: {puzzle_answer}")

# PART TWO
# example_answer = the_function("./day_4/example_input")
# print(f"Example answer: {example_answer}")
# puzzle_answer = the_function("./day_4/puzzle_input")
# print(f"Puzzle answer: {puzzle_answer}")
