NORTH = (0,1)
SOUTH = (0,-1)
EAST = (1,0)
WEST = (-1,0)

def add_tuple(t1, t2):
    return tuple(x + y for x, y in zip(t1, t2))

class Robot:
    def __init__(self, bearing = NORTH, x = 0, y = 0):
        self.bearing = bearing
        self.coordinates = (x,y)
        self.commands = {"L": self.turn_left, 
                         "R": self.turn_right,
                         "A": self.advance
                        }

    def turn_left(self):
        self.bearing = tuple([-self.bearing[1], self.bearing[0]])

    def turn_right(self):
        self.bearing = tuple([self.bearing[1], -self.bearing[0]])

    def advance(self):
        self.coordinates = add_tuple(self.coordinates, self.bearing)

    def simulate(self, string):
        for c in string:
            self.commands[c]()
