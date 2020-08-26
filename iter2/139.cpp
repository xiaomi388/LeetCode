//
// Created by 陈语梵 on 2020/8/23.
//

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        vector<int> dp(s.length());
        dp[0] = dict.count(s.substr(0,1)) ? 0 : -1;
        for (int i = 1; i < s.length(); ++i) {
            if (dict.count(s.substr(0, i+1))) dp[i] = i;
            else if (dp[i-1] != -1)
            else dp[i] = dp[i-1];
        }




    }
};
