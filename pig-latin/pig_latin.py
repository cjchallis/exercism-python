import re
from string import ascii_lowercase
VOWELS = 'aeiouy'
CONSONANTS = ''.join(set(ascii_lowercase) - set(VOWELS))

universal = '[aeio]'
u_if_no_q = '((?<!q)u)'
x_and_y = '(^(x|y)(?=[{0}]))'.format(CONSONANTS)
find_first_vowel = '{0}|{1}|{2}'.format(universal, u_if_no_q, x_and_y)

def _word(word):
    begin = re.search(find_first_vowel, word)
    if begin:
        word = word[begin.start(0):] + word[:begin.start(0)]
    return word + 'ay'

def translate(string):
    return ' '.join([_word(w) for w in string.lower().split()])
