class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0: not own; 1: own
        dp = [[0, 0]] * len(prices)
        dp[0][0] = 0; dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][1] + prices[i], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0]-prices[i], dp[i-1][1])
        return max(*dp[len(prices-1)])

