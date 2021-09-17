class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0

        out = float('inf')
        nums.sort()
        for i in range(4):
            out = min(out, nums[-4+i] - nums[i])
        return out

