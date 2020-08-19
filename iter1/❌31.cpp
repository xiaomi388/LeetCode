//
// https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-by-leetcode/
// 1. 从后往前找第一个非递增元素，找到之后再从后面找一个刚好比这个元素大一点的元素
// 互换位置，然后给后面排序


class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        for (int i = nums.size()-2; i >= 0; --i) {
            if (nums[i] >= nums[i+1]) continue;
            for (int q = nums.size()-1; q > i; --q) {
                if (nums[q] <= nums[i]) continue;
                swap(nums[i], nums[q]);
                sort(nums.begin()+i+1, nums.end());
                return ;
            }
        }
        return sort(nums.begin(), nums.end());
    }
};

