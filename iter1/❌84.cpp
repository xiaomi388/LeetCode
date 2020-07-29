// 暴力解法：遍历每一列，以该列向左向右遍历得到最大面积
// TLE

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        if (heights.empty()) return 0;
        int _max = -1;
        for (int i = 0; i < heights.size(); ++i) {
            int lIdx = i, rIdx = i;
            for (; lIdx >= 0 && heights[lIdx] >= heights[i]; --lIdx);
            for (; rIdx < heights.size() && heights[rIdx] >= heights[i]; ++rIdx);
            _max = max((rIdx - lIdx - 1) * heights[i], _max);
        }
        return _max;
    }
};


// Stack
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        if (heights.empty()) return 0;
        int _max = -1;

        // add sentinel
        heights.insert(heights.begin(), -1); heights.push_back(-1);

        stack<int> s;
        s.push(0);

        for (int i = 1; i < heights.size(); ++i) {
            while (heights[s.top()] > heights[i]) {
                int height = heights[s.top()];
                s.pop();
                _max = max((i - s.top() - 1) * height, _max);
            }
            s.push(i);
        }
        return _max;
    }
};

