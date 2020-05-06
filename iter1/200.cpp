//
// Created by chenyufan on 2020/4/21.
//

#include <unordered_map>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
    int **searched;
    int ret = 0;
public:
    int numIslands(vector<vector<char>>& grid) {
        searched = new int*[grid.size()];
        for (int i = 0; i < grid.size(); ++i) {
            searched[i] = new int[grid[0].size()];
            for (int j = 0; j < grid[0].size(); ++j) searched[i][j] = 0;
        }


        for (int i = 0; i < grid.size(); ++i) {
            for (int q = 0; q < grid[0].size(); ++q) {
                ret += search(i, q, grid);
            }
        }
        return ret;
    }

    bool search(int i, int j, vector<vector<char>>& grid) {
        if (i < 0 || i >= grid.size()) return false;
        if (j < 0 || j >= grid[0].size()) return false;

        if (searched[i][j]) return 0;
        searched[i][j] = 1;

        if (grid[i][j] == '0') return false;

        search(i+1, j, grid); search(i-1, j, grid); search(i, j+1, grid); search(i, j-1, grid);
        return true;
    }
};



int main() {
    Solution s;
    vector<vector<char>> v{
     {1,1,0,0,0},
     {1,1,0,0,0},
     {0,0,1,0,0},
     {0,0,0,1,1},
    };
    cout << s.numIslands(v) << endl;

}
