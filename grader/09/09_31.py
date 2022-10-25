def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_coprime(a, b, c):
    return gcd(a, gcd(b, c)) == 1


def primitive_Pythagorean_triples(n):
    triples = []
    for a in range(1, n + 1):
        for b in range(a+1, n + 1):
            for c in range(b+1, n + 1):
                if a**2 + b**2 == c**2 and is_coprime(a, b, c):
                    triples.append([a, b, c])
    return sorted(triples, key=lambda x: x[2])


exec(input().strip())
