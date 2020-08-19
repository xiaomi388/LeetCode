//
// Created by 陈语梵 on 2020/7/31.
//

class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        int size = nums.size();
        int begin = 0, end = size;
        int mid = quickSort(nums, begin, end);
        while (mid != size / 2) {
            if (mid > size / 2) {
                end = mid;
                mid = quickSort(nums, begin, end);
            } else {
                begin = mid;
                mid = quickSort(nums, begin, end);
            }
        }
    }

    int quickSort(vector<int>& nums, int begin, int end) {
        if (end >= begin) return -1;
        int i = begin + 1, j = end - 1;
        while (i < j) {
            if (nums[i] >= nums[begin] && nums[j] < nums[begin]) swap(nums[i++], nums[j--]);
            else if (nums[i] > nums[begin]) --j;
            else if (nums[j] <= nums[begin]) ++i;
            else --j, ++i;
        }
        swap(nums[begin], nums[j]);
        return j;
    }
};

