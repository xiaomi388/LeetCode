// 快慢指针：先跑到meeting point，然后从meeting point到交点距离 = 从起点到交点距离 + 1

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

#include <iostream>

using namespace std;

struct ListNode {
         int val;
         ListNode *next;
         ListNode(int x) : val(x), next(NULL) {}
     };

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode *fast = head->next, *slow = head;
        while (fast && fast->next && fast != slow) {
            fast = fast->next->next;
            slow = slow->next;
        }
        if (!fast) return NULL;
        ListNode *tmp = head;
        slow = slow->next;
        while (tmp != slow) {
            slow = slow->next;
            tmp = tmp->next;
        }
        return tmp;
    }
};



int main() {

}

