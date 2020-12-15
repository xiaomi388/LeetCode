# brute force: scan all points and calculate the corresponding distance.
# a better solution: knowing the fact that the median point is the optimized point.

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows = [i for i in range(len(grid)) for q in range(len(grid[0])) if grid[i][q]==1]
        cols = [i for i in range(len(grid[0])) for q in range(len(grid)) if grid[q][i]==1]
        return reduce(lambda a, x : a+abs(rows[len(rows)//2]-x[0])+abs(cols[len(cols)//2]-x[1]), zip(rows, cols), 0)







