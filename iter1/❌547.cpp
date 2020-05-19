// 遍历每个点，如果从这个点出发，遍历完了也没有碰到其他已经走过的点（切这个"其他点"并不是此次遍历中已经走过的点"
// 那么则认为与别的块连通了，则此次遍历完之后，不能对计数+1. 否则遍历完之后，计数加一。
//

#include <vector>
#include <unordered_map>
#include <queue>
#include <unordered_set>
#include <iostream>

using namespace std;

class Solution {
public:
    int findCircleNum(vector<vector<int>>& M) {
        vector<int*> group(M.size(), nullptr);
        for (int i = 0; i < M.size(); ++i) {
            if (group[i] != nullptr) continue;
            queue<int> q;
            q.push(i);
            while (!q.empty()) {
                auto j = q.front();
                q.pop();
                if (group[j] == nullptr) {
                    if (group[i] == nullptr) group[i] = new int(i);
                    group[j] = group[i];
                    for (int u = 0; u < M[j].size(); ++u) {
                        if(M[j][u]) {
                            q.push(u);
                        }
                    }
                } else if (*group[j] == *group[i]) {
                    continue;
                } else {
                    *group[j] = *group[i];
                }
            }
        }
        unordered_set<int> count;
        for (auto p : group) { count.insert(*p); }
        return count.size();
    }

};

int main() {
    Solution s;
    vector<vector<int>> fs{
            {1,1,0},
            {1,1,0},
            {0,0,1},
    };
    cout << s.findCircleNum(fs) << endl;

}
