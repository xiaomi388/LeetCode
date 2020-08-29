class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows = len(maze); cols = len(maze[0])
        visited = set()

        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))
        def dfs(row, col):
            if not (0 <= row < rows and 0 <= col < cols
                    and (row, col) not in visited):
                return
            if row == destination[0] and col == destination[1]:
                return True
            visited.add((row, col))
            for dx, dy in dirs:
                x = row; y = col
                while 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0:
                    x += dx
                    y += dy
                x -= dx
                y -= dy
                if dfs(x, y):
                    return True
            return False

        return dfs(*start)



