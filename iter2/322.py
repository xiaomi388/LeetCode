from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dfs(amount):
            if amount == 0: return 0
            ans = min([dfs(amount-i) for i in coins if i <= amount], default=float('inf'))
            return ans+1 if ans != float('inf') else ans
        return ans if ans != float('inf') else -1