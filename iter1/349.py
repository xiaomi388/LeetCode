class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(filter(lambda num : num in set(nums1), set(nums2)))

