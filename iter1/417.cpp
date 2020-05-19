//
// Created by chenyufan on 2020/5/8.
//

#include <vector>
#include <queue>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
        if (matrix.empty()) return {};

        int row = matrix.size();
        int col = matrix[0].size();
        vector<vector<int>> res;
        vector<vector<int>> f(row, vector<int>(col));
        queue<pair<int, int>> gridQueue;
        for (int i = 0; i < row; ++i) {
            gridQueue.push({i, 0});
        }

        for (int i = 0; i < col; ++i) {
            gridQueue.push({0, i});
        }

        while (!gridQueue.empty()) {
            auto grid = gridQueue.front();
            gridQueue.pop();
            int x = grid.first, y = grid.second;
            if (f[x][y] != 0) continue;
            f[x][y] += 1;
            for (int i : {-1, 1}) {
                if (x+i >= 0 && x+i < row && matrix[x][y] <= matrix[x+i][y]) gridQueue.push({x+i, y});
            }
            for (int i : {-1, 1}) {
                if (y+i >= 0 && y+i < col && matrix[x][y] <= matrix[x][y+i]) gridQueue.push({x, y+i});
            }
        }


        for (int i = 0; i < row; ++i) {
            gridQueue.push({i, col-1});
        }

        for (int i = 0; i < col; ++i) {
            gridQueue.push({row-1, i});
        }

        while (!gridQueue.empty()) {
            auto grid = gridQueue.front();
            gridQueue.pop();
            int x = grid.first, y = grid.second;
            if (f[x][y] == 2 || f[x][y] == 3) continue;
            f[x][y] += 2;
            if (f[x][y] == 3) res.push_back({x, y});
            for (int i : {-1, 1}) {
                if (x+i >= 0 && x+i < row && matrix[x][y] <= matrix[x+i][y]) gridQueue.push({x+i, y});
            }
            for (int i : {-1, 1}) {
                if (y+i >= 0 && y+i < col && matrix[x][y] <= matrix[x][y+i]) gridQueue.push({x, y+i});
            }
        }


        return res;
    }
};

int main() {
    Solution s;
    vector<vector<int>> martrix{
            {1,2,2,3,5},
            {3,2,3,4,4},
            {2,4,5,3,1},
            {6,7,1,4,5},
            {5,1,1,2,4},
    };
    auto res = s.pacificAtlantic(martrix);
    for (auto r : res) {
        for (auto i : r) {
            cout << i << " ";
        }
        cout << endl;
    }

}

