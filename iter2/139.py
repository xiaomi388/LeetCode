from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        @lru_cache(None)
        def helper(i):
            if i == len(s): return True
            word = ""
            for q in range(i, len(s)):
                word += s[q]
                if word in words and helper(q+1):
                    return True
            return False
        return helper(0)
