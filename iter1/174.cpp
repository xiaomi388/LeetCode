// 不够简洁：更简洁版本可加一个dummy row and col.

#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int row = dungeon.size();
        int col = dungeon[0].size();

        int f[row+3][col+3];
        memset(f, 0, sizeof(f));

        f[row][col-1] = 1;
        f[row-1][col] = 1;
        f[row-1][col-1] = max(1, 1-dungeon[row-1][col-1]);

        for (int i = row - 2; i >= 0; --i) {
            f[i][col-1] = max(1, f[i+1][col-1] - dungeon[i][col-1]);
        }


        for (int i = col - 2; i >= 0; --i) {
            f[row-1][i] = max(1, f[row-1][i+1] - dungeon[row-1][i]);
        }


        for (int i = row - 2; i >= 0; --i) {
            for (int q = col - 2; q >= 0; --q) {
                f[i][q] = max(1, min(f[i+1][q], f[i][q+1]) - dungeon[i][q]);
            }
        }

        // print
        for (int i = 0; i < row; ++i) {
            for (int q = 0; q < col; ++q) {
                cout << f[i][q] << " ";
            }
            cout << endl;
        }
        return f[0][0];
    }
};

int main() {
    Solution s;
    vector<vector<int>> dun{
            {-2, -3, 3},
            {-5, -10, 1},
            {10, 30, -5},
    };
    cout << s.calculateMinimumHP(dun) << endl;

}