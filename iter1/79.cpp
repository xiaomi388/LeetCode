// 回溯的要点：遍历完退出后，记得把visited状态置为false


#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        if (word.empty()) return true;
        if (board.empty()) return false;
        for (int i = 0; i < board.size(); ++i) {
            for (int q = 0; q < board[0].size(); ++q) {
                vector<vector<bool>> visited(board.size(), vector<bool>(board[0].size()));
                if (dfs(board, word, 0, i, q, visited)) {
                    return true;
                }
            }
        }
        return false;
    }

    bool dfs(vector<vector<char>>& board, string& word, int i, int x, int y, vector<vector<bool>>& visited) {
        if (i >= word.length()) return true;
        if (x >= board.size() || x < 0 || y >= board[0].size() || y < 0) return false;
        if (board[x][y] != word[i]) return false;
        if (visited[x][y]) return false;

        visited[x][y] = true;
        bool res = dfs(board, word, i+1, x+1, y, visited) ||
                dfs(board, word, i+1, x-1, y, visited) ||
                dfs(board, word, i+1, x, y+1, visited) ||
                dfs(board, word, i+1, x, y-1, visited);

        visited[x][y] = false;
        return res;
    }
};

int main() {

}

