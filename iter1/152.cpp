//
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.empty()) return 0;
        vector<int> dp(nums.size()), mdp(nums.size());

        dp[0] = mdp[0] = nums[0];

        for (int i = 1; i < nums.size(); ++i) {
            int a = dp[i-1] * nums[i], b = mdp[i-1] * nums[i], c = nums[i];
            dp[i] = max(max(a, b), c);
            mdp[i] = min(min(a, b), c);
        }

        int ret = INT_MIN;
        for (int i = 0; i < nums.size(); ++i) {
            ret = max(dp[i], ret);
        }
        return ret;
    }
};

int main() {

}

