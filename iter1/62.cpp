//
// Created by chenyufan on 2020/5/28.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m, vector<int>(n));
        dp[m-1][n-1] = 1;
        for (int i = m-1; i >= 0; --i) {
            for (int q = n-1; q >= 0; --q) {
                dp[i][q] += (i+1 < m ? dp[i+1][q] : 0) + (q+1 < n ? dp[i][q+1] : 0);
            }
        }
        return dp[0][0];
    }
};

int main() {
    Solution s;
    cout << s.uniquePaths(7,3) << endl;

}

