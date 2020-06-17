// 这题能用dp...

#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        if (matrix.empty()) return 0;
        vector<vector<int>> dp(matrix.size(), vector<int>(matrix[0].size()));
        for (int i = 0; i < matrix.size(); ++i) dp[i][0] = (matrix[i][0] == '1') ? 1 : 0;
        for (int i = 0; i < matrix[0].size(); ++i) dp[0][i] = (matrix[0][i] == '1') ? 1 : 0;
        int res = INT_MIN;
        for (int i = 1; i < matrix.size(); ++i) {
            for (int q = 1; q < matrix[0].size(); ++q) {
                if (matrix[i][q] == '1') {
                    dp[i][q] = min(dp[i-1][q], min(dp[i][q-1], dp[i-1][q-1])) + 1;
                } else {
                    dp[i][q] = 0;
                }
                res = max(res, dp[i][q]);
            }
        }
        return res * res;
    }
};

int main() {

}
