class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        d = collections.defaultdict(int)
        l, ret = 0, 0
        for r in range(1, len(s)+1):
            d[s[r-1]] += 1
            while len(d) > 2:
                d[s[l]] -= 1
                if d[s[l]] == 0: del d[s[l]]
                l += 1
            ret = max(ret, r-l)
        return ret
