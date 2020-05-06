//
// Created by chenyufan on 2020/5/6.
//

#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end()); sort(s.begin(), s.end());
        int curCki = 0, curCld = 0, res = 0;
        while (curCki < s.size() && curCld < g.size()) {
            if (s[curCki++] >= g[curCld]) {
                res++;curCld++;
            }
        }
        return res;
    }
};

int main() {
    Solution ss;
    vector<int> g{1,2};
    vector<int> s{1,2, 3};
    auto res = ss.findContentChildren(g, s);
    cout << res << endl;

}
