import re
from string import ascii_lowercase
VOWELS = 'aeiouy'
CONSONANTS = ''.join(set(ascii_lowercase) - set(VOWELS))

UNIVERSAL = '[aeio]'
U_IF_NO_Q = '((?<!q)u)'
X_AND_Y = '(^(x|y)(?=[{0}]))'.format(CONSONANTS)
FIND_FIRST_VOWEL = '{0}|{1}|{2}'.format(UNIVERSAL, U_IF_NO_Q, X_AND_Y)

def _word(word):
    begin = re.search(FIND_FIRST_VOWEL, word)
    if begin:
        word = word[begin.start(0):] + word[:begin.start(0)]
    return word + 'ay'

def translate(string):
    return ' '.join([_word(w) for w in string.lower().split()])
