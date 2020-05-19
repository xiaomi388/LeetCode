//
// Created by chenyufan on 2020/5/19.
//

#include <vector>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int num = 0;
        for (int i = 0; i < nums.size(); ++i) {
            num ^= nums[i];
        }
        return num;
    }
};

int main() {

}

