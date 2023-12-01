import sys
sys.path.append('..')

from advent_of_code_2023 import read_input  # noqa: E402

def get_calibration_value(line):
    digits = [int(digit) for digit in line if digit.isdigit()]
    first = digits[0]
    last = digits[-1]
    return int(str(f"{first}{last}"))

# PART ONE
# print(sum(get_calibration_value(line) for line in read_input("./day_1/example_input_1")))
print(sum(get_calibration_value(line) for line in read_input("./day_1/puzzle_input")))

# PART TWO
print(sum(get_calibration_value(line) for line in read_input("./day_1/example_input_2")))
# print(sum(get_calibration_value(line) for line in read_input("./day_1/puzzle_input")))
