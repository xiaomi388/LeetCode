import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        ret = []
        for i in range(len(nums)):
            while (len(q) and (i - q[0] >= k)): q.popleft()
            while (len(q) and nums[q[-1]] < nums[i]): q.pop()
            q.append(i)
            if (i >= k):
                ret.append(nums[q[0]])
        return ret





