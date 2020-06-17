// 更简单的做法：遍历所有字母，假设该字母是回文中心，看有多少个是符合的。
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int countSubstrings(string s) {
        vector<vector<int>> dp(s.length());
        for (int i = 0; i < s.size(); ++i) {
            dp[i].push_back(i);
        }

        for (int i = 1; i < s.size(); ++i) {
            if (s[i] == s[i-1]) dp[i].push_back(i-1);
            for (auto start : dp[i-1]) {
                if (start-1 >= 0 && s[i] == s[start-1]) dp[i].push_back(start-1);
            }
        }

        int ret = 0;
        for (int i = 0; i < dp.size(); ++i) {
            ret += dp[i].size();
        }
        return ret;
    }
};

int main() {
    Solution s;
    cout << s.countSubstrings("abccba") << endl;
}

