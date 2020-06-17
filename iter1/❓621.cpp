//
// Created by chenyufan on 2020/6/16.
//

#include <vector>
#include <map>
#include <iostream>
#include <queue>

using namespace std;

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        auto comp = [](tuple<int, int, char> l, tuple<int,int,char> r) {
            if (get<0>(l) != get<0>(r)) return get<0>(l) < get<0>(r);
            if (get<1>(l) != get<1>(r)) return get<1>(l) > get<1>(r);
            return get<2>(l) < get<2>(r);
        };
        priority_queue<tuple<int, int ,char>, vector<int>, decltype(comp)> q(comp);
        for (auto t : tasks) q.push();
    }
};

int main() {
    Solution s;
    vector<char> v{'A', 'A', 'A', 'B', 'C', 'D', 'E'};
    cout << s.leastInterval(v, 2) << endl;
}

