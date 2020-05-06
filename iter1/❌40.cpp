//
// Created by chenyufan on 2020/4/22.
//

#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> current;
        sort(candidates.begin(),candidates.end());
        backTracking(candidates.begin(),current,res,candidates,target);
        return res;
    }

    void backTracking(vector<int>::iterator n, vector<int>& current,vector<vector<int>>& res, const vector<int>& candidates, int target){
        if(!target) res.push_back(current);
        else if(target>0){
            for(;n!=candidates.end()&&*n<=target;++n){
                current.push_back(*n);
                backTracking(n+1,current,res,candidates,target-*n);
                current.pop_back();
                while(n+1!=candidates.end()&&*(n+1)==*n) ++n;
            }
        }
    }
};

int main() {
    Solution s;
    vector<int> v{10, 1, 2, 7, 6, 1, 5};
    auto ret = s.combinationSum2(v, 8);

}