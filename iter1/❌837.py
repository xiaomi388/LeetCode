# N = 10, K = 2, W = 10
# [1, 10] -> 1 -> 10 -> 11 points -> more than N points
#         -> more than 1 points -> less than / equal to N points
# (1, 10)
# dfs(N, K, W): W choices.
# ans = 0
# for w in range(1, W+1):
#   p = dfs(N-w, K-w, W)
#   ans += p / W
# return ans
# time complexity: O(k)

from functools import lru_cache

class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        @lru_cache(None)
        def dfs(N, K):
            if N < 0: return 0
            if K <= 0: return 1
            ans = 0
            for w in range(1, W+1):
                p = dfs(N-w, K-w)
                ans += p
            return ans / W
        return dfs(N, K)