class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:

        left, right, total = len(s)-1, 0, 0
        d = {}
        for i, c in enumerate(s):
            if c not in d:
                d[c] = (i, i, 1)
            else:
                d[c] = (d[c][0], i, d[c][2]+1)

        ans = []
        for c, (l, r, cnt) in d.items():
            if r-l+1 == cnt:
                ans.append(c*cnt)
                left = min(l, left)
                right = max(r, right)
                total += cnt

        if left == len(s)-1 and right == 0:
            ans.append(s)
        elif right == len(s)-1 and left != 0 and right-left+1 == total:
            ans.append(s[:left])
        elif left == 0 and right != len(s)-1 and right-left+1 == total:
            ans.append(s[right+1:])
        return ans

