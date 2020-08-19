// 一圈作为一个循环；循环完一圈后，再刷新下一圈的边界值。
//

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if(matrix.empty() || matrix[0].empty()) return {};

        vector<int> ret; //(matrix.size() * matrix[0].size);
        int up = 0, down = matrix.size()-1, left = 0, right = matrix[0].size()-1;
        while (true) {
            for (int i = left; i <= right; ++i) ret.push_back(matrix[up][i]);
            if (++up > down) break;
            for (int i = up; i <= down; ++i) ret.push_back(matrix[i][right]);
            if (--right < left) break;
            for (int i = right; i >= left; --i) ret.push_back(matrix[down][i]);
            if (--down < up) break;
            for (int i = down; i >= up; --i) ret.push_back(matrix[i][left]);
            if (++left > right) break;
        }
        return ret;
    }
};



