# Kruskal: 选边

class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        p = list(range(N+1))

        def find(x):
            if p[x] != x: p[x] = find(p[x])
            return p[x]

        connections.sort(key=lambda x : x[2])
        costs = []
        for v, u, cost in connections:
            rv, ru = find(v), find(u)
            if rv == ru: continue
            p[ru] = rv
            costs.append(cost)
            if len(costs) == N-1: return sum(costs)
        return -1

# Prim: 选点
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for conn in connections:
            graph[conn[0]].append((conn[1], conn[2]))
            graph[conn[1]].append((conn[0], conn[2]))
        costs = 0
        seen = set()
        q = [(0, 1)]
        while len(seen) != N:
            if not len(q): return -1
            cost, v = heapq.heappop(q)
            if v in seen: continue
            seen.add(v)
            costs += cost
            for u, cost in graph[v]:
                heappush(q, (cost, u))
        return costs

