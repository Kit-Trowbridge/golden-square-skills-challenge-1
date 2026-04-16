# A function called make_snippet that takes a string as an argument 
# and returns the first five words and then a '...' if there are more than that.

from lib.personal_diary import *

# Given a string, it returns a string
def test_make_snippet_returns_string():
    result = make_snippet("Hello")
    assert result == "Hello"

# not sure what to test in between but it seems like big jump
# need to test it can count how many words?

def test_make_snippet_can_count_words():
    result = make_snippet("Hello there")   
    assert result == 2



# Given a string of six words, it returns the first five
# def test_make_snippet_returns_first_five_words_when_given_six():
#     result = make_snippet("The quick brown fox jumps over")
#     assert result == "The quick brown fox jumps"
