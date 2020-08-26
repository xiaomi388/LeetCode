class Solution(object):
    def minimumCost(self, N, connections):
        """
        :type N: int
        :type connections: List[List[int]]
        :rtype: int
        """

        cost = [[float('inf')] * N] * N
        for i, j, c in connections:
            cost[i][j] = c

        for i in range(N):
            for q in range(N):
                if i == q:
                    cost[i][q] = 0
                    continue
                for k in range(N):
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
        return min([cost[i][j] for i in range(N) for q in range(N)])

