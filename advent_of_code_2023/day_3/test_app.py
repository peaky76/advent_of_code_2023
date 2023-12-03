from .app import get_part_numbers

def test_get_part_numbers():
    lines = ["123...",".45.67","..890."]
    expected = get_part_numbers(lines)
    actual = {
        123: (0, 0), 
        45: (1, 1), 
        67: (1, 4), 
        890: (2, 2)
    }
    assert expected == actual