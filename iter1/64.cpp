//
// Created by chenyufan on 2020/5/28.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        if (grid.empty()) return 0;
        int row = grid.size(), col = grid[0].size();
        vector<vector<int>> dp(row, vector<int>(col));
        for (int i = row-1; i >= 0; --i) {
            for (int q = col-1; q >= 0; --q) {
                if (i == row-1 && q == col-1) {
                    dp[row-1][col-1] = grid[row-1][col-1];
                    continue;
                }
                int right = q+1 < col ? dp[i][q+1] : INT_MAX;
                int down = i+1 < row ? dp[i+1][q] : INT_MAX;
                dp[i][q] = min(right, down) + grid[i][q];
            }
        }
        return dp[0][0];
    }
};

int main() {
    Solution s;
    vector<vector<int>> v{
            {1,3,1},
            {1,5,1},
            {4,2,1},
    };
    cout << s.minPathSum(v) << endl;

}