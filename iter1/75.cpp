// 填高位和低位，那么中位最终肯定能被填好
//

#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;

        for (int i = 0; i <= right;) {
            if (nums[i] == 0) {
                swap(nums[i], nums[left]);
                ++left;
                ++i;
//                i = max(i, left);
            } else if (nums[i] == 1) {
                ++i;
            } else if (nums[i] == 2) {
                swap(nums[i], nums[right]);
                --right;
            }
        }
    }
};

int main() {
    Solution s;
    vector<int> v{2, 0, 1};
    s.sortColors(v);
    for (auto i : v) { cout << i << " "; }
    cout << endl;

}

