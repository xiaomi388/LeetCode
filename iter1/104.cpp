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
    int _max = 0;
public:
    int maxDepth(TreeNode* root) {
        _maxDepth(root, 0);
        return _max;
    }

    void _maxDepth(TreeNode* root, int dep) {
        if (!root) {
            _max = max(_max, dep);
            return ;
        }
        _maxDepth(root->left, dep+1);
        _maxDepth(root->right, dep+1);
    }
};

