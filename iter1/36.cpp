//
// Created by chenyufan on 2020/5/28.
//

#include <vector>
#include <unordered_set>
#include <iostream>

using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int row = board.size(), col = board[0].size();

        unordered_set<char> dict;
        for (int i = 0; i < row; ++i) {
            dict.clear();
            for (int q = 0; q < col; ++q) {
                if (dict.find(board[i][q]) != dict.end()) return false;
                if (board[i][q] != '.') dict.insert(board[i][q]);
            }
        }

        for (int i = 0; i < col; ++i) {
            dict.clear();
            for (int q = 0; q < row; ++q) {
                if (dict.find(board[q][i]) != dict.end()) return false;
                if (board[q][i] != '.') dict.insert(board[q][i]);
            }
        }

        for (auto j : {0, 3, 6}) {
            for (auto u : {0, 3, 6}) {
                dict.clear();
                for (int i = j; i < j+3; ++i) {
                    for (int q = u; q < u+3; ++q) {
                        if (dict.find(board[q][i]) != dict.end()) return false;
                        if (board[q][i] != '.') dict.insert(board[q][i]);
                    }
                }
            }
        }
        return true;
    }
};

