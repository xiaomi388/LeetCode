class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        freqs = collections.defaultdict(int)
        lo, hi = 0, 0
        while hi < len(s):
            freqs[s[hi]] += 1
            ans = max(ans, freqs[s[hi]])
            if hi-lo+1-ans > k:
                freqs[s[lo]] -= 1
                lo += 1
            hi += 1
        return ans
