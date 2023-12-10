from .app import get_continuous_ranges

def test_get_continuous_ranges_for_single_number():
    actual = get_continuous_ranges([1])
    expected = [(1, 2)]
    assert actual == expected

def test_get_continuous_ranges_for_multiple_numbers():
    actual = get_continuous_ranges([1, 2, 3])
    expected = [(1, 4)]
    assert actual == expected

def test_get_continuous_ranges_for_multiple_numbers_with_breaks():
    actual = get_continuous_ranges([1, 2, 3, 5, 6, 7])
    expected = [(1, 4), (5, 8)]
    assert actual == expected

