'''
Example 1:
    input: s = "PPALLP"

Approch 1: check1(), check2(), O(N), O(1)
    check1: count A, O(N), O(1)
    check2: s[i:i+3] == "LLL" ?, O(N), O(1)
'''

class Solution:
    def checkRecord(self, s: str) -> bool:
        # check 1
        cnt = 0
        for a in s:
            if a == "A":
                cnt += 1
        if cnt >= 2:
            return False

        # check 2
        for i in range(len(s)-2):
            if s[i:i+3] == "LLL":
                return False

        return True

