# Day 4: Scratchcards

from collections import defaultdict
import sys

sys.path.append("..")

from advent_of_code_2023 import read_input  # noqa: E402


def parse_line(line):
    return {
        "card_id": int(line.split(":")[0].split("Card ")[1]),
        "winning_nums": [int(num) for num in line.split(":")[1].split("|")[0].split()],
        "selected_nums": [int(num) for num in line.split(":")[1].split("|")[1].split()],
    }


def calculate_points(scratchcard):
    return 1 * (2 ** (wins - 1)) if (wins := calculate_wins(scratchcard)) else 0


def calculate_wins(scratchcard):
    return sum(
        num in scratchcard["winning_nums"] for num in scratchcard["selected_nums"]
    )


def assess_scratchcards(file):
    return sum(val for key, val in get_scratchcard_scores(file).items())


def get_scratchcard_scores(file, *, use_points=True):
    lines = read_input(file)
    scratchcards = [parse_line(line) for line in lines]
    totalling_function = calculate_points if use_points else calculate_wins
    return {
        scratchcard["card_id"]: totalling_function(scratchcard)
        for scratchcard in scratchcards
    }


def count_copies(file):
    copy_count = defaultdict(int)
    scratchcard_scores = get_scratchcard_scores(file, use_points=False)
    for key, val in scratchcard_scores.items():
        copy_count[key] += 1
        for i in range(1, val + 1):
            print(key, i)
            copy_count[key + i] += copy_count[key]
    return sum(copy_count.values())


# # PART ONE
# example_answer = assess_scratchcards("./day_4/example_input")
# print(f"Example answer: {example_answer}")
# puzzle_answer = assess_scratchcards("./day_4/puzzle_input")
# print(f"Puzzle answer: {puzzle_answer}")

# # PART TWO
# example_answer = count_copies("./day_4/example_input")
# print(f"Example answer: {example_answer}")
# puzzle_answer = count_copies("./day_4/puzzle_input")
# print(f"Puzzle answer: {puzzle_answer}")
