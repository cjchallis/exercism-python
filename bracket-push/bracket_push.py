OPEN = '{[('
CLOSE = '}])'
MATCH = dict(zip(CLOSE, OPEN))

def check_brackets(string):
    stack = []
    for c in string:
        if c in OPEN:
            stack.append(c)
        if c in CLOSE:
            if not stack or stack.pop() != MATCH[c]:
                return False
    return not stack 
