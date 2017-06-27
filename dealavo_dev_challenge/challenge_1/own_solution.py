with open('dzi2.in') as input:
    n = int(input.readline().strip())
    data = []
    for i in range(n):
        data.append([int(element) for element in input.readline().strip().split()])


depth_table = [[1 if i == 0 else 0 for i in data[0]]]
for i in range(1, n):
    depth_table.append([depth_table[i - 1][j] + 1 if data[i][j] == 0 else 0 for j in range(n)])

stack = []
glob_max = 0
for row in depth_table:
    max_space = 0
    for i in range(n):
        val = row[i]
        if len(stack) == 0 and val > 0:
            stack.append((val, i))
            continue
        candidate = None
        while len(stack) > 0 and val < stack[-1][0]:
            k, j = stack.pop()
            candidate = (i - j) * k
            if candidate > max_space:
                max_space = candidate
        if val > 0 and candidate is not None:
            stack.append((val, j))
            continue
        if candidate is None and val > 0:
            stack.append((val, i))
        else:
            continue
    while len(stack) > 0:
        k, j = stack.pop()
        candidate = (len(stack) - j) * k
        if candidate > max_space:
            max_space = candidate
    if max_space > glob_max:
        glob_max = max_space

print glob_max


