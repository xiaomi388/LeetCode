# 1. find a valid window
# 2. calculate all substring containing this window
# 3. offset this window

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l, r  = 0, 0
        cnter = {"a": 0, "b": 0, "c": 0}

        out = 0
        while r < len(s):
            cnter[s[r]] += 1
            while all([cnter[key] >= 1 for key in cnter]):
                out += (len(s) - r)
                cnter[s[l]] -= 1
                l += 1
            r += 1
        return out



