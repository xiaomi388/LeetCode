# Approach 2: Binary Search
# Intuition
# It makes sense to try and convert the linear search into a binary search.
# In order to use binary search, we need to be able to look at the middle
# item and then determine whether the solution is the middle item, or to the
# left, or to the right.
#
# The key observation is that the starting array must always have an odd number
# of elements, because it has one element appearing once, and all the other
# elements appearing twice.
#
# Here is what happens when we remove a pair from the center. We are left with
# a left subarray and a right subarray.
# Like the original array, the subarray containing the single element must be
# odd-lengthed. The subarray not containing it must be even-lengthed.
# So by taking a pair out of the middle and then calculating which side
# is not odd-lengthed, we have the information needed for binary search


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def search(begin, end):
            if begin >= end: return -1
            mid = (begin + end) // 2
            if mid == 0 or mid == len(nums)-1 or nums[mid] not in (nums[mid-1], nums[mid+1]):
                return nums[mid]
            elif nums[mid] == nums[mid-1]:
                if (mid - begin + 1) % 2 == 0:
                    return search(mid+1, end)
                else:
                    return search(begin, mid+1)
            else:
                if (end - mid) % 2 == 0:
                    return search(begin, mid)
                else:
                    return search(mid, end)
        return search(0, len(nums))


