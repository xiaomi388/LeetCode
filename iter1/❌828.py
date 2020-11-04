from functools import lru_cache

# brute force: O(N^3)
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            for q in range(i, len(s)):
                seen = collections.defaultdict(int)
                for x in range(i, q+1):
                    seen[s[x]] += 1
                uni = 0
                for c in seen:
                    if seen[c] == 1:
                        uni += 1
                ans += uni
        return ans

# brute force with optimization
# O(n^2)
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        @lru_cache(None)
        def get_seen(i, q):
            seen = collections.defaultdict(int)
            if i <= q:
                seen = get_seen(i, q-1)
                seen[s[q]] += 1
            return seen

        ans = 0
        for i in range(len(s)):
            for q in range(i, len(s)):
                seen = get_seen(i, q)
                uni = 0
                for c in seen:
                    if seen[c] == 1:
                        uni += 1
                ans += uni
        return ans


# pre_sum
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        index_of = collections.defaultdict(lambda : [-1, -1])
        res = 0
        for i, c in enumerate(s):
            q, j = index_of[c]
            res += (i-q) * (j-q)
        for c in enumerate(index_of):
            res += (len(s)-index_of[c][1]) * (index_of[c][1]-index_of[c][0])
        return res













