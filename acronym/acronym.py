from re import split

def abbreviate(string):
    return ''.join([w[0].upper() for w in split(" |-|[a-z](?=[A-Z])", string)])
