from dealavo_dev_challenge.challenge import Challenge


class Challenge_7(Challenge):

    def solve_challenge(self, filename):
        with open(filename) as data:
            w = []
            n = int(data.readline().strip())
            for _ in range(n):
                building = int(data.readline().strip().split()[1])
                w.append(building)

        s = []
        p = 0
        for i in range(n):
            while len(s) != 0 and s[-1] > w[i]:
                s.pop()
            if len(s) == 0 or s[-1] < w[i]:
                s.append(w[i])
                p = p + 1

        return p