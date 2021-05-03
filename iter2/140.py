from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        @lru_cache(None)
        def helper(i):
            if i == len(s): return [""]
            ans = []
            word = ""
            for q in range(i, len(s)):
                word += s[q]
                if word in words:
                    next = helper(q+1)
                    ans += list(map(lambda x : f"{word} {x}".strip(), next))
            return ans
        return helper(0)