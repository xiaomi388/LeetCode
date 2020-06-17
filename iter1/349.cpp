//
// Created by chenyufan on 2020/6/8.
//

#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    string decodeString(string s) {
        int pos = 0;
        return _decodeString(s, pos);
    }

    string _decodeString(string &s, int& p) {
        if (p >= s.length()) return "";
        string ret;
        for (;p < s.length();++p) {
            if (s[p] == ']') return ret;
            else if (s[p] >= '0' && s[p] <= '9') {
                // parse int
                int num = s[p] - '0';
                while (s[++p] != '[') {
                    num *= 10;
                    num += s[p] - '0';
                }
                auto res = _decodeString(s, ++p);
                while (num--) ret += res;
            } else {
                ret.push_back(s[p]);
            }
        }
        return ret;
    }
};

int main() {
    Solution s;
    auto r = s.decodeString("abc3[cd]xyz");
    cout << r << endl;

}
