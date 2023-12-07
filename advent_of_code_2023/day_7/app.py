# Day 7: Camel Cards

from collections import Counter

# Ranking
# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456

import sys

sys.path.append("..")

# from advent_of_code_2023 import read_input  # noqa: E402

def hand_grouping(hand):
    return tuple(sorted(Counter(list(hand)).values(), reverse=True))
    

# PART ONE
# example_answer = the_function("./day_7/example_input")
# print(f"Example answer: {example_answer}")
# puzzle_answer = the_function("./day_7/puzzle_input")
# print(f"Puzzle answer: {puzzle_answer}")

# # PART TWO
# example_answer = the_function("./day_7/example_input")
# print(f"Example answer: {example_answer}")
# puzzle_answer = the_function("./day_7/puzzle_input")
# print(f"Puzzle answer: {puzzle_answer}")
