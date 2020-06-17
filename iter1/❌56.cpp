// 先排序... 然后两个两个顺序合并....
//

#include <iterator>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) return {};
        sort(intervals.begin(), intervals.end(), [](vector<int> a, vector<int>b){return a[0] < b[0];});
        vector<vector<int>> ret;
        ret.push_back(intervals[0]);
        for (int i = 1; i < intervals.size(); ++i) {
            if (intervals[i][0] <= ret.back()[1]) ret.back()[1] = max(intervals[i][1], ret.back()[1]);
            else ret.push_back(intervals[i]);
        }
        return ret;
    }
};


int main() {

}

