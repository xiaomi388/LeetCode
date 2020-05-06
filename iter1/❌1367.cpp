//
// Created by chenyufan on 2020/4/20.
//

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

#include <iostream>
#include <unordered_map>
#include <vector>


using namespace std;

struct ListNode {
         int val;
         ListNode *next;
         ListNode(int x) : val(x), next(NULL) {}
 };

struct TreeNode {
         int val;
         TreeNode *left;
         TreeNode *right;
         TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool isSubPath(ListNode* head, TreeNode* root) {
        if (!root) return false;
        return _isSubPath(head, root) || isSubPath(head, root->left) || isSubPath(head, root->right);
    }

    bool _isSubPath(ListNode* head, TreeNode* root) {
        if (!head) return true;
        if (!root) return false;
        if (head->val != root->val) return false;
        return _isSubPath(head->next, root->left) || _isSubPath(head->next, root->right);
    }
};

