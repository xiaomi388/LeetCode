//
// Created by chenyufan on 2020/5/7.
//

#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        int size = nums.size();
        if (size == 0) return 0;
        if (size == 1) return nums[0];

        int m[size];
        m[size-1] = nums[size-1];
        m[size-2] = max(nums[size-1], nums[size-2]);

        for (int i = size-3; i >= 0; --i) {
            m[i] = max(nums[i] + m[i+2], m[i+1]);
        }
        return m[0];
    }
};

int main() {
    Solution s;
    vector<int> v{2,7,9,3,1};
    cout << s.rob(v) << endl;

}
