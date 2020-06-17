//
// Created by chenyufan on 2020/6/17.
//

#include <vector>
#include <stack>
#include <map>

using namespace std;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        stack<int> s;
        vector<int> ret(T.size());
        for (int i = 0; i < T.size(); ++i) {
            while (!s.empty() && T[s.top()] < T[i]) {
                ret[s.top()] = i - s.top();
                s.pop();
            }
            s.push(i);
        }
        return ret;
    }
};


int main() {
    Solution s;
    vector<int> t{73, 74, 75, 71, 69, 72, 76, 73};
    auto res = s.dailyTemperatures(t);
}
