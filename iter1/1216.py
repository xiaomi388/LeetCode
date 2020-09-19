from functools import lru_cache

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        @lru_cache(None)
        def dfs(lo, hi, k):
            if lo >= hi: return True
            if s[lo] == s[hi]:
                return dfs(lo+1, hi-1, k)
            return k > 0 and (dfs(lo+1, hi, k-1) or dfs(lo, hi-1, k-1))
        return dfs(0, len(s)-1, k)


