import pytest
from .app import extrapolate_value, get_diffs

@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([0,3,6,9,12,15], 18),
        ([1,3,6,10,15,21], 28),
        ([10,13,16,21,30,45], 68),
    ],
)
def test_extrapolate_value(test_input, expected):
    actual = extrapolate_value(test_input)
    assert actual == expected
    
@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([0,3,6,9,12,15], [3,3,3,3,3]),
        ([1,3,6,10,15,21], [2,3,4,5,6]),
        ([10,13,16,21,30,45], [3,3,5,9,15]),
    ],
)
def test_get_diffs(test_input, expected):
    actual = get_diffs(test_input)
    assert actual == expected