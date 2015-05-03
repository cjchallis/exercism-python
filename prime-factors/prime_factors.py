def prime_factors(n):
    factors = []
    return next(n, factors, 2)
	
def next(k, factors, p):
    if k <= 1:
        return factors
    while k % p:
        p += 1
    factors.append(p)
    return next(k / p, factors, p)
