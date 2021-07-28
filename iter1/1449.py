from functools import lru_cache


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        @lru_cache(None)
        def helper(t):
            ret = ""
            for i in range(0, 9):
                d = i + 1
                if cost[i] == t:
                    candidate = str(d)
                    if ret == "" or int(ret) < int(candidate):
                        ret = str(d)
                elif cost[i] > t:
                    continue
                else:
                    r = helper(t - cost[i])
                    if r == "":
                        continue
                    candidate = str(d) + r
                    if ret == "" or int(ret) < int(candidate):
                        ret = candidate
            return ret

        ret = helper(target)
        return "0" if ret == "" else ret

