# 方法一： 用set保存每个灯泡的位置。每次插入灯泡时判断下与隔壁的距离是否等于K
# Time: O(nlogn) Space: O(n)

import sortedcontainers

class Solution:
    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        s = sortedcontainers.SortedSet()
        for i, bulb in enumerate(bulbs):
            s.add(bulb)
            prev = s.index(bulb) - 1
            next = s.index(bulb) + 1
            if prev >= 0 and bulb - s[prev] == K+1: return i+1
            elif next < len(s) and s[next] - bulb == K+1: return i+1
        return -1


# 方法二： bucket，可以把1~k朵花都放到同一个bucket中，只记录桶中最大/最小值
# 可以发现在同一个桶中的花不可能满足条件，因为<K+1
# Time: O(n) Space: O(n/k)
# 划分窗口法：适用于求间隔的题目
class Solution:
    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        bucket = dict()
        for i, bulb in enumerate(bulbs):
            idx = bulb//k
            if idx not in bucket:
                bucket[idx] = (bulb, bulb)
            else:
                bucket[idx] = (min(bucket[idx][0], bulb), max(bucket[idx][1], bulb))
            if idx-1 in bucket and bucket[idx][0] - bucket[idx-1][1] == K+1:
                return i+1
            if idx+1 in bucket and bucket[idx+1][0] - bucket[idx][1] == K+1:
                return i+1
        return -1

# 方法三：滑动窗口法


