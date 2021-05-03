class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist_of = lambda p1, p2 : abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        if len(points) == 0: return 0
        visited = set()
        hq = [(0, None, points[0])]
        ans = 0
        while len(hq):
            dist, start, end = heapq.heappop(hq)
            if tuple(end) in visited: continue
            visited.add(tuple(end))
            ans += dist
            if len(visited) == len(points): break
            next_points = [p for p in points if p != end and tuple(p) not in visited]
            for p in next_points:
                heapq.heappush(hq, (dist_of(end, p), end, p))
        return ans
