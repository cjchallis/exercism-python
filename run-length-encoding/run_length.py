import re

def encode(string):
    out = ''
    while(string):
        m = re.search("(.)\\1*", string).group(0)
        if len(m) > 1:
            out += str(len(m))
        out += m[0]
        string = re.sub(m, '', string, count = 1)
    return out

def decode(string):
    out = ''
    while(string):
        m = re.search('\d*\D', string)
        char = m.group(0)[-1]
        num = m.group(0)[0:-1]
        if num == '':
            num = 1
        else:
            num = int(num)
        out += num * char
        string = re.sub(m.group(0), '', string, count = 1)
    return out
