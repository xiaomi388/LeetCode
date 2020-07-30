//
// Created by 陈语梵 on 2020/7/30.
//

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        unordered_set<string> prefix; unordered_set<string> wordSet;
        // build dict
        for (auto &word : words) {
            wordSet.insert(word);
            for (int i = 0; i < word.length(); ++i) {
                prefix.insert(word.substr(0, i+1));
            }
        }
        string w; unordered_set<string> ret;
        vector<vector<int>> visited(board.size(), vector<int>(board[0].size()));
        for (int i = 0; i < board.size(); ++i) {
            for (int q = 0; q < board[0].size(); ++q) {
                dfs(board, i, q, prefix, wordSet, w, ret, visited);
            }
        }
        return vector<string>(ret.begin(), ret.end());
    }

    void dfs(vector<vector<char>>& board, int r, int c, const unordered_set<string>& prefix,
            const unordered_set<string>& wordSet, string &word, unordered_set<string>& ret,
            vector<vector<int>>& visited) {
        if (r >= board.size() || r < 0 || c >= board[0].size() || c < 0) return ;
        if (visited[r][c]) return ;
        visited[r][c] = 1;

        word.push_back(board[r][c]);
        if (prefix.find(word) == prefix.end()) {
            goto end;
        }
        if (wordSet.find(word) != wordSet.end()) {
            ret.insert(word);
        }

        dfs(board, r+1, c, prefix, wordSet, word, ret, visited);
        dfs(board, r-1, c, prefix, wordSet, word, ret, visited);
        dfs(board, r, c+1, prefix, wordSet, word, ret, visited);
        dfs(board, r, c-1, prefix, wordSet, word, ret, visited);
    end:
        word.pop_back();
        visited[r][c] = 0;
        return ;
    }
};

// 更好的办法：使用trie进行前序搜索


struct TrieNode {
    char val;
    unordered_map<char, TrieNode*> children;
    bool isComplete;
    TrieNode(char v) : isComplete(false), val(v) {}
};


class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        auto trie = buildTrie(words);
        vector<vector<bool>> visited(board.size(), vector<bool>(board[0].size()));
        unordered_set<string> ret;
        string w;

        for (int i = 0; i < board.size(); ++i) {
            for (int q = 0; q < board[0].size(); ++q) {
                dfs(trie, w, board, i, q, visited, ret);
            }
        }
        return vector<string>(ret.begin(), ret.end());
    }

    TrieNode* buildTrie(const vector<string>& words) {
        auto root = new TrieNode(0);
        for (auto &word :words) {
            buildTrieForWord(word, 0, root);
        }
        return root;
    }

    void buildTrieForWord(const string& word, int i, TrieNode* parent) {
        if (parent->children.find(word[i]) == parent->children.end()) {
            parent->children[word[i]] = new TrieNode(word[i]);
        }
        if (i == word.length() - 1) {
            parent->children[word[i]]->isComplete = true;

        } else {
            buildTrieForWord(word, i+1, parent->children[word[i]]);
        }
    }

    void dfs(TrieNode* curNode, string &word, const vector<vector<char>>& board,
             int r, int c, vector<vector<bool>>& visited, unordered_set<string>& ret) {
        if (r >= board.size() || r < 0 || c >= board[0].size() || c < 0) return ;
        if (visited[r][c]) return ;
        if (curNode->children.find(board[r][c]) == curNode->children.end()) return ;

        visited[r][c] = true;
        word.push_back(board[r][c]);
        curNode = curNode->children[board[r][c]];
        if (curNode->isComplete) ret.insert(word);

        dfs(curNode, word, board, r+1, c, visited, ret);
        dfs(curNode, word, board, r-1, c, visited, ret);
        dfs(curNode, word, board, r, c+1, visited, ret);
        dfs(curNode, word, board, r, c-1, visited, ret);

        end:
        word.pop_back();
        visited[r][c] = false;
    }
};

