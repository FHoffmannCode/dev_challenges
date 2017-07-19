from fractions import gcd
import os
import subprocess
from dealavo_dev_challenge.utils import get_challenge_5_own_output_filename
from dealavo_dev_challenge.challenge import Challenge


class Challenge_5(Challenge):

    def solve_challenge(self, filename):
        class Vector(object):
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def __repr__(self):
                return repr((self.x, self.y))

        with open(filename) as data:
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
        return [vectors[0].x, vectors[0].y, vectors[1].x, vectors[1].y]

    def test_challenge(self):
        for filename in self.input_to_output_filenames_map:
            print filename
            res = self.solve_challenge(filename)
            res = self.res_to_str(res)
            own_output = get_challenge_5_own_output_filename(filename)
            with open(own_output, 'w') as own_out_file:
                own_out_file.write(res)
            output = self.input_to_output_filenames_map[filename]
            working_dir = '/home/filip/workspace/dealavo_dev_challenges/dealavo_dev_challenge/'
            try:
                compare_res = subprocess.check_output([
                    os.path.join(working_dir, 'challenge_5/./skospr'),
                    os.path.join(working_dir, own_output),
                    os.path.join(working_dir, output)])
            except Exception:
                compare_res = 'zle'
            if 'OK' in compare_res:
                print 'tak'
            else:
                print 'nie'

    @staticmethod
    def res_to_str(res):
        if len(res) == 2:
            return '%d %d' % (res[0], res[1])
        else:
            return '%d %d\n%d %d' % (res[0], res[1], res[2], res[3])
