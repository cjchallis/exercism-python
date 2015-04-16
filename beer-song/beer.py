def verse(n):
    return (number(n) + bottles(n) + ' of beer on the wall, ' +
            number(n).lower() + bottles(n) + ' of beer.\n' +
            pass_around(n) + number(n-1).lower() +
            bottles(n-1) + ' of beer on the wall.\n')
	
def song(n, m = 0):
    return '\n'.join(verse(i) for i in range(n, m-1, -1)) + '\n'
	
def number(n):
    return 'No more' if n == 0 else str(n % 100)
	
def bottles(n):
    return ' bottle' if n == 1 else ' bottles'
	
def pass_around(n):
    if n == 0:
        return 'Go to the store and buy some more, '
    one = 'it' if n == 1 else 'one'
    return 'Take %s down and pass it around, ' % one
