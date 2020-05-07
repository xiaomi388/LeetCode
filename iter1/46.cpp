//
// Created by chenyufan on 2020/5/7.
//

#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ret;
        vector<int> ans(nums.size());
        vector<bool> taken(nums.size(), false);
        _permute(nums, ret, ans, taken, 0);
        return ret;
    }

    void _permute(vector<int>& nums, vector<vector<int>>& ret, vector<int> &ans, vector<bool> &taken, int curPos) {
        if (curPos >= nums.size()) {
            ret.push_back(ans);
            return;
        }
        for (int i = 0; i < ans.size(); ++i) {
            if (!taken[i]) {
                ans[i] = nums[curPos];
                taken[i] = true;
                _permute(nums, ret, ans, taken, curPos + 1);
                taken[i] = false;
            }
        }
    }
};

int main() {
    Solution s;
    vector<int> nums{1, 2, 3};
    auto res = s.permute(nums);
    for (auto r : res) {
        for (auto c : r) {
            cout << c << " ";
        }
        cout << endl;
    }
}
