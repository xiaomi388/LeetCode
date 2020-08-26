class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        shapes = set()

        def dfs(r, c, shape):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or (r, c) in visited:
                return
            shape.add((r, c))
            for i, q in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                dfs(r, c, shape)

        for i in range(len(grid)):
            for q in range(len(grid[0])):
                if (i, q) not in visited:
                    shape = set()
                    dfs(i, q, shape)
                    shapes.add(shape)
        return len(shapes)














