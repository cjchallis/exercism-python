from string import ascii_lowercase

def is_pangram(string):
    return set(list(ascii_lowercase)) <= set(string.lower())
