# dfs with memo
# the main point is scanning the string from right to left
# because we need to know if a character is followed by a *.
# if we scan from left to right, we may hard to be sure
# if we should match the current char in the pattern with
# the current char of the string, because if it is followed
# by a *, then we can skip the current char in the pattern.

from functools import lru_cache

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        @lru_cache(None)
        def dfs(si, pi):
            # print(si, pi)
            if si < 0 and pi < 0: return True
            if pi < 0: return False
            if si < 0:
                if p[pi] == "*": return dfs(si, pi-2)
                else: return False
            # normal case
            if p[pi] == ".": return dfs(si-1, pi-1)
            elif p[pi] == "*":
                if dfs(si, pi-2): return True
                while si >= 0 and pi-1 >= 0 and (s[si] == p[pi-1] or p[pi-1] == "."):
                    if dfs(si:=si-1, pi-2):
                        return True
            else:
                if p[pi] != s[si]: return False
                return dfs(si-1, pi-1)
            return False
        return dfs(len(s)-1, len(p)-1)

