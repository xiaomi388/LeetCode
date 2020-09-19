# 滑动窗口法
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = collections.Counter(t)
        n, l, r, ans = 0, 0, 0, ""

        for r in range(len(s)):
            if s[r] not in cnt: continue
            cnt[s[r]] -= 1
            if cnt[s[r]] == 0: n += 1

            while s[l] not in cnt or cnt[s[l]] < 0:
                if s[l] in cnt: cnt[s[l]] += 1
                l += 1
            if n == len(cnt):
                ans = min(ans, s[l:r+1], key=lambda x: len(x) if x else float('inf'))
        return ans





