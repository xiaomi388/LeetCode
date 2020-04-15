//
// Created by chenyufan on 2020/4/12.
//

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
    int candy(vector<int>& ratings) {
        vector<int> nums(ratings.size(), 1);
        for (int i = 1; i < ratings.size(); ++i) {
            if (ratings[i] > ratings[i-1]) nums[i] = nums[i-1]+1;
            else nums[i] = 1;
            cout << nums[i] << " ";
        }

        for (int i = ratings.size() - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i+1]) nums[i] = max(nums[i+1]+1, nums[i]);
        }

        int ret = 0;
        for (auto n : nums) {
            cout << n << " " ;
            ret += n;
        }
        return ret;
    }
};

int main() {
    Solution s;
    vector<int> r{1,0,2};
    cout << s.candy(r) << endl;
}
