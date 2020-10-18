class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        d, rd = {}, {}
        def dfs(i, begin):
            # optimization 1
            if len(pattern) - i > len(s) - len(begin):
                return False
            if i == len(pattern):
                if begin == len(s):
                    return True
                return False

            # optimization 2
            if pattern[i] in d:
                word = s[begin:begin+len(d[pattern[i]])]
                if d[pattern[i]] != word: return False
                return dfs(i+1, begin+len(d[pattern[i]]))

            for q in range(begin, len(s)):
                word = s[begin:q+1]
                if word in rd and rd[word] != pattern[i]: continue
                old_p = rd[word] if word in rd else None
                d[pattern[i]] = word
                rd[word] = pattern[i]
                ans = dfs(i+1, q+1)
                del d[pattern[i]]
                if not old_p: del rd[word]
                if ans: return True
            return False
        if not len(pattern) and not len(s): return True
        if not len(pattern) or not len(s): return False
        return dfs(0, 0)







