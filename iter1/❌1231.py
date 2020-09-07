# https://leetcode-cn.com/problems/divide-chocolate/
# https://blog.csdn.net/qq_17550379/article/details/102646247


# DFS: TLE
# 可学习的点： 1. functools - lru_cache
from functools import lru_cache
class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        res, n = 0, len(sweetness)
        @lru_cache(None)
        def dfs(u, t, m):
            nonlocal res
            if t == K:
                res = max(res, min(m, sum(sweetness[u:])))
                return
            for i in range(u, n):
                dfs(i + 1, t + 1, min(m, sum(sweetness[u:i+1])))
        dfs(0, 0, float("inf"))
        return res

# 二分搜索法：我们可以知道自己的那份巧克力的甜度要<其他所有人，所以
# 自己的巧克力甜度的取值范围只可能是[1, total // K+1]，
# 否则自己的巧克力不可能甜度都小于其他的人, 所以我们可以二分查找自己的甜度是多少
class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        l, r = 1, (sum(sweetness) // K+1) + 1
        while l < r:
            mid = l + r // 2
            cur = cnt = 0
            for sw in sweetness:
                cur += sw
                if cur >= mid:
                    cnt += 1
                    cur = 0
            if cnt > K:
                l = mid + 1
            else:
                r = mid
        return l


