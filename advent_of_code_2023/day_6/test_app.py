import pytest
from .app import get_times_and_distances

@pytest.mark.parametrize(
    "test_input,expected",
    [
        (["Time:      7  15   30", "Distance:  9  40  200"], [(7, 9), (15, 40), (30, 200)])
    ],
)
def test_get_times_and_distances(test_input, expected):
    actual = get_times_and_distances(test_input)
    assert actual == expected
    
