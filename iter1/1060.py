# brute force
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(1, len(nums)):
            cnt += nums[i] - nums[i-1] - 1
            if cnt >= k:
                return nums[i] - (cnt - k + 1)
        return nums[-1] + (k - cnt)

# bisect
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi-1:
            mid = (lo + hi) // 2
            slots = nums[mid] - nums[lo] - 1 - (mid - lo - 1)
            if slots == k:
                return nums[mid]-1
            elif slots < k:
                lo = mid
                k -= slots
            else:
                hi = mid
        return nums[lo] + k






