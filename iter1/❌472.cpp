// 1. dp：参考word break：遍历每个单词，跑一遍dp。
// 2.


class Solution {
public:
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        unordered_set<string> s(words.begin(), words.end());
        vector<string> res;
        for (auto w : words) {
            if (w.empty()) continue;
            int n = w.size();
            vector<int> dp(n+1);
            dp[0] = 1;
            for (int i = 1; i <= n; ++i) {
                for (int j = i - 1; j >= 0; --j) {
                    if (dp[j] == 0) continue;
                    if (i-j < n && s.count(w.substr(j, i-j))) {
                        dp[i] = 1;
                        break;
                    }
                }
            }
            if (dp[n]) {
                res.push_back(w);
            }
        }
        return res;
    }
};
