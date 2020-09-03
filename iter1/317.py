class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        buildings = []
        for i in range(rows):
            for q in range(cols):
                if grid[i][q] == 1:
                    buildings.append((i, q))

        costs = collections.defaultdict(lambda : collections.defaultdict(int))
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        for i, building in enumerate(buildings):
            seen = set()
            q = collections.deque([(building[0]+dx, building[1]+dy, 1) for dx, dy in dirs])

            while len(q):
                r, c, cost = q.popleft()

                if ((not (0 <= r < rows and 0 <= c < cols)) or
                        (r, c) in seen or grid[r][c] != 0):
                    continue
                seen.add((r, c))
                # core code: if the current land can not visted by previous
                # building, then we do not search this land
                if len(costs[(r, c)]) != i: continue
                costs[(r, c)][building] += cost
                q += [(r+dx, c+dy, cost+1) for dx, dy in dirs]
        ret = float('inf')
        for cost in costs.values():
            #print(cost)
            if len(cost) != len(buildings): continue
            ret = min(ret, sum(cost.values()))

        return -1 if ret == float('inf') else ret

