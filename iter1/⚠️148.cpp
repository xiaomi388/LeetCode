// 做了好久...
// 主要遇到的坑点是：
// 1. 重新排序后，首位元素 != 原本的首位元素
// 2. 做递归时，先把中间链子解开，不然会出现奇怪问题


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

#include <iostream>
#include <vector>

using  namespace std;

struct ListNode {
         int val;
         ListNode *next;
         ListNode() : val(0), next(nullptr) {}
         ListNode(int x) : val(x), next(nullptr) {}
         ListNode(int x, ListNode *next) : val(x), next(next) {}
     };

class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if (head == nullptr) return head;
        if (head->next == nullptr) return head;

        ListNode *fast = head->next, *slow = head;

        while (fast != nullptr && fast->next != nullptr) {
            fast = fast->next->next;
            slow = slow->next;
        }
        auto rhead = sortList(slow->next);
        slow->next = nullptr;
        auto lhead = sortList(head);


        auto root = ListNode();
        ListNode *tail = &root;
        ListNode *l = lhead, *r = rhead;
        while (l != nullptr && r != nullptr) {
            ListNode **p = l->val < r->val ? &l : &r;
            tail->next = *p;
            *p = (*p)->next;
            tail = tail->next;
        }
        ListNode **p = l == nullptr ? &r : &l;
        while (*p != nullptr) {
            tail->next = *p; *p = (*p)->next; tail = tail->next;
        }
        tail->next = nullptr;
        return root.next;
    }
};

int main() {
    auto head = new ListNode(2);
    ListNode *cur = head;
    for (int v : {1}) {
        cur->next = new ListNode(v);
        cur = cur->next;
    }
    Solution s;
    s.sortList(head);
}