//
// Created by 陈语梵 on 2020/7/28.
//

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int _max = 0;
        int cur_min_val = INT_MAX;
        for (int i = 0; i < prices.size(); ++i) {
            if (prices[i] < cur_min_val) cur_min_val = prices[i];
            else _max = max(_max, prices[i] - cur_min_val);
        }
        return _max;
    }
};

