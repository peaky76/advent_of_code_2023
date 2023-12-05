from .app import create_map_function, parse_seeds_line, parse_title

def test_create_map_function():
    lines = [(1, 0, 10), (13, 11, 10), (24, 21, 10)]
    map_function = create_map_function(lines)
    assert map_function(0) == 1
    assert map_function(15) == 17
    assert map_function(25) == 28
    assert map_function(35) == 35

def test_parse_seeds_line_not_as_range():
    actual = parse_seeds_line("seeds: 79 14 55 13")
    expected = [79, 14, 55, 13]
    assert actual == expected

def test_parse_seeds_line_as_range():
    actual = parse_seeds_line("seeds: 79 14 55 13", as_range=True)
    expected = [79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]
    assert actual == expected

def test_parse_title():
    actual = parse_title("water-to-light map")
    expected = ("water", "light")
    assert actual == expected
    
