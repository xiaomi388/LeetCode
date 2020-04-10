// 做法跟简单版的其实一样，但是现在的解法有个缺陷
// 每次循环后，都要重新比一遍所有的值找到最小那一个
// 更好的做法是使用一个数据结构（优先级队列），来快速找到最小那一个。

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        vector<ListNode*> heads = lists;
        vector<bool> isEnd(lists.size());
        auto *root = new ListNode(0);
        ListNode *tail = root;

        int cnt = lists.size();
        while (cnt > 1) {
            int minNum = INT_MAX;
            ListNode* minNode = NULL;
            int minRow = -1;
            for (int i = 0; i < heads.size(); ++i) {
                auto &head = heads[i];
                if (!head) {
                    if (!isEnd[i]) {
                        cnt--;
                        isEnd[i] = true;
                    }
                    continue;
                }
                if (head->val <= minNum) {
                    minNum = head->val;
                    minNode = head;
                    minRow = i;
                }
            }
            if (minNode) {
                heads[minRow] = minNode->next;
            }
            tail->next = minNode;
            tail = tail->next;
        }
        for (auto &head : heads) {
            if (head) {
                tail->next = head;
                break;
            }
        }
        return root->next;
    }
};

int main() {

}
