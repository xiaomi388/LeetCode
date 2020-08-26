class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        q = n - 1
        p = m + n - 1
        while i >= 0 and q >= 0:
            if nums1[i] > nums2[q]:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[q]
                q -= 1
            p -= 1
        while q >= 0:
            nums1[p] = nums2[q]
            q -= 1
            p -= 1
