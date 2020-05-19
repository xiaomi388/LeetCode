//
// Created by chenyufan on 2020/5/9.
//

#include <map>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        map<int, int> m;
        for (auto num : nums) {
            if (m.find(num) == m.end()) m[num] = 1;
            else m[num]++;
        }
        vector<vector<int>> ret;
        vector<int> ans;
        bfs(m, ans, ret, nums.size());
        return ret;
    }

    void bfs(map<int, int> &m, vector<int>& ans, vector<vector<int>>& ret, int size) {
        if (ans.size() == size) {
            ret.push_back(ans);
            return ;
        }
        for (auto it = m.begin(); it != m.end(); ++it) {
            int num = it->first, cnt = it->second;
            if (cnt <= 0) continue;
            ans.push_back(num);
            it->second--;
            bfs(m, ans, ret, size);
            it->second++;
            ans.pop_back();
        }
    }

};

int main() {
    Solution s;
    vector<int> nums{1,2,3};
    auto ret = s.permuteUnique(nums);
    for (auto r : ret) {
        for (auto i : r) {
            cout << i << " ";
        }
        cout << endl;
    }

}

