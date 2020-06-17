//
// Created by chenyufan on 2020/6/10.
//

#include <vector>
#include <bitset>
#include <algorithm>
#include <numeric>

using namespace std;


class Solution {
public:
    bool canPartition(vector<int>& nums) {
        bitset<100* 200/2 +1> bits(1);
        int sum = 0;
        for (auto n : nums) {
            sum += n;
            bits |= bits << n;
        }
        return !(sum%2) && bits[sum/2];
    }
};

int main() {
    Solution s;
    vector<int> v{1, 5, 11, 6};
    cout << s.canPartition(v) << endl;
}