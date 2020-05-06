// 老剑指offer题目了。

#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        nums.push_back(INT_MIN);
        for (int i = 0; i < nums.size(); ++i) {
            while (nums[i] != i) {
                if (nums[i] < 0 || nums[i] >= nums.size() || nums[i] == nums[nums[i]]) break;
                swap(nums[i], nums[nums[i]]);
            }
        }
        int i = 1;
        for (; i < nums.size(); ++i) {
            if (nums[i] != i) return i;
        }
        return i;
    }
};


int main() {
    Solution s;
    vector<int> v{-1,-1};
    cout << s.firstMissingPositive(v) << endl;
}

