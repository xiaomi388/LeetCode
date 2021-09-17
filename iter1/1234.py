# 1. count every chars (Q: a, W: b, E: c, R: d), a, b > (total // 4) n
# 2. find all substrings that contains a-n Q and b-n W
# 3. return the minimum one

from collections import defaultdict

class Solution:
    def balancedString(self, s: str) -> int:
        # count
        cnter = defaultdict(int)
        for i in range(len(s)):
            cnter[s[i]] += 1

        # find subplus chars
        surplus = {}
        for c in cnter:
            if cnter[c] > len(s) // 4:
                surplus[c] = cnter[c] - len(s) // 4

        # if already balanced, return 0
        if len(surplus) == 0:
            return 0

        # sliding window to find substring
        ans = float('inf')
        l = 0
        cnter = defaultdict(int)

        for r in range(len(s)):
            cnter[s[r]] += 1

            # check if is a valid substring
            is_valid = True
            for c in surplus:
                if cnter[c] < surplus[c]:
                    is_valid = False
                    break
            if not is_valid:
                continue

            while l < r and (s[l] not in surplus or cnter[s[l]] > surplus[s[l]]):
                cnter[s[l]] -= 1
                l += 1
            ans = min(ans, r-l+1)
        return ans





