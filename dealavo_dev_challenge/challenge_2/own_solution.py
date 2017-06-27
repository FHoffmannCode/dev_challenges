with open('prz0.in') as data:
    n = int(data.readline().strip())
    prices = {}
    for i in range(n):
        prices[i + 1] = int(data.readline().strip())
    m = int(data.readline().strip())
    processes_prices = {}
    processes = {}
    for j in range(m):
        a, b, c = tuple([int(i) for i in data.readline().strip().split()])
        processes[a] = processes.get(a, []) + [b]
        processes_prices[(a, b)] = c


def count_tax(metal):
    return prices[metal] * 0.5


def reverse_processes(processes):
    rev = {}
    for key in processes:
        for val in processes[key]:
            rev[val] = rev.get(val, []) + [key]
    return rev


def weight(a, b):
    return processes_prices[(a, b)]

source = 1
dist = {}
q = set()
for v in processes:
    dist[v] = float('inf')
    q.add(v)
dist[source] = 0
while len(q) > 0:
    v = min(q, key=lambda x: dist[x])
    q.remove(v)
    for u in processes[v]:
        dist[u] = dist[v] + weight(v, u) if dist[u] > dist[v] + weight(v, u) else dist[u]

rev_proc = reverse_processes(processes)
rev_dist = {}
q = set()
for v in rev_proc:
    rev_dist[v] = float('inf')
    q.add(v)
rev_dist[source] = 0
while len(q) > 0:
    v = min(q, key=lambda x: rev_dist[x])
    q.remove(v)
    for u in rev_proc[v]:
        rev_dist[u] = rev_dist[v] + weight(u, v) if rev_dist[u] > rev_dist[v] + weight(u, v) else rev_dist[u]

min_price = float('inf')
for metal in processes:
    price = dist[metal] + rev_dist[metal] + count_tax(metal)
    if price < min_price:
        min_price = price
print min_price

