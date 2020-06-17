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

#include <vector>

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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return _buildTree(preorder, 0, preorder.size(), inorder, 0, inorder.size());
    }

    TreeNode* _buildTree(vector<int>& preorder, int pstart, int pend, vector<int>& inorder, int istart, int iend) {
        if (pstart >= pend || istart >= iend) return nullptr;

        auto root = new TreeNode(preorder[pstart]);
        int m = istart;
        for (; m < iend && inorder[m] != root->val; ++m);
        m = m - istart;
        root->left = _buildTree(preorder, pstart+1, m+pstart+1, inorder, istart, istart+m);
        root->right = _buildTree(preorder, pstart+m+1, pend, inorder, istart+m+1, iend);
        return root;
    }
};

