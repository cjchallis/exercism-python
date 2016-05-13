import re


def decode(encoded_data):
    # Split data into a list of pairs, e.g. '2A3B' -> [('2','A'),('3','B')]
    char_count = re.findall(r'(\d*)(\D)', encoded_data)

    # Convert list of pairs to 'AABBB'
    return ''.join(int_with_default(count, 1) * char for (count, char) in char_count)


def encode(data):
    # Iterator yielding match objects.
    # e.g. 'AAA' -> one match object, o.group() == 'AAA', o.group(1) == 'A'
    matches = re.finditer(r'(.)\1*', data)

    # Convert 'AAA' to '3A'
    def reduce_match(m):
        lenprefix = str(len(m.group())) if len(m.group()) > 1 else ''
        return ''.join((lenprefix, m.group(1)))

    return ''.join(reduce_match(m) for m in matches)


def int_with_default(x=0, default=0):
    '''Like int(), but returns the given default value instead of throwing an
    ValueError if x is not parseable.'''
    try:
        return int(x)
    except ValueError:
        return default