//
// Created by chenyufan on 2020/5/20.
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

struct TreeNode {
         int val;
         TreeNode *left;
         TreeNode *right;
         TreeNode() : val(0), left(nullptr), right(nullptr) {}
         TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
         TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
     };

class Solution {
    int sum = 0;

public:
    TreeNode* convertBST(TreeNode* root) {
        _convertBST(root);
        return root;
    }

    void _convertBST(TreeNode* root) {
        if (root == nullptr) return ;
        _convertBST(root->right);
        root->val += sum;
        sum = root->val;
        _convertBST(root->left);
    }
};
