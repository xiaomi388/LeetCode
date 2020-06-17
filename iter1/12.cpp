//
// Created by chenyufan on 2020/5/25.
//

#include <iostream>
#include <string>
#include <map>

using namespace std;

class Solution {
    map<int, string> dict{
            {1, "I"}, {4, "IV"}, {5, "V"}, {9, "IX"}, {10, "X"},
            {40, "XL"}, {50, "L"}, {90, "XC"}, {100, "C"},
            {400, "CD"}, {500, "D"}, {900, "CM"}, {1000, "M"},
    };
public:
    string intToRoman(int num) {
        if (num == 0) return "";
        for (auto i : {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}) {
            if (i <= num) return dict[i] + intToRoman(num - i);
        }
        return "";
    }
};

int main() {
    Solution s;
    cout << s.intToRoman(1994) << endl;
}
