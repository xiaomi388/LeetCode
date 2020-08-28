class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        begin = 0; end = len(nums)

        def upperBound():
            left = begin; right = end
            while left < right:
                mid = (left + right) / 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        def lowerBound():
            left = begin; right = end
            while left < right:
                mid = (left + right) / 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        lower = lowerBound()
        upper = upperBound()
        return [lower, upper-1] if 0 <= lower < end and 0 < upper <= end else [-1, -1]



