//
// Created by chenyufan on 2020/5/27.
//

#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        if (nums.size() < 1) return true;
        int nearest = nums.size() - 1;

        for (int i = int(nums.size() - 2); i >= 0; --i) {
            if (nums[i] + i >= nearest) nearest = i;
        }
        return nearest == 0;
    }
};

int main() {

}

