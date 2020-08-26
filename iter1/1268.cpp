//
//


struct TrieNode {
    bool isWord;
    char c;
    TrieNode* children[26];
};

class Solution {
    void buildTrie(TrieNode* root, string &word) {
        TrieNode* cur = root;
        for (auto c : word) {
            if (!cur->children[c-'a']) {
                auto node = new TrieNode();
                node->c = c;
                cur->children[c-'a'] = node;
            }
            cur = cur->children[c-'a'];
        }
        cur->isWord = true;
    }

    void dfs(TrieNode* root, vector<string>& ret, string& ans) {
        if (!root || ret.size() == 3) return ;
        ans += root->c;
        if (root->isWord) ret.push_back(ans);
        for (int i = 0; i < 26; ++i) dfs(root->children[i], ret, ans);
        ans.pop_back();
    }

public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        TrieNode* root = new TrieNode();
        for (auto &product : products) {
            buildTrie(root, product);
        }

        TrieNode* cur = root;
        vector<vector<string>> ret;
        string prefix = "";
        for (auto c : searchWord) {
            if (!cur) {
                ret.push_back({});
                continue;
            };
            cur = cur->children[c-'a'];
            vector<string> res; string ans = prefix;
            dfs(cur, res, ans);
            ret.push_back(res);
            prefix += c;
        }
        return ret;
    }
};

