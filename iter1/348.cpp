//
// Created by 陈语梵 on 2020/8/23.
//

class TicTacToe {
    vector<int> rows, cols;
    int leftDig, rightDig;
    int n;
public:
    /** Initialize your data structure here. */
    TicTacToe(int n) {
        this->n = n;
        rows = vector<int>(n);
        cols = vector<int>(n);
        leftDig = 0;
        rightDig = 0;
    }

    /** Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
    int move(int row, int col, int player) {
        rows[row] += player == 1 ? 1 : -1;
        if (abs(rows[row]) == n) return player;

        cols[col] += player == 1 ? 1 : -1;
        if (abs(cols[col]) == n) return player;

        if (row == col) {
            leftDig += player == 1 ? 1 : -1;
            if (abs(leftDig) == n) return player;
        }
        if (row == n - col - 1) {
            rightDig += player == 1 ? 1 : -1;
            if (abs(rightDig) == n) return player;
        }
        return 0;
    }
};

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe* obj = new TicTacToe(n);
 * int param_1 = obj->move(row,col,player);
 */

