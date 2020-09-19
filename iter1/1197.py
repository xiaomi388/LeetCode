class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        def dist(x1, y1, x2, y2):
            return abs(y1-y2) + abs(x1-x2)

        q = [(0, dist(0, 0, x, y), (0, 0))]
        seen = set()
        seen.add((0, 0))

        while len(q):
            cnt, d, (curx, cury) = heapq.heappop(q)
            if (curx, cury) == (x, y): return cnt
            for dx, dy in ((2, 1), (1, 2), (-2, -1), (-1, -2), (1, -2), (2, -1), (-1, 2), (-2, 1)):
                tx, ty = curx+dx, cury+dy
                if (tx, ty) in seen: continue
                nextd = dist(tx, ty, x, y)
                if nextd > 10 and nextd > d-1: continue
                if nextd > 600: continue
                heapq.heappush(q, (cnt+1, dist(tx, ty, x, y), (tx, ty)))
                seen.add((tx, ty))
        return -1
