def flatten(l):
    master = []
    while l:
        new = l.pop(0)
        if new not in [None, (), []]:
            if isinstance(new, list):
                new = flatten(new)
                master.extend(new)
            else:
                master.append(new)
    return master

