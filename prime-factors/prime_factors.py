def prime_factors(n):
    return next(n, [], 2)
	
def next(k, factors, p):
    if k <= 1:
        return factors
    while k % p:
        p += 1
    return next(k / p, factors + [p], p)
