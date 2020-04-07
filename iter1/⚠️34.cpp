// 虽然过了，但是解法不是最优的
// 最优方法：left_search & right_search

#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        auto l = binSearch(nums, 0, nums.size(), target, true);
        cout << l << endl;
        auto r = binSearch(nums, 0, nums.size(), target, false);
        cout << r << endl;
        if (l > r) return{-1, -1};
        return {l, r};
    }

    int binSearch(vector<int>& nums, int l, int r, int target, bool isLeft) {
        if (l == r) return isLeft ? r : r - 1;
        int m = (l + r) / 2;
        if (isLeft) {
            if (nums[m] >= target) return binSearch(nums, l, m, target, isLeft);
            else return binSearch(nums, m+1, r, target, isLeft);
        } else {
            if (nums[m] > target) return binSearch(nums, l, m, target, isLeft);
            else return binSearch(nums, m+1, r, target, isLeft);
        }
    }
};

int main() {
    Solution s;
    vector<int> a{5,7,7,8,8,10};
    auto res = s.searchRange(a, 8);
    cout << res[0] << " " << res[1] << endl;
}
