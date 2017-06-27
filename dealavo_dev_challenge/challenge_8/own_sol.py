with open('example.txt') as data:
    n = int(data.readline().strip())
    masses = [int(m) for m in data.readline().strip().split()]
    order_a = [int(a) for a in data.readline().strip().split()]
    order_b = [int(b) for b in data.readline().strip().split()]
    elephants_to_masses = {n + 1: masses[n] for n in range(n)}

permutation = {}
for i in range(n):
    permutation[order_b[i]] = order_a[i]

cycles = []
odw = [False for _ in range(n)]
for i in range(n):
    if not odw[i]:
        x = i + 1
        cycles.append([])
        while not odw[x]:
            odw[x] = True
            cycles[-1].append(x)
            x = permutation[x]
cycles_mins = []
cycles_sums = []
for cycle in cycles:
    procced_cycle = map(lambda e: elephants_to_masses[e], cycle)
    cycles_sums.append(sum(procced_cycle))
    cycles_mins.append(min(procced_cycle))
global_min = min(cycles_mins)

w = 0
for i in range(len(cycles)):
    method_1 = cycles_sums[i] + (len(cycles[i]) - 2) * cycles_mins[i]
    method_2 = cycles_sums[i] + cycles_mins[i] + (len(cycles[i]) + 1) * global_min
    w += min([method_1, method_2])
print w



