//
// Created by 陈语梵 on 2020/7/29.
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
class Solution {
    unordered_map<TreeNode*, int> memo;
    int _max = INT_MIN;
public:
    int maxPathSum(TreeNode* root) {
        _maxPathSum(root);
        return _max;
    }

    void _maxPathSum(TreeNode* root) {
        if (!root) return ;
        _max = max(max(getHeight(root->left), 0) + max(getHeight(root->right), 0) + root->val, _max);
        _maxPathSum(root->left);
        _maxPathSum(root->right);
    }

    int getHeight(TreeNode* root) {
        if (!root) return 0;
        if (memo.find(root) != memo.end()) return memo[root];
        int ret = max(max(getHeight(root->left), getHeight(root->right)), 0) + root->val;
        memo[root] = ret;
        return ret;
    }
};
