class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        begin = 0; end = len(nums)

        def upperBound():
            left = begin; right = end
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return right

        def lowerBound():
            left = begin; right = end
            while left < right:
                mid = left + right // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        lower = lowerBound()
        upper = upperBound()
        return [lower, upper-1] if lower != upper else [-1, -1]



