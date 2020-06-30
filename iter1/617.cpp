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
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if (!t1 && !t2) return nullptr;
        TreeNode* cur = new TreeNode();
        if (t1) cur->val += t1->val;
        if (t2) cur->val += t2->val;
        cur->left = mergeTrees(t1 ? t1->left : nullptr, t2 ? t2->left : nullptr);
        cur->right = mergeTrees(t1 ? t1->right : nullptr, t2 ? t2->right : nullptr);
        return cur;
    }
};
