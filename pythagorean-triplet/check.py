from math import floor

def find_product():
    i = 0
    is_square = False
    while(not is_square):
        i += 1
        square = i**2 + i*4000
        is_square = square == floor(square**0.5 + 0.5)**2
    a = (floor(square**0.5 + 0.5) - i) / 2
    b = a**2 / (2*i) - i / 2
    c = a**2 / (2*i) + i / 2
    print(a)
    print(b)
    print(c)

find_product()
    
