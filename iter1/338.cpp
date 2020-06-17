// 杨辉三角，找规律即可
//

#include <cmath>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> countBits(int num) {
        if (num == 0) return {0};
        vector<int> dp(num+1);
        dp[0] = 0; dp[1] = 1;
        for (int val = 2; val <= num; ++val) {
            dp[val] = dp[val >> 1] + (val & 1);
        }
        return dp;
    }
};


int main() {
    Solution s;
    auto v = s.countBits(5);
    for (auto i : v) {
        cout << i << " ";
    }
    cout << endl;
}
