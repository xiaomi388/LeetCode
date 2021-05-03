# O(n), O(n)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnter1 = collections.Counter(nums1)
        cnter2 = collections.Counter(nums2)
        ans = []
        for num in cnter2:
            if num not in cnter1:
                continue
            ans += [num] * min(cnter2[num], cnter1[num])
        return ans

# What if the given array is already sorted? How would you optimize your algorithm?
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i, q = 0, 0
        ans = []
        while i < len(nums1) and q < len(nums2):
            if nums[i] == nums[q]:
                ans.append(nums[i])
                i += 1
                q += 1
            elif nums1[i] < nums[q]:
                i += 1
            else:
                q += 1
        return ans

