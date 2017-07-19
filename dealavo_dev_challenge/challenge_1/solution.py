from dealavo_dev_challenge.challenge import Challenge


class Challenge_1(Challenge):

    def solve_challenge(self, filename):
        with open(filename) as input:
            n = int(input.readline().strip())
            data = []
            for i in range(n):
                data.append([int(element) for element in input.readline().strip().split()])

        depth_table = []
        depth_table.append([1 if not data[0][i] else 0 for i in range(n)])
        for i in range(1, n):
            prev_row = depth_table[i - 1]
            depth_table.append([prev_row[j] + 1 if not data[i][j] else 0 for j in range(n)])

        global_max = 0
        for row in depth_table:
            stack = []
            row_max = 0
            for i in range(n):
                val = row[i]
                if len(stack) == 0 and val > 0:
                    stack.append((val, i))
                    continue
                candidate = None
                while len(stack) > 0 and val < stack[-1][0]:
                    k, j = stack.pop()
                    candidate = k * (i - j)
                    if candidate > row_max:
                        row_max = candidate
                if candidate is None and val > 0:
                    stack.append((val, i))
                elif val > 0:
                    stack.append((val, j))
            while len(stack) > 0:
                k, j = stack.pop()
                candidate = k * (i - j + 1)
                if candidate > row_max:
                    row_max = candidate
            if row_max > global_max:
                global_max = row_max
        return global_max

    @staticmethod
    def res_to_str(res):
        return str(res)


