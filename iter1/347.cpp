//
// Created by chenyufan on 2020/6/4.
//

#include <iostream>
#include <vector>
#include <unordered_set>
#include <map>


using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, unordered_set<int>> cntToNums;
        map<int, int> numToCnt;

        for (auto i : nums) {
            if (numToCnt.find(i) == numToCnt.end()) numToCnt[i] = 0;
            else {
                cntToNums[numToCnt[i]].erase(i);
            }
            ++numToCnt[i];
            if (cntToNums.find(numToCnt[i]) == cntToNums.end()) {
                cntToNums[numToCnt[i]] = unordered_set<int>();
            }
            cntToNums[numToCnt[i]].insert(i);
        }

        vector<int> ret;
        for (auto it = cntToNums.rbegin(); it != cntToNums.rend(); ++it) {
            for (auto i : it->second) {
                ret.push_back(i);
                if (ret.size() == k) goto end;
            }
        }
    end:
        return ret;
    }
};

int main() {
    Solution s;
    vector<int> v{1};
    auto vv = s.topKFrequent(v, 2);
    for (auto i : vv) {
        cout << i << " ";
    }
    cout << endl;
}

