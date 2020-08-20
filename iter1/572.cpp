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
    bool isSubtree(TreeNode* s, TreeNode* t) {
        if (t == nullptr) return true;
        if (s == nullptr) return false;

        bool ret = _isSubtree(s, t);
        if (!ret) ret = isSubtree(s->left, t) || isSubtree(s->right, t);
        return ret;
    }

    bool _isSubtree(TreeNode* s, TreeNode *t) {
        if (s == nullptr && t == nullptr) return true;
        if (s == nullptr || t == nullptr) return false;
        if (s->val != t->val) return false;
        return _isSubtree(s->left, t->left) && _isSubtree(s->right, t->right);
    }
};