//
// Created by 陈语梵 on 2020/7/29.
//

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int _max = 0;
        unordered_set<int> numSet(nums.begin(), nums.end());

        for (auto v : numSet) {
            if (numSet.find(v-1) != numSet.end()) continue;
            int cnt = 1;
            for (; numSet.find(v+cnt) != numSet.end(); cnt++);
            _max = max(cnt, _max);
        }
        return _max;
    }
};


