from fractions import gcd


with open('example.txt') as data:
    n = int(data.readline().strip())
    vectors = []
    for _ in range(n):
        a_b = data.readline().strip().split()
        vectors.append([int(coord) for coord in a_b])


def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return x0, y0


def process_vectors(a, b):
    xa, ya = a
    xb, yb = b
    m = gcd(ya, yb)
    k = ya / m
    l = yb / m
    p, q = xgcd(k, l)
    c = (l * xa - k * xb, 0)
    d = (p * xa + q * xb, p * ya + q * yb)
    return c, d

res = []
a = vectors[0]
for i in range(1, n):
    b = vectors[i]
    b, a = process_vectors(a, b)
    res.append(b)
b = reduce(lambda v, k: (gcd(v[0], k[0]), 0), res)
print a, b

