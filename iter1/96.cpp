//
//


class Solution {
    vector<vector<int>> dp;
public:
    int numTrees(int n) {
        dp = vector<vector<int>>(n+3, vector<int>(n+3));
        return _numTrees(1, n);
    }

    int _numTrees(int l, int r) {
        if (l >= r) return 1;
        if (dp[l][r] != 0) return dp[l][r];

        int ret = 0;
        for (int i = l; i <= r; ++i) {
            ret += _numTrees(l, i-1) * _numTrees(i+1, r);
        }
        dp[l][r] = ret;
        return ret;
    }
};

