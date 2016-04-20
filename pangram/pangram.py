from string import ascii_lowercase

def is_pangram(string):
    alpha = dict.fromkeys(ascii_lowercase, 0)
    for l in string.lower():
        if l in ascii_lowercase:
            alpha[l] += 1
    return all(alpha.values())
