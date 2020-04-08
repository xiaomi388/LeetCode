// 正解要用到trie树，感觉面试不会出这么难的题吧？
//

#include <vector>
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        vector<string> ret;
        for (auto &word : words) {
            if (findWord(board, word)) ret.push_back(word);
        }
        return ret;
    }

    bool findWord(vector<vector<char>>& board, string& word) {
        vector<vector<bool>> state(board.size(), vector<bool>(board[0].size()));
        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[0].size(); ++j) {
                if (findWord(board, word, state, i, j)) return true;
            }
        }
        return false;
    }

    bool findWord(vector<vector<char>>& board, string word, vector<vector<bool>> state, int r, int c) {
        if (word.empty()) return true;
        if (r >= board.size() || c >= board[0].size() || r < 0 || c < 0) return false;
        if (state[r][c]) return false;
        if (board[r][c] != word[0]) return false;

        setState(state, r, c, true);
        for (int i = -1; i <= 1; ++i) {
            for (int j = -1; j <= 1; ++j) {
                if ((i != 0 && j != 0) || (i == 0 && j == 0)) continue;
                if (findWord(board, word.substr(1), state, r+i, c+j)) return true;
            }
        }
        return false;
    }

    void setState(vector<vector<bool>>& state, int r, int c, bool flag) {
        if (r >= state.size() || c >= state[0].size() || r < 0 || c < 0) return;
        state[r][c] = flag;
    }
};


int main() {
    Solution s;
    vector<vector<char>> board = {
        {'o', 'a', 'a', 'n'},
        {'e', 't', 'a', 'e'},
        {'i', 'h', 'k', 'r'},
        {'i', 'f', 'l', 'v'},
    };
    vector<string> words = {"oath","pea","eat","rain"};

    auto res = s.findWords(board, words);
    for (auto &ss : res) cout << ss << endl;
}