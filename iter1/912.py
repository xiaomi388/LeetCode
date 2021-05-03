# quick sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(lo, hi):
            pivot = nums[lo]
            l, r = lo, hi
            while l < r:
                while l < r and nums[l] <= pivot: l += 1
                while l < r and nums[r] > pivot: r -= 1
                nums[l], nums[r] = nums[r], nums[l]
            nums[lo], nums[r] = nums[r], nums[lo]
            return r

        def sort(lo, hi):
            if lo > hi: return
            mid = partition(lo, hi)
            #print(nums)
            sort(lo, mid-1)
            sort(mid+1, hi)
        sort(0, len(nums)-1)
        return nums
