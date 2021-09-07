from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        st = deque()
        maxs = []
        for i in range(k):
            while len(st) > 0 and nums[i] >= nums[st[-1]]:
                st.pop()
            st.append(i)
        maxs.append(nums[st[0]])
        for i in range(k, len(nums)):
            while len(st) > 0 and nums[i] >= nums[st[-1]]:
                st.pop()
            while len(st) > 0 and (i - st[0]) >= k:
                st.popleft()
            st.append(i)
            maxs.append(nums[st[0]])
        return maxs



