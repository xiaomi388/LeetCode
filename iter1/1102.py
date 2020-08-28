class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        rows = len(A); cols = len(A[0])
        visited = set()
        q = [(-A[0][0], (0, 0))]
        ret = A[0][0]
        while len(q):
            val, cord = heapq.heappop(q)
            val = -val
            ret = min(ret, val)
            visited.add(cord)
            dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))
            for dx, dy in dirs:
                nextCord = (cord[0]+dx, cord[1]+dy)
                if nextCord == (rows-1, cols-1):
                    return min(ret, A[nextCord[0]][nextCord[1]])
                elif (0 <= nextCord[0] < rows and 0 <= nextCord[1] < cols 
                        and nextCord not in visited):
                    heapq.heappush(q, (-A[nextCord[0]][nextCord[1]], nextCord))
        return ret
