// 思路：dfs，每一层选一个数字。注意要点是，下一层不能选前一层之前的数字。


#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        return combinationSum(candidates, target, 0);
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target, int left) {
        vector<vector<int>> ret;
        for (int i = left; i < candidates.size(); ++i) {
            if (target - candidates[i] < 0) continue;
            else if (target - candidates[i] == 0) ret.push_back({candidates[i]});
            else {
                auto nextRet = combinationSum(candidates, target - candidates[i], i);
                for (auto &row : nextRet) {
                    row.push_back(candidates[i]);
                    ret.push_back(row);
                }
            }
        }
        return ret;
    }
};


int main() {
    Solution s;
    vector<int> candidates{2,3,5};
    auto res = s.combinationSum(candidates, 8);
    for (auto &row : res) {
        for (auto n : row) {
            cout << n << " ";
        }
        cout << endl;
    }
}
