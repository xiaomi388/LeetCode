// 对每个字母进行26次遍历。
// 这题有所疑问，为什么遍历list里所有单词就超时，要是一个单词很长，list很短不就凉了？

#include <iostream>
#include <string>
#include <queue>
#include <unordered_map>
#include <cmath>

using namespace std;

struct Param {
    int depth;
    string curWord;
};

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_map<string, bool> dict;
        for (auto &s : wordList) {
            dict[s] = true;
        }

        queue<Param> q;
        q.push(Param{0, beginWord});
        while (!q.empty()) {
            auto param = q.front();
            q.pop();
            if (param.curWord == endWord) return param.depth + 1;
            for (int i = 0; i < param.curWord.length(); ++i) {
                for (int j = 0; j < 26; ++j) {
                    string nextWord = param.curWord;
                    nextWord[i] = 'a' + j;
                    auto it = dict.find(nextWord);
                    if (it != dict.end()) {
                        q.push(Param{param.depth+1, nextWord});
                        dict.erase(it);
                    }
                }
            }
        }
        return 0;
    }
};

int main() {
    Solution s;
    vector<string> wordList{"hot","dot","dog","lot","log","cog"};
    cout << s.ladderLength("hit", "cog", wordList) << endl;

}