from functools import lru_cache


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # set up 16 buckets
        maxlen = 1
        buckets = [[] for _ in range(17)]
        for word in words:
            maxlen = max(maxlen, len(word))
            buckets[len(word)].append(word)

        # print(buckets)
        # print(maxlen)
        # assume len(pre) == len(cur)-1
        def is_predecessor(pre, cur):
            flag = True
            i, j = 0, 0
            while i < len(pre) and j < len(cur):
                if pre[i] != cur[j]:
                    if flag:
                        flag = False
                        j += 1
                    else:
                        return False
                else:
                    i += 1
                    j += 1
            return True

        # dfs with memorization
        @lru_cache(None)
        def dfs(i, j):
            if i == 1:
                return 1

            ret = 1
            for u in range(len(buckets[i - 1])):
                if is_predecessor(buckets[i - 1][u], buckets[i][j]):
                    ret = max(ret, dfs(i - 1, u) + 1)
            return ret

        ret = 1
        for i in range(1, maxlen + 1):
            for j in range(len(buckets[i])):
                ret = max(ret, dfs(i, j))
        return ret


