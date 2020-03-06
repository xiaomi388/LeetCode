// 艰难的一次做题..
// 首先，思路是对nums1进行二分，然后从nums2中挑选剩余的前k个，最后判断四个中间值的情况，根据不同情况，调整下一次划分
// 自己的一些弱点：1. 对二分不熟；2. nums1比nums2长时，调换顺序即可

#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }

        const int total = nums1.size() + nums2.size();
        int lo = 0, hi = nums1.size();

        while (true) {
            int mid1 = (lo + hi) / 2;
            int nums1LeftMax = mid1-1 >= 0 ? nums1[mid1-1] : INT_MIN;
            int nums1RightMin = mid1 < nums1.size() ? nums1[mid1] : INT_MAX;

            int mid2 = total / 2 - mid1;
            int nums2LeftMax = mid2-1 >= 0 ? nums2[mid2-1] : INT_MIN;
            int nums2RightMin = mid2 < nums2.size() ? nums2[mid2] : INT_MAX;

            if (nums1LeftMax <= nums2RightMin && nums2LeftMax <= nums1RightMin) {
                if (total % 2) return min(nums1RightMin, nums2RightMin);
                else return (max(nums1LeftMax, nums2LeftMax) + min(nums1RightMin, nums2RightMin)) / 2.0;
            } else if (nums1LeftMax > nums2RightMin) {
                hi = mid1;
            } else if (nums2LeftMax > nums1RightMin) {
                lo = mid1 + 1;
            }
        }
    }
};


int main() {
    Solution s;
    vector<int> v1 = {1, 2}, v2 = {3, 4};
    cout << s.findMedianSortedArrays(v1, v2) << endl;
}

