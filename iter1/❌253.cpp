// 上下车算法
//

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        vector<int> starts, ends;
        for (auto &m : intervals) {
            starts.push_back(m[0]);
            ends.push_back(m[1]);
        }
        sort(starts.begin(), starts.end()); sort(ends.begin(), ends.end());

        int i = 0, q = 0;
        int ava = 0, total = 0;
        while (i < starts.size() && q < starts.size()) {
            if (starts[i] < ends[q]) {
                if (!ava) { ava++, total++;}
                ava--; i++;
            } else {
                ava++; q++;
            }
        }
        return total;
    }
};

