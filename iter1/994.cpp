// BFS技巧：1. dir_x, dir_y，用于控制一个循环就获取所有下一阶的点
// 2. 层级BFS，在循环内再做一个循环，循环次数是当前queue的大小

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        queue<pair<int, int>> q;

        int orgLeft = 0;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == 2) q.push({i, j});
                else if (grid[i][j] == 1) orgLeft++;
            }
        }

        if (orgLeft == 0) return 0;

        int ts = 0;
        while (!q.empty()) {
            ts++;
            int t = q.size();
            while (t--) {
                auto cord = q.front(); q.pop();

                static vector<int> dir_x{0, 0, 1, -1};
                static vector<int> dir_y{1, -1, 0, 0};

                for (int i = 0; i < 4; ++i) {
                    int tx = cord.first + dir_x[i], ty = cord.second + dir_y[i];

                    if (tx >= 0 &&  tx < grid.size() &&
                        ty >= 0 && ty < grid[0].size() &&
                        grid[tx][ty] == 1) {
                        orgLeft--;
                        grid[tx][ty] = 2;
                        q.push({tx, ty});
                    }
                }
            }
        }
        return orgLeft ? -1 : ts-1;
    }
};

