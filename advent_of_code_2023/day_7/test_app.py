import pytest
from .app import hand_grouping, rank_cards, rank_equal_hands, rank_hands

@pytest.mark.parametrize(
    "test_input,expected",
    [
       ('AAAAA', (5,)),
       ('AA8AA', (4, 1)),
       ('23332', (3, 2)),
       ('TTT98', (3, 1, 1)),
       ('23432', (2, 2, 1)),
       ('A23A4', (2, 1, 1, 1)),
       ('23456', (1, 1, 1, 1, 1))
    ],
)
def test_hand_grouping_without_wild_jack(test_input, expected):
    actual = hand_grouping(test_input)
    assert actual == expected

@pytest.mark.parametrize(
    "test_input,expected",
    [
       ('KTJJT', (4, 1)),
    ],
)
def test_hand_grouping_with_wild_jack(test_input, expected):
    actual = hand_grouping(test_input, wild_jack=True)
    assert actual == expected

def test_rank_cards():
    actual = rank_cards(['5', 'A', '7', '3', 'K', '2', 'T', 'Q', '6'])
    expected = ['2', '3', '5', '6', '7', 'T', 'Q', 'K', 'A']
    assert actual == expected

def test_rank_equal_hands():
    actual = rank_equal_hands(["33332", "2AAAA", "QKQQQ"])
    expected = ["2AAAA", "33332", "QKQQQ"]
    assert actual == expected

def test_rank_hands():
    actual = rank_hands(["32T3K", "T55J5", "KK677", "KTJJT", "QQQJA"])
    expected = ["32T3K", "KTJJT", "KK677", "T55J5", "QQQJA"]
    assert actual == expected