from functools import lru_cache
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:

        @lru_cache(None)
        def find_a_r(r, c):
            return pizza[r][c:].find("A") != -1

        @lru_cache(None)
        def find_a_c(r, c):
            return any([i[c] == "A" for i in range(r, len(pizza))])


        @lru_cache(None)
        def dfs(r, c, k):
            if not (0 <= r < len(pizza) and 0 <= c <= len(pizza[0])): return 0
            if k == 0: return int(any([find_a_r(i, c) for i in range(r, len(pizza)-1)]))
            ans = 0
            i = r
            while i < len(pizza) and not find_a_r(i, c): i += 1
            for i in range(i+1, len(pizza)):
                ans += dfs(i, c, k-1)

            i = c
            while i < len(pizza[0]) and not find_a_c(r, i): i += 1
            for i in range(i+1, len(pizza[0])):
                ans += dfs(r, i, k-1)
            return ans





