from dealavo_dev_challenge.challenge import Challenge


class Challenge_2(Challenge):

    def solve_challenge(self, filename):

        with open(filename) as data:
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
            return prices[metal]/2

        def weight(a, b):
            return processes_prices[(a, b)]

        def invert(processes):
            res = {}
            for metal in processes:
                for node in processes[metal]:
                    update = res.get(node, [])
                    update.append(metal)
                    res[node] = update
            return res

        q = set()
        dist = {}
        source = 1
        for v in processes:
            q.add(v)
            dist[v] = float('inf')
        dist[source] = 0
        while len(q) > 0:
            u = min(q, key=lambda x: dist[x])
            q.remove(u)
            for v in processes[u]:
                alt = dist[u] + weight(u, v)
                if dist.get(v, float('inf')) > alt:
                    dist[v] = alt

        inv_proc = invert(processes)
        q = set()
        inv_dist = {}
        for v in inv_proc:
            q.add(v)
            inv_dist[v] = float('inf')
        inv_dist[source] = 0
        while len(q) > 0:
            u = min(q, key=lambda x: inv_dist[x])
            q.remove(u)
            for v in inv_proc[u]:
                alt = inv_dist[u] + weight(v, u)
                if inv_dist.get(v, float('inf')) > alt:
                    inv_dist[v] = alt

        def count_price(metal):
            return dist[metal] + inv_dist[metal] + count_tax(metal)

        return min([count_price(metal) for metal in processes]) if len(processes) > 0 else count_tax(source)

