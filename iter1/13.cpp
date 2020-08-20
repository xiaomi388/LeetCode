//
// Created by 陈语梵 on 2020/8/20.
//

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<string, int> dict{
                {"I", 1}, {"V", 5}, {"X", 10}, {"L", 50},
                {"C", 100}, {"D", 500}, {"M", 1000}, {"IV", 4},
                {"IX", 9}, {"XL", 40}, {"XC", 90}, {"CD", 400},
                {"CM", 900}};

        int i = 0;
        int sum = 0;
        while (i < s.length()) {
            if (i == s.length() - 1) {
                sum += dict[s.substr(i, 1)];
                break;
            } else if (dict.find(s.substr(i, 2)) != dict.end()) {
                sum += dict[s.substr(i, 2)];
            } else {
                sum += dict[s.substr(i, 1)];
            }
        }
        return sum;
    }
};

