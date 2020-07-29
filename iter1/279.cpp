//
// Created by chenyufan on 2020/6/2.
//

class Solution {
    vector<int> dp;
public:
    int numSquares(int n) {
        dp = vector<int>(n+3);
        return _numSquares(n);
    }

    int _numSquares(int n) {
        if (dp[n]) return dp[n];
        if (n == 0) return 0;
        int _min = INT_MAX;
        for (int i = 1, q = int(sqrt(n)); i <= sqrt(n); ++i) {
            _min = min(_min, 1 + _numSquares(n - i*i));
        }
        dp[n] = _min;
        return _min;
    }
};



