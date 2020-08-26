//
// Created by 陈语梵 on 2020/8/21.
//

class Solution {
    bool equals(vector<int> &a, vector<int> &b) {
        for (int i = 0; i < 8; ++i) if (a[i] != b[i]) return false;
        return true;
    }

public:
    vector<int> prisonAfterNDays(vector<int>& cells, int N) {
        // move 1 step
        cells[0] = 0; cells[7] = 0;
        for (int i = 1; i < 7; ++i) cells[i] = cells[i-1] == cells[i+1] ? 1 : 0;
        N--;

        vector<int> oriCells = cells;

        for (int i = 0; i < N; ++i) {
            for (int i = 1; i < 7; ++i) cells[i] = cells[i-1] == cells[i+1] ? 1 : 0;
            if (equals(cells, oriCells)) {
                N %= i; i = -1;
                continue;
            }
        }
    }
};

