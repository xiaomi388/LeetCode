from functools import lru_cache

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)

        @lru_cache(None)
        def dfs(i, k):
            if i > stones[-1] or i not in stone_set:
                return False
            if i == stones[-1]:
                return True
            return any(dfs(i+k+1, k+1), dfs(i+k, k), dfs(i+k-1, k-1))

        if 1 not in stone_set:
            return False
        return dfs(2, 1) or dfs(3, 2)







