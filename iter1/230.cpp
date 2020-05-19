//
// Created by chenyufan on 2020/5/19.
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
#include <vector>
#include <queue>

struct TreeNode {
         int val;
         TreeNode *left;
         TreeNode *right;
         TreeNode() : val(0), left(nullptr), right(nullptr) {}
         TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
         TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
     };

using namespace std;

class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        return _kthSmallest(root, k).first;

    }

    pair<int, int> _kthSmallest(TreeNode* root, int k) {
        if (root == nullptr) return {INT_MIN, 0};
        auto res = _kthSmallest(root->left, k);
        int found = res.first, leftCnt = res.second;
        if (found) return {found, 0};

        if (k == leftCnt) return {root->val, 0};

        res = _kthSmallest(root->right, k - leftCnt - 1);
        found = res.first;
        int rightCnt = res.second;

        if (found) return {found, 0};
        return {INT_MIN, leftCnt+rightCnt+1};
    }
};


int main() {
    TreeNode *root;
    root = new TreeNode(3);
    vector<int> a{1,4,0,2};
    queue<TreeNode*> q;
    q.push(root);
    int i = 0;
    while (i < a.size()) {
        auto cur = q.front();
        cur->val = a[i];

        q.push(cur->left);
        q.push(cur->right);

        q.pop();
        cur = new TreeNode(a[i]);
    }
    Solution s;
    s.kthSmallest(root, 1);
}

