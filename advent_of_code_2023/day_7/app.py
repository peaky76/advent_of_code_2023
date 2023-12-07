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

from advent_of_code_2023 import read_input  # noqa: E402

CARD_ORDER = "23456789TJQKA"
CARD_ORDER_WILD = "J23456789TQKA"

def hand_grouping(hand, *, wild_jack=False):
    count = Counter(list(hand))

    if wild_jack:
        hand = hand.replace("J", max(count, key=count.get))
        count = Counter(list(hand))

    return tuple(sorted(count.values(), reverse=True))

def rank_cards(cards):
    return sorted(cards, key=lambda card: CARD_ORDER.index(card))

def rank_equal_hands(hands):
    return sorted(hands, key=lambda hand: [CARD_ORDER.index(card) for card in hand])

def rank_hands(hands):
    return sorted(hands, key=lambda hand: (hand_grouping(hand), [CARD_ORDER.index(card) for card in hand]))
    
def get_total_winnings(file, *, wild_jack=False):
    lines = read_input(file)
    ORDERING = CARD_ORDER_WILD if wild_jack else CARD_ORDER
    hands_and_bets = [(line.split(" ")[0], int(line.split(" ")[1])) for line in lines]
    ranked_hands_and_bets = sorted(hands_and_bets, key=lambda hand_and_bet: (hand_grouping(hand_and_bet[0], wild_jack=wild_jack), [ORDERING.index(card) for card in hand_and_bet[0]]))
    return sum([(i + 1) * hand_and_bet[1] for i, hand_and_bet in enumerate(ranked_hands_and_bets)])

# PART ONE
example_answer = get_total_winnings("./day_7/example_input")
print(f"Example answer: {example_answer}")
puzzle_answer = get_total_winnings("./day_7/puzzle_input")
print(f"Puzzle answer: {puzzle_answer}")

# # PART TWO
example_answer = get_total_winnings("./day_7/example_input", wild_jack=True)
print(f"Example answer: {example_answer}")
# puzzle_answer = get_total_winnings("./day_7/puzzle_input", wild_jack=True)
# print(f"Puzzle answer: {puzzle_answer}")
