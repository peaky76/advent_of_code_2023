import sys

sys.path.append("..")

from advent_of_code_2023 import read_input  # noqa: E402
from peak_utility.number import Numbertext  # noqa: E402

NUMBERWORDS = [str(Numbertext(n)) for n in range(0, 10)]


def find_first_number(line):
    chars = list(line)
    while True:
        for word in NUMBERWORDS:
            if "".join(chars).startswith(word):
                return int(NUMBERWORDS.index(word))
        current_char = chars.pop(0)
        if current_char.isdigit():
            return int(current_char)


def find_last_number(line):
    chars = list(line)
    while True:
        for word in NUMBERWORDS:
            if "".join(chars).endswith(word):
                return int(NUMBERWORDS.index(word))
        current_char = chars.pop(-1)
        if current_char.isdigit():
            return int(current_char)


def get_calibration_value(line, *, digits_only=True):
    first = (
        next(int(char) for char in line if char.isdigit())
        if digits_only
        else find_first_number(line)
    )
    last = (
        next(int(char) for char in line[::-1] if char.isdigit())
        if digits_only
        else find_last_number(line)
    )
    return int(str(f"{first}{last}"))


# PART ONE
# example_answer = sum(
#     get_calibration_value(line) for line in read_input("./day_1/example_input_1")
# )
# print(f"Example answer: {example_answer}")
# puzzle_answer = sum(
#     get_calibration_value(line) for line in read_input("./day_1/puzzle_input")
# )
# print(f"Puzzle answer: {puzzle_answer}")

# # PART TWO
# example_answer = sum(
#     get_calibration_value(line, digits_only=False)
#     for line in read_input("./day_1/example_input_2")
# )
# print(f"Example answer: {example_answer}")
# puzzle_answer = sum(
#     get_calibration_value(line, digits_only=False)
#     for line in read_input("./day_1/puzzle_input")
# )
# print(f"Puzzle answer: {puzzle_answer}")
