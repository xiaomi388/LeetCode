//
// Created by chenyufan on 2020/5/29.
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

#include <iostream>

using namespace std;

 struct TreeNode {
         int val;
         TreeNode *left;
         TreeNode *right;
         TreeNode() : val(0), left(nullptr), right(nullptr) {}
         TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
         TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
     };

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return _isValidBST(root, LONG_MIN, LONG_MAX);
    }

    bool _isValidBST(TreeNode *root, long long _min, long long _max) {
        if (!root) return true;
        if (root->val >= _max || root->val <= _min) return false;
        return _isValidBST(root->left, _min, root->val) && _isValidBST(root->right, root->val, _max);
    }
};

int main() {

}

