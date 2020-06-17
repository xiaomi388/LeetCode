//
// Created by chenyufan on 2020/6/2.
//

#include <unordered_map>
#include <iostream>

using namespace std;

class Solution {

    unordered_map<int, int> memo;

public:
    int numSquares(int n) {
        if (n == 0) return 0;
        if (memo.find(n) != memo.end()) return memo[n];

        int ret = INT_MAX;
        for (int i = 1; i*i <= n; ++i) {
            ret = min(numSquares(n-i*i), ret);
        }
        if (ret != INT_MAX) ++ret;
        memo[n] = ret;
        return ret;
    }
};

int main() {
    Solution s;
    cout << s.numSquares(13) << endl;
}
