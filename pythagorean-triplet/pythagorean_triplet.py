from fractions import gcd

def is_triplet(trip):
    trip = sorted(trip)
    return trip[0]**2 + trip[1]**2 == trip[2]**2
    

def primitive_triplets(b):
    if b % 4:
        raise ValueError('Integer must be divisible by 4')
    triplets = []
    for n in range(1, int((b/2)**0.5)+1):
        q, r = divmod(b//2, n)
        if r == 0 and gcd(n,q) == 1 and (q-n) % 2:
            a = q*q - n*n
            triplets.append((min(a,b), max(a,b), q*q + n*n))
    return set(triplets)
    

def triplets_in_range(low, high):
    candidates = [primitive_triplets(b) for b in range(4, high, 4)]
    primitives = set([triplet for sublist in candidates
                              for triplet in sublist
                              if max(triplet) <= high])
    return set([tuple(i*k for k in p) for p in primitives
                for i in range(low // min(p) + (low % min(p) != 0), 
                               high // max(p) + 1)])
