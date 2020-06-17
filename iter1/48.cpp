//

#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        for (int i = 0; i < matrix.size() / 2; ++i) {
            _rotate(matrix, i);
        }
    }

    void _rotate(vector<vector<int>>& matrix, int n) {

        for (int i = n; i < matrix.size() - n - 1; ++i) {
            int &f = matrix[n][i];
            int &s = matrix[i][matrix.size()-1-n];
            int &t = matrix[matrix.size()-1-n][matrix.size()-1-i];
            int &l = matrix[matrix.size()-1-i][n];
            swap(f, s); swap(t, l); swap(f, t);
        }
    }
};

int main() {
    Solution s;
    vector<vector<int>> v{
            {1,2,3},
            {4,5,6},
            {7,8,9},
    };
    s.rotate(v);
    for (auto r : v) {
        for (auto i : r) {
            cout << i << " ";
        }
        cout << endl;
    }
}