# min_effort
# dfs(i, j, w)
#    if (i, j) is the target, then update min_effort to be min(min_effort, w)
#    else dfs to other cells

import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        hq = [(0, 0, 0)]
        visited = set()
        while len(hq):
            e, r, c = heapq.heappop(hq)
            #print(e, r, c)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if r == len(heights)-1 and c == len(heights[0])-1:
                return e
            for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                if 0 <= r+dx < len(heights) and 0 <= c+dy < len(heights[0]):
                    dif = abs(heights[r][c] - heights[r+dx][c+dy])
                    heapq.heappush(hq, (max(e, dif), r+dx, c+dy))







