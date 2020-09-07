# 难点：问题可转化成2个人同时从起点出发，到达终点，能够收集到的cherry的总数
# 我们把两人的位置保存到状态中。
# 复杂度估算：grid大小10以内，可考虑搜索。若>50，则必然是dp

from functools import lru_cache
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        @lru_cache(None)
        def dfs(x1, y1, x2, y2):
            if (x1, y1, x2, y2) == (r-1, c-1, r-1, c-1):
                return grid[r-1][c-1]
            n = -1
            for dx1, dy1 in ((1, 0), (0, 1)):
                for dx2, dy2 in ((1, 0), (0, 1)):
                    tx1, ty1, tx2, ty2 = x1+dx1, y1+dy1, x2+dx2, y2+dy2
                    if not (0 <= tx1 < r and 0 <= tx2 < r and
                            0 <= ty1 < c and 0 <= ty2 < c and
                            grid[tx1][ty1] != -1 and grid[tx2][ty2] != -1):
                        continue
                    n = max(n, dfs(tx1, ty1, tx2, ty2))
            if n == -1: return n
            return n+grid[x1][y1]+(grid[x2][y2] if (x1, y1) != (x2, y2) else 0)
        return max(0, dfs(0, 0, 0, 0))


