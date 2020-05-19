//
// Created by chenyufan on 2020/5/19.
//

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

#include <vector>
#include <queue>

 struct TreeNode {
         int val;
         TreeNode *left;
         TreeNode *right;
         TreeNode() : val(0), left(nullptr), right(nullptr) {}
         TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
         TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
     };

using namespace std;

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<pair<TreeNode*, int>> q;
        q.push({root, 0});
        vector<vector<int>> ret;
        while (!q.empty()) {
            auto params = q.front();
            q.pop();
            auto cur = params.first;
            if (cur == nullptr) continue;

            int level = params.second;
            if (level >= ret.size()) ret.emplace_back();
            ret[level].push_back(cur->val);
            q.push({cur->left, level+1}); q.push({cur->right, level+1});
        }
        return ret;
    }
};

int main() {

}
