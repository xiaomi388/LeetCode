class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if len(grid) == 0: return 0
        rows, cols = len(grid), len(grid[0])
        ans = 0
        for i in range(rows):
            for q in range(cols):
                if grid[i][q] != 1: continue
                cnt = 4
                for x, y in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    if not (0 <= i+x < rows and 0 <= q+y < cols): continue
                    if grid[i+x][q+y] == 1:
                        cnt -= 1
                ans += cnt
        return ans