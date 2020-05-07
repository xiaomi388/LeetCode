//
// Created by chenyufan on 2020/5/7.
//

#include <vector>
#include <map>
#include <iostream>

using namespace std;

class Solution {
public:
    int findMaximizedCapital(int k, int W, vector<int>& Profits, vector<int>& Capital) {
        map<int, map<int, int>> m;

        for (int i = 0; i < Capital.size(); ++i) {
            if (m.find(Capital[i]) == m.end()) m[Capital[i]] = map<int, int>();
            if (m[Capital[i]].find(Profits[i]) == m[Capital[i]].end()) m[Capital[i]][Profits[i]] = 0;
            m[Capital[i]][Profits[i]] += 1;
        }
        int total = W;
        for (int i = 0; i < k; ++i) {
            int maxProfit = 0;
            auto it = m.begin();
            decltype(it) maxCit = m.end();
            while (total >= it->first && it != m.end()) {
                auto pit = --(it->second.end());
                if (pit->first > maxProfit) {
                    maxProfit = pit->first;
                    maxCit = it;
                }
                it++;
            }
            total += maxProfit;
            if (maxCit != m.end()) {
                auto maxPit = --(maxCit->second.end());
                if (maxPit->second == 1) maxCit->second.erase(maxPit);
                else maxPit->second--;
                if (maxCit->second.empty()) m.erase(maxCit);
            } else {
                break;
            }
        }
        return total;
    }
};

int main() {
    Solution s;
    vector<int> Profits{1,2,3};
    vector<int> Capital{0,1,1};
    cout << s.findMaximizedCapital(2, 0, Profits, Capital) << endl;
}

