//
// Created by chenyufan on 2020/6/2.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int fast = nums[nums[0]], slow = nums[0];
        while (fast != slow) {
            slow = nums[slow];
            fast = nums[nums[fast]];
        }
        fast = 0;
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }
};

int main() {
    Solution s;
    vector<int> v{1,3,4,2,2};
    cout << s.findDuplicate(v) << endl;
}

