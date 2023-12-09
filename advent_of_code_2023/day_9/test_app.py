import pytest
from .app import extrapolate_value

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
    
