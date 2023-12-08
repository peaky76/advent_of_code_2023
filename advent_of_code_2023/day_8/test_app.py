import pytest
from .app import lr_to_binary_str

def test_lr_to_binary_str():
    actual = lr_to_binary_str('LLRLRRR')
    expected = "0010111"
    assert actual == expected

# @pytest.mark.parametrize(
#     "test_input,expected",
#     [
#         (None, None),
#     ],
# )
# def test_the_function(test_input, expected):
#     actual = the_function(test_input)
#     expected = None
#     assert actual == expected
    
