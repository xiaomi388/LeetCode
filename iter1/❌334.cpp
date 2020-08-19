// 思路：保存最小的前两个数即可。若当前遍历的数字都比这两数字大，则说明已经找到。

class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int c1 = INT_MAX, c2 = INT_MAX;
        for (auto x : nums) {
            if (x <= c1) c1 = x;
            else if (x <= c2) c2 = x;
            else return true;
        }
        return false;
    }
};
