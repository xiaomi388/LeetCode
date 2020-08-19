// 使用dp来记录每个时刻的三种不同选择（状态）所能获取到的最大利润
//


class Solution {
    unordered_map<int, int> memo;
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty()) return 0;
        vector<vector<int>> dp(prices.size(), vector<int>(3));
        // 0: owning
        // 1: sold
        // 2: not owning
        dp[0][0] = -prices[0];
        dp[0][1] = 0;
        dp[0][2] = 0;
        for (int i = 1; i < prices.size(); ++i) {
            dp[i][0] = max(dp[i-1][0], dp[i-1][2]-prices[i]);
            dp[i][1] = dp[i-1][0]+prices[i];
            dp[i][2] = max(dp[i-1][1], dp[i-1][2]);
        }
        return *max_element(dp.back().begin(), dp.back().end());
    }

};
