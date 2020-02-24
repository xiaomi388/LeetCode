// 总结：bfs，难点：
// 1. 找出当前状态的状态转移: 遍历每个字母
// 2. 熟练写出bfs

#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cstdlib>
#include <queue>
#include <unordered_set>

using namespace std;

class Solution {
public:
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        vector<vector<string>> ans;

        // set for quick lookup
        unordered_set<string> dict(wordList.begin(), wordList.end());

        // case when endWord is not present in dict
        if (dict.find(endWord) == dict.end()) {
            return ans;
        }

        queue<vector<string>> q;
        int level = 0;
        q.push({beginWord});

        while (!q.empty() && level < 1000) {
            int s = q.size();
            vector<string> newWords;

            while (s--) {
                vector<string> path = q.front();
                q.pop();
                handleCurPath(path, beginWord, endWord, q, ans, dict, newWords);
            }

            for (string w : newWords) {
                dict.erase(w);
            }
            level++;
        }
        return ans;
    }

    void handleCurPath(
            vector<string> path, string beginWord, string endWord, queue<vector<string>> &q,
            vector<vector<string>> &ans, unordered_set<string> &dict, vector<string> &newWords) {
        string word = path.back();
        if (word == endWord) {
            ans.push_back(path);
            return;
        }

        for (int i = 0; i < word.length(); ++i) {
            char c = word[i];
            for (int j = 0; j < 26; ++j) {
                word[i] = j + 'a';
                if (dict.find(word) != dict.end()) {
                    // create a new path from older path if we get new word exist in dict
                    vector<string> newPath(path.begin(), path.end());
                    newPath.push_back(word);
                    newWords.push_back(word);
                    q.push(newPath);
                }
            }
            word[i] = c;
        }

    }
};

int main() {
    auto s = Solution();
    vector<string> list =  {"hot","dot","dog","lot","log","cog"};
    auto ans = s.findLadders("hit", "cog", list);
    for (auto subans : ans) {
        for (auto word : subans) {
            cout << word << " ";
        }
        cout << endl;
    }
}


