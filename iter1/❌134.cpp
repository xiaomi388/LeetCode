// 贪心题，

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int preReq = 0;
        int gain = 0;
        int size = gas.size();
        int startPos = 0;
        for (int i = 0; i < size; ++i) {
            gain = gain + gas[i] - cost[i];
            if (gain < 0) {
                startPos = i + 1;
                preReq = preReq + gain;
                gain = 0;
            }
        }
        if (gain + preReq < 0 || startPos == size) return -1;
        return startPos;
    }
};

int main() {
    Solution s;
    vector<int> gas = {3,3,4};
    vector<int> cost = {3,4,4};
    cout << s.canCompleteCircuit(gas, cost) << endl;
}
