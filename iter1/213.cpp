//
// Created by chenyufan on 2020/5/7.
//

#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.empty()) return 0;
        if (nums.size() == 1) return nums[0];

        return max(_rob(nums, 0, nums.size()-1), _rob(nums, 1, nums.size()));
    }

    int _rob(vector<int>& nums, int l, int r) {
        int size = r-l;
        if (size == 0) return 0;
        if (size == 1) return nums[l];

        int m[size];
        m[size-1] = nums[r-1];
        m[size-2] = max(nums[r-1], nums[r-2]);

        for (int i = size-3; i >= 0; --i) {
            m[i] = max(nums[i+l] + m[i+2], m[i+1]);
        }

        return m[0];

    }
};

int main() {
    Solution s;
    vector<int> v{2,3,2};
    cout << s.rob(v) << endl;

}
