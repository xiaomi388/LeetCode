from functools import reduce
from collections import defaultdict

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        buckets = defaultdict(int)
        ret = 0
        for answer in answers:
            buckets[answer] += 1
            if buckets[answer] == answer+1:
                del buckets[answer]
                ret += answer+1
        for num in buckets:
            ret += num+1
        return ret
