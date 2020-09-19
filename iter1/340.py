class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        d = collections.defaultdict(int)
        l, ans = 0, 0
        for r in range(1, 1+len(s)):
            d[s[r-1]] += 1
            while len(d) > k:
                d[s[l]] -= 1
                if d[s[l]] == 0: del d[s[l]]
                l += 1
            ans = max(ans, r-l)

        return ans


