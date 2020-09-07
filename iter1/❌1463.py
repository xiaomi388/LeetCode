from functools import lru_cache
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        @lru_cache(None)
        def dfs(x, y1, y2):
            if x == r: return 0
            cur = grid[x][y1] + (grid[x][y2] if y1 != y2 else 0)
            next = 0
            for dir1 in (0, -1, 1):
                for dir2 in (0, -1, 1):
                    if all([0 <= i < c for i in (y1+dir1, y2+dir2)]):
                        next = max(next, dfs(x+1, y1+dir1, y2+dir2))
            return cur + next
        return dfs(0, 0, c-1)










