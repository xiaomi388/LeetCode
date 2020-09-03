class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = [-1]*len(nums1)
        d = {k: v for v, k in enumerate(nums1)}
        q = collections.deque()
        for num in nums2:
            while len(q) and num > q[-1] and q[-1] in d: ret[d[q.pop()]] = num
            q.append(num)
        return ret




