from collections import defaultdict

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnter = defaultdict(int)
        for el in arr:
            cnter[el] += 1
        els = sorted(cnter.items(), key=lambda x : x[1])
        out = len(els)
        for el, cnt in els:
            k -= cnt
            if k >= 0:
                out -= 1
            else:
                return out
        return out
