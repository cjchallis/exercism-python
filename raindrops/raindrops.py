def raindrops(n):
    out = ''
    out += '' if n%3 else 'Pling'
    out += '' if n%5 else 'Plang'
    out += '' if n%7 else 'Plong'
    return out if out else str(n)
