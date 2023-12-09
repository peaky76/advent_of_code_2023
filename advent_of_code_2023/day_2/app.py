from math import prod
import re
import sys

sys.path.append("..")

from advent_of_code_2023 import read_input  # noqa: E402


def parse_grab(grab):
    def find(phrase):
        return (
            int(match.groups(0)[0])
            if (match := re.search(f"(\\d+) {phrase}", grab))
            else 0
        )

    return (find("red"), find("green"), find("blue"))


def parse_input(line):
    the_id = int(line.split(":")[0].split("Game ")[1])
    grabs = line.split(":")[1].split(";")
    return {"id": the_id, "rgb": [parse_grab(grab) for grab in grabs]}


def min_possible_balls(grabs):
    reds = [grab[0] for grab in grabs]
    greens = [grab[1] for grab in grabs]
    blues = [grab[2] for grab in grabs]
    return (max(reds), max(greens), max(blues))


def is_grab_too_much(grab_rgb, limit_rgb):
    return any(grab > limit for grab, limit in zip(grab_rgb, limit_rgb))


def is_game_possible(grabs, limit_rgb):
    return not any(is_grab_too_much(grab_rgb, limit_rgb) for grab_rgb in grabs)


def sum_of_possible_games(lines, limit_rgb=(12, 13, 14)):
    return sum(
        game["id"]
        for game in get_games(lines)
        if is_game_possible(game["rgb"], limit_rgb)
    )


def get_games(input):
    return [parse_input(line) for line in input]


# PART ONE
example_answer = sum_of_possible_games(read_input("./day_2/example_input"))
print(f"Example answer: {example_answer}")
puzzle_answer = sum_of_possible_games(read_input("./day_2/puzzle_input"))
print(f"Puzzle answer: {puzzle_answer}")

# # PART TWO
example_answer = sum(
    prod(min_possible_balls(game["rgb"]))
    for game in get_games(read_input("./day_2/example_input"))
)
print(f"Example answer: {example_answer}")
puzzle_answer = sum(
    prod(min_possible_balls(game["rgb"]))
    for game in get_games(read_input("./day_2/puzzle_input"))
)
print(f"Puzzle answer: {puzzle_answer}")
