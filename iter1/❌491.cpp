//
// Created by chenyufan on 2020/5/18.
//

#include <vector>
#include <map>
#include <iostream>
#include <unordered_set>

using namespace std;

class Solution {
public:
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        vector<vector<int>> ret;
        vector<int> tmp;
        dfs(nums, 0, ret, tmp);
        return ret;
    }

    void dfs(vector<int>& nums, int i, vector<vector<int>>& states, vector<int> &state) {
        if (state.size() > 1) states.push_back(state);

        unordered_set<int> m;
        for (int q = i; q < nums.size(); ++q) {
            if ((state.empty() || state.back() <= nums[q]) && m.find(nums[q]) == m.end() ) {
                state.push_back(nums[q]);
                dfs(nums, q+1, states, state);
                state.pop_back();
                m.insert(nums[q]);
            }
        }
    }
};


int main() {
    Solution s;
    vector<int> a{4, 6, 7, 7};
    auto ret = s.findSubsequences(a);
    for (auto r : ret) {
        for (auto i : r) {
            cout << i << " ";
        }
        cout << endl;
    }
}


