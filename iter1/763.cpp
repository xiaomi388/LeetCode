//
// Created by 陈语梵 on 2020/8/20.
//

class Solution {
public:
    vector<int> partitionLabels(string S) {
        unordered_map<char, int> lastPosOf;
        for (int i = 0; i < S.length(); ++i) {
            lastPosOf[s[i]] = i;
        }

        vector<int> ret;
        int i = 0, q = 0;
        while (i < S.length()) {
            do {
                q = lastPosOf[s[i]];
            } while (i++ < q);
            ret.push_back(i);
        }
    }
};


