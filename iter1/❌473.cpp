//
// Created by chenyufan on 2020/5/14.
//

#include <vector>
#include <iostream>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
private:
    int maxEdgeLength = 0;

public:
    bool makesquare(vector<int>& nums) {
        if (nums.size() < 4) return false;
        if (nums.empty()) return false;
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % 4 != 0) return false;
        sort(nums.begin(), nums.end(), greater<int>());
        vector<int> edges(4, 0);
        maxEdgeLength = sum / 4;
        return _makesquare(nums, 0, edges);
    }

    bool _makesquare(vector<int>& nums, int i, vector<int>& edges) {
        if (i == nums.size()) return edges[0] == edges[1] && edges[1] == edges[2] && edges[2] == edges[3];
        for (int q = 0; q < 4; ++q) {
            if (edges[q] + nums[i] > maxEdgeLength) continue;

            int j = q;
            while (--j >= 0) if (edges[q] == edges[j]) break;
            if (j != -1) continue;

            edges[q] += nums[i];
            if (_makesquare(nums, i+1, edges)) return true;
            edges[q] -= nums[i];
        }
        return false;
    }
};


int main() {
    Solution s;
    vector<int> nums{1,1,2,2,2};
    cout << s.makesquare(nums) << endl;

}
