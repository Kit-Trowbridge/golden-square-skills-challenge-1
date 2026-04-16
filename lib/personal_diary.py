# A function called make_snippet that takes a string as an argument 
# and returns the first five words and then a '...' if there are more than that.

def make_snippet(string):
    word_list = string.split()
    if len(word_list) <= 5:
        return string
    else:
        return " ".join(word_list)