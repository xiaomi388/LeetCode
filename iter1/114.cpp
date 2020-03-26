// 难点：1. 递归的思想，先把两个子树搞成链表。
// 2. 而后要记录两个子树的最后一个元素。
// 3. 注意考虑的特殊情况：有两个子树，只有左/右子树，没有子节点。其中只有右子树和有两个子树的返回是一致的。

#include <iostream>

using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

 struct TreeNode {
         int val;
         TreeNode *left;
         TreeNode *right;
         TreeNode(int x) : val(x), left(NULL), right(NULL) {}
     };

class Solution {
public:

    TreeNode* flattenAndGetLast(TreeNode* root) {
        if (root == NULL) return NULL;
        auto leftLast = flattenAndGetLast(root->left);
        auto rightLast = flattenAndGetLast(root->right);
        if (leftLast != NULL) {
            leftLast->right = root->right;
            root->right = root->left;
            root->left = NULL;
        }
        if (rightLast) return rightLast;
        else if(leftLast) return leftLast;
        else return root;
    }


    void flatten(TreeNode* root) {
        flattenAndGetLast(root);
    }
};

int main() {
    auto root = TreeNode(1);
    root.left = new TreeNode(2);
    root.right = new TreeNode(3);
    Solution s;
    s.flatten(&root);
}

