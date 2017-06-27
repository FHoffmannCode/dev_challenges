with open('dzi1.in') as input:
    n = int(input.readline().strip())
    data = []
    for i in range(n):
        data.append([int(element) for element in input.readline().strip().split()])


def init_depth_table(first_row, n):
    return [[0 if first_row[i] else 1 for i in range(n)]]


def make_depth_table(data, n):
    depth_table = init_depth_table(data[0], n)
    for row in range(1, n):
        depth_table_row = []
        for i in range(n):
            if data[row][i] == 1:
                depth_table_row.append(0)
                continue
            depth_table_row.append(depth_table[row - 1][i] + 1)
        depth_table.append(depth_table_row)
    return depth_table


def process_row(row_index, n, depth_table):
    stack = []
    max_space = 0
    for i in range(n):
        if len(stack) == 0:
            stack.append((i, depth_table[row_index][i]))
            continue
        candidate = None
        while len(stack) > 0 and depth_table[row_index][i] < stack[-1][1]:
            candidate = stack.pop()
            cand_space = (i - candidate[0] + 1) * candidate[1]
            if cand_space > max_space:
                max_space = cand_space
        if candidate is None:
            if depth_table[row_index][i] == 0:
                continue
            stack.append((i, depth_table[row_index][i]))
        elif depth_table[row_index][i] == 0:
            continue
        else:
            stack.append((candidate[0], depth_table[row_index][i]))
    while len(stack) > 0:
        candidate = stack.pop()
        cand_space = (i - candidate[0] + 1) * candidate[1]
        if cand_space > max_space:
            max_space = cand_space
    return max_space

def main():
    depth_table = make_depth_table(data, n)
    max_space = 0
    for row_index in range(n):
        candidate_space = process_row(row_index, n, depth_table)
        if candidate_space > max_space:
            max_space = candidate_space
    return max_space


if __name__ == '__main__':
    max_space = main()
    print max_space

