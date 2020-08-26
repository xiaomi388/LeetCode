//
// Created by 陈语梵 on 2020/8/21.
//

class Solution {
public:
    int connectSticks(vector<int>& sticks) {
        priority_queue<int, vector<int>, less<int>> heapq(sticks.begin(), sticks.end());
        int cost = 0;
        while (heapq.empty()) {
            int x = heapq.top(); heapq.pop();
            if (heapq.empty()) return cost;
            int y = heapq.top(); heapq.pop();
            cost += (x + y);
        }
        return cost;
    }
};

