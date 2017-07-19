with open('in/prz1c.in') as data:
    n = int(data.readline().strip())
    prices = {}
    for i in range(n):
        prices[i + 1] = int(data.readline().strip())
    print prices
    m = int(data.readline().strip())
    processes_prices = {}
    processes = {}
    for j in range(m):
        a, b, c = tuple([int(i) for i in data.readline().strip().split()])
        processes[a] = processes.get(a, []) + [b]
        processes_prices[(a, b)] = c


def count_tax(metal):
    return prices[metal] / 2


def weight(a, b):
    return processes_prices[(a, b)]


def inverse_processes():
    inv_proc = {}
    for metal_a in processes:
        for metal_b in processes[metal_a]:
            inv_proc[metal_b] = inv_proc.get(metal_b, []) + [metal_a]
    return inv_proc


dist = {}
q = set()
source = 1
for v in processes:
    q.add(v)
    dist[v] = float('inf')
dist[source] = 0
while len(q) != 0:
    u = min(q, key=lambda x: dist[x])
    q.remove(u)
    for v in processes[u]:
        if dist.get(v) is None:
            dist[v] = float('inf')
        if dist[v] > dist[u] + weight(u, v):
            dist[v] = dist[u] + weight(u, v)

inv_proc = inverse_processes()
inv_dist = {}
q = set()
source = 1
for v in inv_proc:
    q.add(v)
    inv_dist[v] = float('inf')
inv_dist[source] = 0

while len(q) != 0:
    u = min(q, key=lambda x: inv_dist[x])
    q.remove(u)
    for v in inv_proc[u]:
        if inv_dist.get(v) is None:
            inv_dist[v] = float('inf')
        if inv_dist[v] > inv_dist[u] + weight(v, u):
            inv_dist[v] = inv_dist[u] + weight(v, u)


def count_price(metal):
    return dist[metal] + inv_dist[metal] + count_tax(metal)

print min([count_price(metal) for metal in prices])

