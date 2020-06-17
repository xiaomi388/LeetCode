//
// Created by chenyufan on 2020/5/8.
//

#include <vector>
#include <queue>
#include <iostream>

using namespace std;

class Solution {
public:
    int trapRainWater(vector<vector<int>>& heightMap) {
        int maxLevel = 0;
        for (int r = 0; r < heightMap.size(); ++r) {
            for (int c = 0; c < heightMap[0].size(); ++c) {
                maxLevel = max(maxLevel, heightMap[r][c]);
            }
        }
        int ret = 0;
        for (int l = 1; l <= maxLevel; ++l) {
            dfsFillEdges(heightMap, l);
        }

        int row = heightMap.size(), col = heightMap[0].size();
        for (int r = 0; r < row; ++r) {
            for (int c = 0; c < col; ++c) {
                if (heightMap[r][c] < maxLevel) ret += (maxLevel - heightMap[r][c]);
            }
        }
        return ret;
    }

    void dfsFillEdges(vector<vector<int>>& heightMap, int level) {
        int row = heightMap.size(), col = heightMap[0].size();

        for (int r = 0; r < row; ++r) {
            dfsFill(heightMap, r, 0, level);
            dfsFill(heightMap, r, col-1, level);
        }

        for (int c = 0; c < col; ++c) {
            dfsFill(heightMap, 0, c, level);
            dfsFill(heightMap, row-1, c, level);
        }
    }

    void dfsFill(vector<vector<int>>& heightMap, int r, int c, int level) {
        int row = heightMap.size(), col = heightMap[0].size();
        if (r < 0 || c < 0 || r >= row || c >= col) return ;
        else if (heightMap[r][c]+1 != level) return;
        heightMap[r][c] = level;
        dfsFill(heightMap, r+1, c, level);
        dfsFill(heightMap, r-1, c, level);
        dfsFill(heightMap, r, c+1, level);
        dfsFill(heightMap, r, c-1, level);
    }
};

int main() {
    Solution s;
    vector<vector<int>>()
    s.trapRainWater()

}

