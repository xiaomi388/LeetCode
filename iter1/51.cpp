//
// Created by chenyufan on 2020/5/11.
//

#include <vector>
#include <unordered_set>
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<int>> states;
        vector<int> state;
        _solveNQueens(state, states, 0, n);


        vector<vector<string>> ret(states.size(), vector<string>(n, string(n, '.')));
        for (int i = 0; i < states.size(); ++i) {
            for (int q = 0; q < states[i].size(); ++q) {
                ret[i][q][states[i][q]] = 'Q';
            }
        }
        return ret;
    }

    void _solveNQueens(vector<int> &state, vector<vector<int>> &states, int curRow, int n) {
        if (curRow >= n) {
            states.push_back(state);
            return;
        }

        unordered_set<int> unusableIndex;
        for (int r = 0; r < state.size(); ++r) {
            int c = state[r];
            unusableIndex.insert(c);
            if (c + (curRow - r) < n) unusableIndex.insert(c + (curRow - r));
            if (c - (curRow - r) >= 0) unusableIndex.insert(c - (curRow - r));
        }

        for (int i = 0; i < n; ++i) {
            if (unusableIndex.find(i) == unusableIndex.end()) {
                state.push_back(i);
                _solveNQueens(state, states, curRow+1, n);
                state.pop_back();
            }
        }
    }
};


int main() {
    Solution s;
    auto ret = s.solveNQueens(5);
    for (auto i : ret) {
        for (auto r : i) {
            for (auto q : r) {
                cout << q;
            }
            cout << endl;
        }
        cout << "-------" << endl;
    }
}
