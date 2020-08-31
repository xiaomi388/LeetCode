# O(n^2)解法
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not len(nums): return 0

        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            dp[i] = max([dp[q]+1 for q in range(0, i) if nums[q] < nums[i]] + [1])
        return max(dp)

# 贪心 + 二分：顺序遍历，需要一个大于最前元素的元素，就二分替换掉
# LIS问题核心思路：后面遇到一个小的，就对原来的ret数组找上界并替换。这样的话ret数组保留了两个信息：1是原序列的长度信息，2是新序列都有哪些数字
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ret = []
        def upper_bound(i):
            lo, hi = 0, len(ret)
            while lo < hi:
                mid = (lo + hi) / 2
                if ret[mid] <= i:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        for num in nums:
            if not len(ret) or num > ret[-1]:
                ret.append(num)
            else:
                ret[upper_bound(num)] = num
        return ret

