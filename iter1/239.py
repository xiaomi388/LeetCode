class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = list()
        q = collections.deque()
        for i, num in enumerate(nums):
            if len(q) and q[0][0] <= i - k: q.popleft()
            while len(q) and num > q[-1][1]: q.pop()
            q.append((i, num))
            if i >= k-1: ret.append(q[0][1])
        return ret