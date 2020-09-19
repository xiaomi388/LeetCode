# 滑动窗口
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, ans = 0, 0
        d = collections.defaultdict(int)
        for r in range(1, len(nums)+1):
            d[nums[r-1]] += 1
            while d[0] > 1:
                if nums[l] == 0:
                    d[0] -= 1
                l += 1
            ans = max(r-l, ans)
        return ans

# DP
# dp[i] = (到i的子串最长长度，上一个0的位置）
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        dp = [0] * len(nums)
        dp[0] = (1, -1 if nums[0] else 0)
        for i in range(1, len(nums)):
            if nums[i] == 0:
                dp[i] = (dp[i-1][0]+1, i) if dp[i-1][1] == -1 else (i-dp[i-1][1], i)
            elif nums[i] == 1:
                dp[i] = (dp[i-1][0]+1, dp[i-1][1])
        return max(dp, key=lambda x : x[0])[0]

# 内存优化dp
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        cur = (1, -1 if nums[0] else 0)
        ans = cur[0]
        for i in range(1, len(nums)):
            if nums[i] == 0:
                cur = (cur[0]+1, i) if cur[1] == -1 else (i-cur[1], i)
            elif nums[i] == 1:
                cur = (cur[0]+1, cur[1])
            ans = max(ans, cur[0])
        return ans


