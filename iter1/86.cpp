// 思路：其实是要求两段。所以我们新开两个哨兵节点，遍历所有点，然后串起来就好了。
//

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

#include <vector>
#include <iostream>

using namespace std;

struct ListNode {
         int val;
         ListNode *next;
         ListNode() : val(0), next(nullptr) {}
         ListNode(int x) : val(x), next(nullptr) {}
         ListNode(int x, ListNode *next) : val(x), next(next) {}
     };

class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        auto leftBegin = new ListNode(0);
        ListNode* leftEnd = leftBegin;

        auto rightBegin = new ListNode(0);
        ListNode* rightEnd = rightBegin;

        ListNode* p = head;
        while (p != nullptr) {
            if (p->val < x) {
                leftEnd->next = p;
                leftEnd = leftEnd->next;
                p = p->next;
            } else {
                rightEnd->next = p;
                rightEnd = rightEnd->next;
                p = p->next;
            }
        }
        leftEnd->next = rightBegin->next;
        rightEnd->next = nullptr;
        return leftBegin->next;
    }
};

int main() {
    Solution s;
    ListNode *head = new ListNode(1);
    ListNode *cur = head;

    for (auto i : vector<int>{4,3,2,5,2}) {
        cur->next = new ListNode(i);
        cur = cur->next;
    }
    s.partition(head, 3);

    for (cur = head; cur != nullptr; cur = cur->next) {
        cout << cur->val << " ";
    }
    cout << endl;

}
