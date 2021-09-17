# core window: all 1s, then extend the left boundary and right boundary

from collections import deque

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        st = deque()
        out = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                st.append(i)

            if len(st) == k:
                l, r = 0, 0
                for i in range(st[0]-1, -1, -1):
                    if nums[i] % 2 == 1:
                        break
                    l += 1
                for i in range(st[-1]+1, len(nums)):
                    if nums[i] % 2 == 1:
                        break
                    r += 1
                out += (l+1) * (r+1)
                st.popleft()
        return out






