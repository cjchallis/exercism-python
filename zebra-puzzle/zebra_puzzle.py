from itertools import permutations

pieces = {'colors' : ['red', 'green', 'yellow', 'blue', 'ivory'],
          'nations' : ['Englishman', 'Spaniard', 'Ukrainian', 'Japanese', 'Norwegian'],
          'cigs' : ['Old Gold', 'Kools', 'Lucky Strike', 'Parliaments', 'Chesterfields'],
          'beverages' : ['coffee', 'milk', 'orange juice', 'tea', 'water'],
          'pets' : ['dog', 'horse', 'fox', 'zebra', 'snails']
         }

positions = [('milk', 2),
             ('Norwegian', 0)
            ]

same = [('Englishman', 'red'),
        ('Spaniard', 'dog'),
        ('coffee', 'green'),
        ('Ukrainian', 'tea'),
        ('Old Gold', 'snails'),
        ('Kools', 'yellow'),
        ('Lucky Strike', 'orange juice'),
        ('Japanese', 'Parliaments')
       ]

neighbor = [('Chesterfields', 'fox'),
            ('Kools', 'horse'),
            ('Norwegian', 'blue')
           ]

offset = [('green', 'ivory', 1)]

def brute():
    for p0 in permutations(pieces['colors']):
        for p1 in permutations(pieces['nations']):
            if p1.index('Norwegian') != 0:
                continue
            if p0.index('red') != p1.index('Englishman'):
                continue
            for p2 in permutations(pieces['cigs']):
                if p0.index('yellow') != p2.index('Kools'):
                    continue
                for p3 in permutations(pieces['beverages']):
                    if p3.index('milk') != 2:
                        continue
                    for p4 in permutations(pieces['pets']):
                        lists = [p0,p1,p2,p3,p4]
                        if check(lists):
                            return lists   


def check(lists):
    for s in same:
        s0 = -1
        s1 = -1
        for l in lists:
            if s[0] in l:
                s0 = l.index(s[0])
            elif s[1] in l:
                s1 = l.index(s[1])
        if s0 != s1:
            return False
    for n in neighbor:
        n0 = -1
        n1 = -1
        for l in lists:
            if n[0] in l:
                n0 = l.index(n[0])
            elif n[1] in l:
                n1 = l.index(n[1])
        if abs(n1 - n0) != 1:
            return False
    for o in offset:
        o0 = -1
        o1 = -1
        for l in lists:
            if o[0] in l:
                o0 = l.index(o[0])
            if o[1] in l:
                o1 = l.index(o[1])
        if o0 - o1 != o[2]:
            return False
    return True


def solution():
    sol = brute()
    water_index = sol[3].index('water')
    zebra_index = sol[4].index('zebra')
    water_drinker = sol[1][water_index]
    zebra_owner = sol[1][zebra_index]
    return ("It is the %s who drinks the water.\n"
           "The %s keeps the zebra." %(water_drinker, zebra_owner))
