def prime_factors(n):
    factors = []
    return next(n, factors)
	
def next(k, factors):
    if k <= 1:
        return factors
    i = 2
    while k % i:
        i += 1
    factors.append(i)
    return next(k / i, factors)
