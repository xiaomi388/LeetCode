//
// Created by chenyufan on 2020/5/12.
//

#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (amount == 0) return 0;

        vector<unsigned int> f(amount+2, -1);
        f[0] = 0;

        for (int i = 1; i <= amount; ++i) {
            for (int coin : coins) {
                if (i - coin >= 0) {
                    f[i] = min(f[i-coin] + 1, f[i]);
                }
            }
        }
        return f[amount];
    }

};


int main() {
    Solution s;
    vector<int> c{1,2,5};
    cout << s.coinChange(c, 1) << endl;
}
