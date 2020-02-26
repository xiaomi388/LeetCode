// 总结：先二分找出最大点和最小点，然后判断target落在哪个区间，二分查找即可。

#include <vector>
#include <cmath>
#include <iostream>

using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.size() == 0) return -1;
        if (nums.size() == 1) {
            if (target == nums[0]) return 0;
            else return -1;
        }

        int startPos = 0, endPos = nums.size() - 1;
        int maxNumPos = startPos, minNumPos = endPos;

        while (minNumPos > maxNumPos + 1) {
            int mid = (minNumPos + maxNumPos) / 2;
            if (nums[mid] < nums[minNumPos]) {
                minNumPos = mid;
            } else {
                maxNumPos = mid;
            }
        }

        if (target >= nums[startPos] && target <= nums[maxNumPos]) {
            return binSearch(nums, startPos, maxNumPos, target);
        } else {
            return binSearch(nums, minNumPos, endPos, target);
        }
    }

    int binSearch(vector<int>&nums, int leftPos, int rightPos, int target) {
        while (rightPos > leftPos + 1) {
            if (target == nums[leftPos]) return leftPos;
            if (target == nums[rightPos]) return rightPos;

            int mid = (rightPos + leftPos) / 2;
            if (target <= nums[mid]) rightPos = mid;
            else leftPos = mid;
        }
        if (target == nums[leftPos]) return leftPos;
        if (target == nums[rightPos]) return rightPos;
        return -1;
    }
};



int main() {
    Solution s;
    vector<int> n = {3, 1, 2};
    int i = s.search(n, 3);
    cout << i << endl;
}