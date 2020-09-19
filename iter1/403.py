from functools import lru_cache

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        begin, end = stones[0], stones[-1]
        stones = set(stones)

        @lru_cache(None)
        def dfs(i, l):
            if i == end:
                return True
            if i not in stones:
                return False

            if l == 0:
                return dfs(i+1, 1)
            if l == 1:
                return dfs(i+1, 1) or dfs(i+2, 2)

            return dfs(i+l-1, l-1) or dfs(i+l, l) or dfs(i+l+1, l+1)
        return dfs(begin, 0)
