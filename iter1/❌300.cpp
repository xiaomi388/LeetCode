// 有特定算法能做这题
//

#include <vector>
#include <map>
#include <iostream>

using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> ret;
        for (auto val : nums) {
            auto it = lower_bound(ret.begin(), ret.end(), val);
            if (it == ret.end()) ret.push_back(val);
            else *it = val;
        }
        return ret.size();
    }
};

int main() {
    Solution s;
    vector<int> v{10, 9, 2, 5, 3, 7, 101, 18};
    cout << s.lengthOfLIS(v) << endl;


}

