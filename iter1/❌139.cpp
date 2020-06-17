// dp，i代表第子串[0,i)能否由字典中的词组成。
// 起始：子串[0, 0)返回真
// 转移方程: dp[i] = dp[i-k] && (substr(i-k, i) in dict) for k in 1...i

#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> m(wordDict.begin(), wordDict.end());
        vector<bool> dp(s.length()+1, false);
        dp[0] = true;
        for (int i = 1; i <= s.length(); ++i) {
            for (int j = i - 1; j >= 0; --j) {
                if (dp[j]) {
                    string w = s.substr(j, i-j);
                    if (m.find(w) != m.end()) {
                        dp[i] = true;
                        break;
                    }
                }
            }
        }
        return dp[s.size()];
    }
};

int main() {

}