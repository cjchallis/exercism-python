from string import ascii_lowercase

def is_pangram(string):
    return set(ascii_lowercase) <= set(string.lower())
