from constraint import *

var= {'colors' : ['red', 'green', 'yellow', 'blue', 'ivory'],
      'nations' : ['Englishman', 'Spaniard', 'Ukrainian', 'Japanese', 'Norwegian'],
      'cigs' : ['Old Gold', 'Kools', 'Lucky Strike', 'Parliaments', 'Chesterfields'],
      'beverages' : ['coffee', 'milk', 'orange juice', 'tea', 'water'],
      'pets' : ['dog', 'horse', 'fox', 'zebra', 'snails']
     }

all_var = [v for k in var for v in var[k]]

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

position = [(1, 'Norwegian'),
            (3, 'milk')
           ]

def solution():
    problem = Problem()
    problem.addVariables(all_var, range(1,6))
    for k in var:
        problem.addConstraint(AllDifferentConstraint(), var[k])
    for s in same:
        problem.addConstraint(AllEqualConstraint(), s)
    for n in neighbor:
        problem.addConstraint(lambda a, b: abs(a-b) == 1, n)
    for p in position:
        problem.addConstraint(InSetConstraint([p[0]]), [p[1]])
    problem.addConstraint(lambda a, b: a-b == 1, ('green', 'ivory'))
    sol = problem.getSolutions()[0]
    print_solution(sol)
    zebra_dude = [v for v in var['nations'] if sol[v] == sol['zebra']][0]
    water_dude = [v for v in var['nations'] if sol[v] == sol['water']][0]
    return ("It is the %s who drinks the water.\n"
            "The %s keeps the zebra." %(water_dude, zebra_dude))

def print_solution(sol):
    out = ''
    for k in var:
        for i in range(1,6):
            for v in sol:
                if v in var[k] and sol[v] == i:
                    out += '%-17s' % v
        out += '\n'
    print out
