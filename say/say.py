import re

ONES = dict(zip(range(20),
                ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
                 'eight', 'nine','ten','eleven','twelve','thirteen','fourteen',
                 'fifteen', 'sixteen','seventeen','eighteen','nineteen']))
TENS = dict(zip(range(2,10),
                ['twenty','thirty','forty','fifty','sixty','seventy','eighty',
                 'ninety']))
ORDERS = ['', 'thousand', 'million', 'billion']

def say(n):
    if not 0 <= n < 1e12:
        raise AttributeError('Value must be between 0 and 999,999,999,999')
    if n == 0:
        return 'zero'
    out = [] 
    i = 0
    while n > 0:
        n, r = divmod(n, 1000)
        if r > 0:
            out.insert(0, ORDERS[i])
        out[0:0] = _three_digit(r)
        if i == 0 and 0 < r < 100 and n > 0:
            out.insert(0, 'and')
        i += 1                
    return re.sub(' +', ' ', ' '.join(out)).strip()


def _three_digit(n):
    three, two = divmod(n, 100)
    return [ONES[three], filler('hundred', three), filler('and', three * two),
            _two_digit(two)]


def _two_digit(n):
    if n < 20:
        return ONES[n]
    two, one = divmod(n, 10)
    return '{0}{1}{2}'.format(TENS[two], filler('-', one), ONES[one])


def filler(word, n):
    return  word * (n > 0)

