class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0

        nums.sort()
        out = float('inf')
        for rorate in range(4):
            _max = nums[-rorate-1]
            _min = nums[3-rorate]
            out = min(out, _max-_min)
        return out