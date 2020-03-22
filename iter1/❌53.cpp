//
// Created by chenyufan on 2020/3/22.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int pre = nums[0];
        int res = pre;
        for (int i = 1; i < nums.size(); ++i) {
            pre = pre > 0 ? pre + nums[i] : nums[i];
            res = max(res, pre);
        }
        return res;
    }
};

int main() {
    Solution s;
    vector<int> a = {-2,1,-3,4,-1,2,1,-5,4};
    cout << s.maxSubArray(a) << endl;

}