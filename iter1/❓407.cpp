//
// Created by chenyufan on 2020/5/8.
//

#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int trapRainWater(vector<vector<int>>& heightMap) {
        int row = heightMap.size();
        int col = heightMap[0].size();
        // -1 wall 1 water 0 undefined
        vector<vector<int>> islandMap(row, vector<int>(col));
        for (int i = 1; i < row -1; ++i) {
            for (int q = 1; q < col - 1; ++q) {
                queue<pair<int,int>> cordQueue;
                cordQueue.push({i, q});
                while (!cordQueue.empty()) {
                    auto cord = cordQueue.front();
                    cordQueue.pop();
                    if (islandMap[cord.first][cord.second]) continue;

                }
            }
        }
    }

};

int main() {}

