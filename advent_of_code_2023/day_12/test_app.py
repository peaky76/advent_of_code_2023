import pytest
from .app import number_of_arrangements

@pytest.mark.parametrize(
    "test_input,expected",
    [
        (("?", [1]), 1),
        (("??", [1]), 2),
        (("??", [2]), 1),
        (("?#", [2]), 1),
        (("???", [1]), 3),
        (("?.?", [1, 1]), 1),
        (("?.?", [1]), 2),
        (("???", [1, 1]), 1),
        (("????", [1, 1]), 3),
        (("???????", [2, 1]), 10),
        (("???", [1]), 3),
        (("?#?", [2]), 2),
        (("#??", [2]), 1),
        (("???.###", [1,1,3]), 1),
        (("?#?#?#?#?#?#?#?", [1,3,1,6]), 1),
        (("?###????????", [3,2,1]), 10),
    ],
)
def test_number_of_arrangements(test_input, expected):
    actual = number_of_arrangements(*test_input)
    assert actual == expected

