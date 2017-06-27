from fractions import gcd

with open('example.txt') as data:
    n = int(data.readline().strip())
    vectors = []
    for _ in range(n):
        a_b = data.readline().strip().split()
        vectors.append([int(coord) for coord in a_b])


def process_vectors(a, b):
    x_a, y_a = a
    x_b, y_b = b
    m = gcd(y_a, y_b)
    k = y_a / m
    l = y_b / m
    p, q = xgcd(k, l)
    c = (l * x_a - k * x_b, l * y_a - k * y_b)
    d = ((p * x_a) + (q * x_b), (p * y_a) + (q * y_b))
    return c, d


def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  x0, y0


def solve_challenge(vectors):
    a = vectors[0]
    processed_vectors = []
    for i in xrange(1, len(vectors)):
        a_i = vectors[i]
        b, a = process_vectors(a, a_i)
        processed_vectors.append(b)
    b = reduce(lambda v, k: (gcd(v[0], k[0]), 0), processed_vectors)
    return a

print solve_challenge(vectors)
