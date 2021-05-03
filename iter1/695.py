# solution 1
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # visited coordinate
        visited = set()
        max_cnt = 0

        def search(r, c):
            cnt = 1
            visited.add((r, c))
            for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                if (len(grid) > r + dx >= 0 and
                    len(grid[0]) > c + dy >= 0 and
                        (r+dx, r+dy) not in visited and
                        grid[r+dx][c+dy] == 1):
                    cnt += search(r, c)
            return cnt

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) in visited or grid[r][c] == 0:
                    continue
                max_cnt = max(search(r, c), max_cnt)
        return max_cnt

# solution 2
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # visited coordinate
        visited = set()
        max_cnt = 0

        def search(r, c, state):
            cnt = 1
            visited.add((r, c))
            for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                if (len(grid) > r + dx >= 0 and
                        len(grid[0]) > c + dy >= 0 and
                        (r+dx, r+dy) not in visited and
                        grid[r+dx][c+dy] == 1):
                    cnt += search(r, c)
            return cnt

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) in visited or grid[r][c] == 0:
                    continue
                max_cnt = max(search(r, c), max_cnt)
        return max_cnt
