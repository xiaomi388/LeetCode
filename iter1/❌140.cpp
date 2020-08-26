//
// Created by 陈语梵 on 2020/8/22.
//

class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        vector<string> ret;
        string ans;
        unordered_set<string> dict;
        for (auto &word : wordDict) dict.insert(word);
        dfs(ans, s, 0, ret, dict);
        return ret;
    }

    void dfs(string &ans, string &s, int i, vector<string>& ret, unordered_set<string> &dict) {
        if (i == s.length()) {
            ret.push_back(ans);
            return ;
        }

        for (int q = i+1; q <= s.length(); ++q) {
            string nexts = s.substr(i, q-i);
            if (dict.find(nexts) != dict.end()) {
                ans += " " + nexts;
                dfs(ans, s, q, ret, dict);
                ans.erase(ans.end() - nexts.length() - 1);
            }
        }
    }
};

