from copy import deepcopy
from itertools import permutations

pieces = {'colors' : ['red', 'green', 'yellow', 'blue', 'ivory'],
          'nations' : ['Englishman', 'Spaniard', 'Ukranian', 'Japanese', 'Norwegian'],
          'cigs' : ['Old Gold', 'Kools', 'Lucky Strike', 'Parliaments', 'Chesterfields'],
          'beverages' : ['coffee', 'milk', 'orange juice', 'tea', 'water'],
          'pets' : ['dog', 'horse', 'fox', 'zebra', 'snails']
         }

types = {i:l for l,v in pieces.items() for i in v}

solution = [{} for i in range(5)]

positions = [('milk', 2),
             ('Norwegian', 0)
            ]

same = [('Englishman', 'red'),
        ('Spaniard', 'dog'),
        ('coffee', 'green'),
        ('Ukranian', 'tea'),
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

pcs = {}

def solve():
    position()
    solved = False
    while not solved:
        pcs = deepcopy(pieces)
        same(pcs)
        neighbor()
        offset()
        solved = True
    
def position():
    for item, pos in positions:
        solution[pos][types[item]] = item
        pieces[types[item]].remove(item)

def neighbor():
    pass

def same(pcs):
    print(pcs)
    pc = 'nations'
    p = pcs[pc]
    for house in solution:
        if pc not in house:
            house[pc] = p.pop()
    print(pcs)
    print(solution)
    

def offset():
    pass

solve()
