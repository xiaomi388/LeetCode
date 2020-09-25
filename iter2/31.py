class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. scan from end to begin till we find the first un-ascending element
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                break
        else:
            nums.reverse()
            return nums
        # find the element slightly smaller than nums[i]
        for q in range(i+1, len(nums)):
            if nums[q] <= nums[i]:
                break
        else:
            q += 1
        # swap i and q-1 (slightly greater than nums[i])
        nums[i], nums[q-1] = nums[q-1], nums[i]
        for q in range(i+1, len(nums)):
            if q > len(nums)-q+i: break
            nums[q], nums[len(nums)-q+i] = nums[len(nums)-q+i], nums[q]