//
// Created by chenyufan on 2020/4/15.
//

#include <vector>
#include <iostream>


using namespace std;

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int f[triangle.size()+3][triangle.size()+3];

        f[0][0] = triangle[0][0];
        for (int i = 1; i < triangle.size(); ++i) {
            f[i][i] = f[i-1][i-1] + triangle[i][i];
            f[i][0] = f[i-1][0] + triangle[i][0];
        }
        for (int i = 1; i < triangle.size(); ++i) {
            for (int j = 1; j < i; j ++) {
                f[i][j] = min(f[i-1][j] + triangle[i][j], f[i-1][j-1] + triangle[i][j]);
            }
        }

        int _min = INT_MAX;
        for (int i = 0; i < triangle.size(); ++i) {
            _min = min(f[triangle.size()-1][i], _min);
        }
        return _min;
    }
};

int main() {
    Solution s;
    vector<vector<int>> t{
            {2},
            {3,4},
            {6,5,7},
            {4,1,8,3},
    };
    cout << s.minimumTotal(t) << endl;
}
