// 这道题还有很多做法，可以尝试一下 dfs。
//

#include <vector>
#include <cmath>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ret;
        for (int i = 0; i < (1 << nums.size()); ++i) {
            vector<int> picked;
            for (int pos = 0; pos < nums.size(); ++pos) {
                if (i & (1 << pos)) picked.push_back(nums[pos]);
            }
            ret.push_back(picked);
        }
        return ret;
    }
};

int main() {
    Solution s;
    vector<int> v{1, 2, 3};
    auto ret = s.subsets(v);
    for (int i = 0; i < ret.size(); ++i) {
        for (int j = 0; j < ret[i].size(); ++j) {
            cout << ret[i][j] << " ";
        }
        cout << endl;
    }
}

