//
// Created by chenyufan on 2020/5/19.
//

#include <vector>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int a = 0, b = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (i % 2) a ^= nums[i];
            else b ^= nums[i];
        }
        return a == 0 ? b : a;
    }
};

int main() {

}

