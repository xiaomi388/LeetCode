// 可以dp。。。 其实跟背包问题一样
//
// 新知识：二维unordered_map可以在一维用vector，这样可以更方便初始化所有unordered_map

#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
    vector<unordered_map<long long, int>> dp;
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        dp = vector<unordered_map<long long, int>>(nums.size());
        if (nums.empty()) return 0;
        return _findTargetSumWays(nums, nums.size()-1, S);
    }

    int _findTargetSumWays(vector<int>& nums, int i, long long S) {
        if (i == 0) return (S == -nums[0]) + (S == nums[0]);
        if (dp[i].find(S) != dp[i].end()) return dp[i][S];
        int res = _findTargetSumWays(nums, i-1, S+nums[i]) + _findTargetSumWays(nums, i-1, S-nums[i]);
        dp[i][S] = res;
        return res;
    }
};


int main() {
    Solution s;
    vector<int> nums{1,1,1,1,1};
    cout << s.findTargetSumWays(nums, 3) << endl;
}
