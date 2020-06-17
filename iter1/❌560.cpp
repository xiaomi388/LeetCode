// preSum + map
//

#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int sum = 0, result = 0;
        unordered_map<int, int> preSum;
        preSum[0] = 1;
        for (auto n : nums) {
            sum += n;
            if (preSum.find(sum - k) != preSum.end()) {
                result += preSum[sum-k];
            }
            if (preSum.find(sum) != preSum.end()) {
                preSum[sum]++;
            } else {
                preSum[sum] = 1;
            }
        }
        return result;
   }
};

int main() {
    Solution s;
    vector<int> v{1,1,1};
    cout << s.subarraySum(v, 2) << endl;
}
