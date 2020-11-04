class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        st = list()
        start, end = len(nums), len(nums)
        for i, num in enumerate(nums):
            peak, left = num, i
            while st and st[-1][0] > num:
                n, p = st.pop()
                peak = max(n, peak)
                left = p
                start = min(start, left)
                end = i
            st.append((peak, left))
        return end-start+1



