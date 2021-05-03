from functools import lru_cache

#aabcddcba
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def helper(lo, hi):
            if lo > hi: return 0
            if lo == hi: return 1
            ans = 0
            if s[lo] == s[hi]:
                ans = max(ans, 2+helper(lo+1, hi-1))
            else:
                ans = max(ans, helper(lo, hi-1))
                ans = max(ans, helper(lo+1, hi))
            return ans
        return helper(0, len(s)-1)
