// 难点：新建一个新的头。

#include <iostream>

using namespace std;

 struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *head = new ListNode(0), *tail;
        tail = head;

        ListNode *left = l1, *right = l2;
        while (left != NULL && right != NULL) {
            if (left->val > right->val) {
                tail->next = right;
                right = right->next;
            } else {
                tail->next = left;
                left = left->next;
            }
            tail = tail->next;
        }

        if (left == NULL) {
            tail->next = right;
        } else {
            tail->next = left;
        }
        return head->next;
    }
};
