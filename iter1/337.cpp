//
// Created by chenyufan on 2020/6/1.
//

#include <iostream>
#include <vector>

using namespace std;

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
#include <map>

 struct TreeNode {
         int val;
         TreeNode *left;
         TreeNode *right;
         TreeNode() : val(0), left(nullptr), right(nullptr) {}
         TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
         TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
     };


class Solution {
    map<pair<TreeNode*, bool>, int> memo;

public:
    int rob(TreeNode* root) {
        return max(_rob(root, true), _rob(root, false));
    }

    int _rob(TreeNode* root, bool steal) {
        if (!root) return 0;
        if (memo.find({root, steal}) != memo.end()) {
            return memo[{root, steal}];
        }

        int val = steal ? root->val : 0;
        if (!steal) {
            val += rob(root->right);
            val += rob(root->left);
        } else {
            val += _rob(root->left, false);
            val += _rob(root->right, false);
        }
        memo[{root, steal}] = val;
        return val;
    }
};

int main() {

}
