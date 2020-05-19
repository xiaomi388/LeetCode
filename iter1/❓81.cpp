//
// Created by chenyufan on 2020/5/9.
//

#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    bool search(vector<int>& nums, int target) {
        if (nums.empty()) return false;
        if (target == nums.front() || target == nums.back()) return true;

        int size = nums.size();
        int l = 0, r = size;
        while (r - l > 1) {
            int m = (l + r) / 2;
            if (nums[m] == target) return true;

            if (nums[m] > nums[l]) l = m;
            else if (nums[m] < nums[r-1]) r = m;
            else --r;
        }
        decltype(nums.begin()) start, end;
        if (target >= nums[0] && target <= nums[l]) {
            start = nums.begin();
            end = start + r;
        } else {
            start = nums.begin() + r;
            end = nums.end();
        }
        auto pp = equal_range(start, end, target);
        return !(pp.first == pp.second);
    }
};

int main() {
    Solution s;
    vector<int> nums{1, 1};
    cout << s.search(nums, 0) << endl;
}

