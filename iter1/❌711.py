class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:

        visited = set()

        def dfs(shape, lw, r, c, i, j):
            if (not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or
                    (r, c) in visited or grid[r][c] == "0"):
                return

            shape.add((i, j))
            for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                dfs(shape, r+dx, c+dx, i+dx, j+dy)

        def rotate(shape):
            t = [s[1] for s in shape]
            length = max(t) - min(t)
            t = [s[0] for s in shape]
            width = max(t) - min(t)
            shapes = [shape]

            for i in range(3):
                next_shape = set()
                for s in shape:
                    next_shape.add((width-shape[1], length-shape[0]))
                shapes.append(next_shape)
                shape = next_shape
                width = length
                length = width
            return shapes


        shapes = set()
        for i in range(len(grid)):
            for q in range(len(grid[0])):
                if grid[i][q] == "1" and (i, q) not in visited:
                    shape = set()
                    dfs(shape, i, q, 0, 0)
                    shapes.update([frozenset(s) for s in rotate(shape)])
        return len(shapes)



