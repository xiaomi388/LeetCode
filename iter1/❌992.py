# 滑动窗口（双指针）思想：把问题转化成：求解固定右边界的子问题。而且对于某个固定右边界，该子问题只有唯一的左边界

import collections

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(k):
            left, right = 0, -1
            cnter = collections.defaultdict(int)

            res = 0
            while right < len(nums)-1:
                right += 1
                cnter[nums[right]] += 1
                while len(cnter) > k:
                    cnter[nums[left]] -= 1
                    if cnter[nums[left]] == 0:
                        del cnter[nums[left]]
                    left += 1
                res += right - left
            return res

        return atMostK(k) - atMostK(k-1)





