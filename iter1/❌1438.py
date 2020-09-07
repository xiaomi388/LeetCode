# treeset
# tips: treeset is suitable for storing the max/min elements in a range


import sortedcontainers
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        s = sortedcontainers.SortedDict()
        l, ret = 0, -1
        for i, num in enumerate(nums):
            s[num] = s.get(num, 0) + 1
            while s.keys()[-1] - s.keys()[0] > limit:
                s[nums[l]] -= 1
                if s[nums[l]] == 0:
                    del s[nums[l]]
                l = l + 1
            ret = max(ret, i-l+1)
        return ret

# slide windows (dequeue)
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        dq = collections.deque()
        aq = collections.deque()
        l, ret = 0, -1
        for r, num in enumerate(nums):
            while len(dq) and num > dq[-1]: dq.pop()
            while len(aq) and num < aq[-1]: aq.pop()
            dq.append(num)
            aq.append(num)
            while dq[0] - aq[0] > limit:
                if dq[0] == nums[l]: dq.popleft()
                if aq[0] == nums[l]: aq.popleft()
                l += 1
            ret = max(ret, r-l+1)
        return ret


