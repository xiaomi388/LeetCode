// 多状态dp：dp[i][0]代表当第i位本身作为一个划分时的组合数；dp[i][1]代表第i位和第i-1位作为一个划分时的组合数

class Solution {
    bool isValidNum(string &s, int i) {
        if (s[i] <= '0' || s[i] >= '3') return false;
        if (s[i] == '2' && s[i+1] > '6') return false;
        return true;
    }

public:
    int numDecodings(string s) {
        if (s.empty()) return 0;
        if (s.length() == 1) return s[0] == '0' ? 0 : 1;
        vector<vector<int>> dp(s.length(), vector<int>(2));
        dp[0][0] = s[0] == '0' ? 0 : 1;
        dp[1][0] = s[1] == '0' ? 0 : dp[0][0] + dp[0][1];
        dp[1][1] = isValidNum(s, 0) ? 1 : 0;

        for (int i = 2; i < s.length(); ++i) {
            dp[i][0] = s[i] == '0' ? 0 : dp[i-1][0] + dp[i-1][1];
            dp[i][1] = isValidNum(s, i-1) ? dp[i-2][0] + dp[i-2][1] : 0;
        }
        return dp[s.length()-1][0] + dp[s.length()-1][1];
    }
};

