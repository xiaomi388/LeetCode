# 我们目标是要求出一个连续区间，这个区间的水果数量最多，所以用双指针法来遍历连续区间即可

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        ret = 0
        d = dict()
        lo, hi = 0, 0
        while hi < len(tree):
            if tree[hi] in d:
                d[tree[hi]] += 1
            else:
                while len(d) == 2:
                    d[tree[lo]] -= 1
                    if d[tree[lo]] == 0:
                        del d[tree[lo]]
                    lo += 1
                d[tree[hi]] = 1
            ret = max(ret, sum([d[t] for t in d]))
            hi += 1
        return ret
