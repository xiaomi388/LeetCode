class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        q = collections.deque()
        d = [-1] * len(nums)
        for i in range(len(nums)):
            while len(q) and nums[i] > nums[q[-1]]:
                d[q.pop()] = nums[i]
            q.append(i)
        for i in range(len(nums)):
            while len(q) and nums[i] > nums[q[-1]]:
                d[q.pop()] = nums[i]
            q.append(i)
        return d

