import pytest
from .app import get_times_and_distances, possible_distances, num_ways_to_win


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            ["Time:      7  15   30", "Distance:  9  40  200"],
            [(7, 9), (15, 40), (30, 200)],
        )
    ],
)
def test_get_times_and_distances(test_input, expected):
    actual = get_times_and_distances(test_input)
    assert actual == expected


def test_possible_distances_with_odd_time():
    assert possible_distances(7) == [0, 6, 10, 12, 12, 10, 6, 0]


def test_possible_distances_with_even_time():
    assert possible_distances(8) == [0, 7, 12, 15, 16, 15, 12, 7, 0]


def test_num_ways_to_win():
    assert num_ways_to_win(7, 9) == 4
