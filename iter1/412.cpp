//
// Created by 陈语梵 on 2020/7/30.
//


class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> ret;
        for (int i = 1; i < n; ++i) {
            if (n % 3 == 0 && n % 5 == 0) ret.push_back("FizzBuzz");
            else if (n % 3 == 0) ret.push_back("Fizz");
            else if (n % 5 == 0) ret.push_back("Buzz");
            else ret.push_back(to_string(i));
        }
        return ret;
    }
};