with open('example.txt') as data:
    n = int(data.readline().strip())
    masses = [int(m) for m in data.readline().strip().split()]
    order_a = [int(a) for a in data.readline().strip().split()]
    order_b = [int(b) for b in data.readline().strip().split()]
    elephants_to_masses = {n + 1: masses[n] for n in range(n)}

permutation = {}


for i in range(n):
    permutation[order_b[i]] = order_a[i]

odw = [False for _ in range(n)]
c = 0
cycles = []
for i in range(n):
    if not odw[i]:
        c += 1
        x = i + 1
        cycles.append([])
        while not odw[x]:
            odw[x] = True
            cycles[c - 1].append(x)
            x = permutation[x]

cycles_sums = []
cycles_mins = []
min_val = float('inf')
for i in range(c):
    cycles_sums.append(0)
    cycles_mins.append(float('inf'))
    for e in cycles[i]:
        cycles_sums[i] += elephants_to_masses[e]
        cycles_mins[i] = min([cycles_mins[i], elephants_to_masses[e]])
    min_val = min(min_val, cycles_mins[i])

w = 0
method_1 = []
method_2 = []
for i in range(c):
    method_1.append(cycles_sums[i] + (len(cycles[i]) - 2) * cycles_mins[i])
    method_2.append(cycles_sums[i] + cycles_mins[i] + (len(cycles) + 1) * min_val)
    w += min(method_1[i], method_2[i])

print w

