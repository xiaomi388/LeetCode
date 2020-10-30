# observation 1: if we put one mailbox among houses[i, j], then we should
# put the mailbox to the median house

# observation 2: we should divide all houses into k groups


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        # the cost of putting one mailbox among houses[i, q]
        houses.sort()
        cost = {}
        for i in range(len(houses)):
            for q in range(i, len(houses)):
                cost[(i, q)] = 0
                mid = (i + q) // 2
                cost[(i, q)] = sum([abs(houses[x] - houses[mid]) for x in range(i, q+1)])
        dp = {}
        for i in range(len(houses)+1):
            for j in range(k+1):
                if j == 0 and i == 0: dp[(i,j)] = 0
                elif j == 0 or i == 0: dp[(i,j)] = math.inf
                else:
                    dp[(i, j)] = math.inf
                    for x in range(i, 0, -1):
                        dp[(i, j)] = min(cost[(x-1, i-1)] + dp[(x-1, j-1)], dp[(i, j)])
        return dp[(len(houses), k)]


