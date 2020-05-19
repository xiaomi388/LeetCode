//
// Created by chenyufan on 2020/5/8.
//

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */


#include <vector>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

using namespace std;

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ret;
        _rightSideView(root, ret, 0);
        return ret;
    }

    void _rightSideView(TreeNode* root, vector<int>& pre, int curLevel) {
        if (!root) return;
        if (curLevel == pre.size()) pre.push_back(root->val);
        _rightSideView(root->right, pre, curLevel+1);
        _rightSideView(root->left, pre, curLevel+1);
    }

};

int main() {
    Solution s;
}
