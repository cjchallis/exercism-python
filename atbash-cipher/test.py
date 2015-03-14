delchars = ''.join(c for c in map(chr, range(256)) if not c.isalnum())
print(delchars)
