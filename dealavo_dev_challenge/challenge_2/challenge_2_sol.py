with open('prz0.in') as input:
    metal_type_count = int(input.readline().strip())
    metal_prices = {}
    for i in range(metal_type_count):
        metal_prices[str(i + 1)] = int(input.readline().strip())
    processes_count = int(input.readline().strip())
    processes = {}
    processes_prices = {}
    for j in range(processes_count):
        data = input.readline().strip().split()
        data_to_update = processes.get(data[0], [])
        data_to_update.append(data[1])
        processes[data[0]] = data_to_update
        processes_prices[(data[0], data[1])] = int(data[2])

print processes_prices
print processes

def count_tax(metal):
    return metal_prices[metal] / 2


def weight(node_a, node_b, inverted=False):
    return processes_prices[(node_a, node_b)] if not inverted else processes_prices[(node_b, node_a)]


def shortest_path(processes, source, inverted=False):
    if inverted:
        processes = invert_processes(processes)
    q = set()
    dist = {}
    for v in processes:
        dist[v] = float('inf')
        q.add(v)
    dist[source] = 0
    while len(q) > 0:
        u = min(q, key=lambda x: dist[x])
        q.remove(u)
        for v in processes[u]:
            alt = dist[u] + weight(u, v) if not inverted else dist[u] + weight(u, v, True)
            if alt < dist.get(v, float('inf')):
                dist[v] = alt
    return dist


def invert_processes(processes):
    inv_processes = {}
    for key in processes:
        nodes = processes[key]
        for node in nodes:
            inv_processes[node] = inv_processes.get(node, []) + [key]
    return inv_processes


def count_real_path_cost(target_node, dist, inv_dist):
    process_price = dist[target_node] + inv_dist[target_node]
    tax = count_tax(target_node)
    return process_price + tax

dist = shortest_path(processes, '1')
inv_dist = shortest_path(processes, '1', True)

print min([count_real_path_cost(metal, dist, inv_dist) for metal in dist])