//
// Created by chenyufan on 2020/6/1.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ret(nums.size());
        int q = 1;
        for (int i = 0; i < nums.size(); ++i) {
            ret[i] = q ;
            q *= nums[i];
        }
        q = 1;
        for (int i = nums.size()-1; i >= 0; --i) {
            ret[i] *= q;
            q *= nums[i];
        }
        return ret;
    }
};


int main() {
    Solution s;
    vector<int> v{1,2,3,4};
    auto r = s.productExceptSelf(v);
    for (auto c : r) {
        cout << c << " " ;
    }
    cout << endl;

}
