class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0: return 0

        # mark what points we've visited
        visited = set()
        shapes = set()

        def dfs(r, c, ir, ic, shape):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])): return
            if (r, c) in visited: return
            if grid[r][c] == 0: return
            visited.add((r, c))
            dx, dy = r-ir, c-ic
            shape.append((dx, dy))
            dfs(r+1, c, ir, ic ,shape)
            dfs(r-1, c, ir, ic ,shape)
            dfs(r, c+1, ir, ic ,shape)
            dfs(r, c-1, ir, ic ,shape)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0: continue
                shape = []
                dfs(r, c, r, c, shape)
                shape = tuple(shape)
                shapes.add(shape)
        print(shapes)
        return len(shapes)

