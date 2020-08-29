# 单调栈
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d, q = dict(), collections.deque()
        for i in range(len(nums2)):
            while len(q) and nums2[i] > nums2[q[-1]]:
                d[nums2[q.pop()]] = nums2[i]
            q.append(i)
        while len(q): d[nums2[q.pop()]] = -1
        return [d[num] for num in nums1]

