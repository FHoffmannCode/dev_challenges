from fractions import gcd


class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return repr((self.x, self.y))


with open('./in/sko10.in') as data:
    n = int(data.readline().strip())
    vectors = []
    for _ in range(n):
        a_b = data.readline().strip().split()
        vectors.append(Vector(*[int(coord) for coord in a_b]))


def xch(a, b):
    return b, a


def extended_gcd(a, b):
    a_a, a_b, b_a, b_b = 1, 0, 0, 1
    if a < 0:
        a, a_a = -a, -1
    if b < 0:
        b, b_b = -b, -1
    if b < a:
        a, b = b, a
        a_a, b_a = b_a, a_a
        a_b, b_b = b_b, a_b
    while a != 0:
        b_a = b_a - (b / a) * a_a
        b_b = b_b - (b / a) * a_b
        b = b % a
        a, b = b, a
        a_a, b_a = b_a, a_a
        a_b, b_b = b_b, a_b
    k, l = b_a, b_b
    return b, k, l


def join_if_dependent(u, v):
    if v.x == 0 and v.y == 0:
        return u, v
    if u.x == 0 and u.y == 0:
        u = v
        return u, v
    if u.x == 0 and v.x == 0:
        u.y = gcd(u.y, v.y)
        return u, v
    if u.y == 0 and v.y == 0:
        u.x = gcd(u.x, v.x)
        return u, v
    if u.x * v.y == v.x * u.y:
        u.x = abs(gcd(u.x, v.x))
        u.y = (v.y * u.x) / v.x
        return u, v
    return False


def normal_form(u, v):
    if join_if_dependent(u, v):
        v.x, v.y = 0, 0
        return u, v
    gcdy = gcd(u.y, v.y)
    new_v = Vector(0, 0)
    new_v.x = abs(u.x * (v.y / gcdy) - v.x * (u.y / gcdy))
    new_v.y = 0
    ignore, k, l = extended_gcd(u.y, v.y)
    new_u = Vector(0, 0)
    new_u.x = k * u.x + l * v.x
    new_u.y = k * u.y + l * v.y
    if new_v.x != 0:
        if new_u.x < 0:
            new_u.x = - new_u.x
            new_u.y = - new_u.y
        new_u.x = new_u.x % new_v.x
    u = new_u
    v = new_v
    return u, v


def reduce_v():
    vectors[-2], vectors[-1] = normal_form(vectors[-2], vectors[-1])
    for i in range(n - 3, -1, -1):
        vectors[i], vectors[i+1] = normal_form(vectors[i], vectors[i+1])
        vectors[i+1], vectors[i+2] = join_if_dependent(vectors[i+1], vectors[i+2])
    vectors[0], vectors[1] = normal_form(vectors[0], vectors[1])

reduce_v()
with open('./test_own_out.out', 'w') as out:
    out.write(str(vectors[0].x) + ' ' + str(vectors[0].y) + '\n')
    out.write(str(vectors[1].x) + ' ' + str(vectors[1].y))
