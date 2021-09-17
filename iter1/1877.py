class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        out = 0
        nums.sort()
        for i in range(len(nums) // 2):
            out = max(out, nums[i] + nums[len(nums)-i-1])
        return out
