import re

def abbreviate(string):
    return ''.join([w[0].upper() for w in re.split(" |-|[a-z](?=[A-Z])", string)])
