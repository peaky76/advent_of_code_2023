# Day 4: Scratchcards

import sys

sys.path.append("..")

from advent_of_code_2023 import read_input  # noqa: E402

def parse_line(line):
    return {
        "card": int(line.split(":")[0].split("Card ")[1]),
        "winning_nums": [int(num) for num in line.split(":")[1].split("|")[0].split()],
        "selected_nums": [int(num) for num in line.split(":")[1].split("|")[1].split()],
    }    

def calculate_points(scratchcard):
    wins = sum(num in scratchcard["winning_nums"] for num in scratchcard["selected_nums"])
    return 1 * (2 ** (wins  - 1)) if wins else 0

def assess_scratchcards(file):
    lines = read_input(file)
    scratchcards = [parse_line(line) for line in lines]
    return sum(calculate_points(scratchcard) for scratchcard in scratchcards)

# PART ONE
example_answer = assess_scratchcards("./day_4/example_input")
print(f"Example answer: {example_answer}")
puzzle_answer = assess_scratchcards("./day_4/puzzle_input")
print(f"Puzzle answer: {puzzle_answer}")

# PART TWO
# example_answer = the_function("./day_4/example_input")
# print(f"Example answer: {example_answer}")
# puzzle_answer = the_function("./day_4/puzzle_input")
# print(f"Puzzle answer: {puzzle_answer}")
