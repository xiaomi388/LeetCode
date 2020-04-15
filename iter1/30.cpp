// 两个循环。外循环对每一位开始寻找，内循环从这一位开始找串匹配。
// 优化点：1. 外循环到总长度-目标串长度即可停止循环
// 2. 避免拷贝map，拷贝map是很耗时的操作。

#include <vector>
#include <string>
#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        if (words.empty() || s.empty()) return {};
        unordered_map<string, int> dict;
        for (auto &w : words) {
            if (dict.find(w) == dict.end()) dict[w] = 1;
            else dict[w]++;
        }

        int wordLen = words[0].length();
        int wordNum = words.size();
        int sLen = s.length();
        vector<int> ret;

        for (int head = 0; head <= sLen - wordNum*wordLen; ++head) {
            bool res = startFindSequence(dict, s, head, wordLen, wordNum);
            if (res) ret.push_back(head);
        }
        return ret;
    }

    bool startFindSequence(unordered_map<string, int> &dict, string &s, int curPos, int wordLen, int wordNum) {
        unordered_map<string, int> seen;
        int sLen = s.length();
        for (int i = curPos; i < curPos + wordNum*wordLen; i += wordLen) {
            string word = s.substr(i, wordLen);
            auto it = dict.find(word);
            if (it == dict.end()) return false;
            else {
                seen[it->first]++;
                if (seen[it->first] > it->second) return false;
            }
        }
        return true;
    }
};

int main() {
    Solution s;
    vector<string> w{"foo", "bar"};
    auto res = s.findSubstring("barfoothefoobarman", w);
    for (auto i : res) cout <<  i << " ";
    cout << endl;
}
