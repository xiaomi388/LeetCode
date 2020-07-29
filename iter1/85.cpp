// 思路：和84题一样，我们对每一行看作是84题的直方图的底，然后套用84的方法去做
//

class Solution {
    int _max = -1;

public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty()) return 0;
        vector<vector<int>> histograms(matrix.size(), vector<int>(matrix[0].size()));

        buildHistograms(histograms, matrix);

        for (int i = 0; i < histograms.size(); ++i) {
            calMax(histograms, i);
        }
        return _max;
    }

    void buildHistograms(vector<vector<int>>& histograms, vector<vector<char>>& matrix) {
        for (int r = 0; r < matrix.size(); ++r) {
            for (int c = 0; c < matrix[0].size(); ++c) {
                if (r == 0) {
                    histograms[r][c] = matrix[r][c] == '1';
                    continue;
                }
                histograms[r][c] = matrix[r][c] == '0' ? 0 : histograms[r-1][c] + 1;
            }
        }
    }

    void calMax(vector<vector<int>> &histograms, int r) {
        vector<int> histogram = histograms[r];

        // add sentinel
        histogram.insert(histogram.begin(), -1);
        histogram.push_back(-1);

        stack<int> s;
        s.push(0);

        for (int i = 1; i < histogram.size(); ++i) {
            while (histogram[s.top()] > histogram[i]) {
                int height = histogram[s.top()];
                s.pop();
                _max = max(_max, height * (i - s.top() - 1));
            }
            s.push(i);
        }
    }
};

