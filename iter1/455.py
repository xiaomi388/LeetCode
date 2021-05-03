class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, q, cnt = 0, 0, 0
        while i < len(g) and q < len(s):
            if g[i] <= s[i]:
                cnt += 1
                i += 1
            q += 1
        return cnt
