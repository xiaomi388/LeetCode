//
// Created by 陈语梵 on 2020/8/17.
//

class Solution {
public:
    int hammingDistance(int x, int y) {
        int ret = 0;
        for (int i = 0; i < 32; ++i) {
            if ((x&(1<<i))^(y&(1<<i))) ++ret;
            else --ret;
        }
        return ret;
    }
};

