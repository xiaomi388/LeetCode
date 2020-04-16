//
// Created by chenyufan on 2020/4/16.
//

#include <string>
#include <iostream>
#include <unordered_map>
#include <stack>

using namespace std;

int add(const int &a, const int&b) { return a+b; }
int minus(const int &a, const int &b) { return a-b; }
int multiply(const int &a, const int &b) { return a*b; }
int devide(const int &a, const int &b) { return a/b; }

class Solution {
public:
    int getRight(string &s, int curPos) {
        if (s[curPos] != '(') return curPos;
        int leftCnt = 1, rightCnt = 0;

        while (leftCnt != rightCnt) {
            curPos++;
            if (s[curPos] == ')') rightCnt++;
            else if (s[curPos] == '(') leftCnt++;
        }
        return curPos;
    }

    int parseNum(string &s, int curPos, int &res) {
        int i = 0;
        while (s[curPos] >= '0' && s[curPos] <= '9') {
            res = res * 10 + (s[curPos] -  '0');
            i++;
            curPos++;
        }
        curPos--;
        return curPos;
    }


    int calculate(string s) {
        return _calculate(s, 0, s.length());
    }

    int _calculate(string &s, int start, int end) {
        int l = 0, r = 0;
        char op = '+';
        unordered_map<char, function<int(const int&, const int&)>> funcMap{
                {'+', add}, {'-', ::minus}
        };

        for (int i = start; i < end; ++i) {
            if (s[i] == '+' || s[i] == '-') {
                l = funcMap[op](l, r);
                r = 0;
                op = s[i];
            } else if (s[i] == '(') {
                int next = getRight(s, i);
                r = _calculate(s, i+1, next);
                i = next;
            } else if (s[i] >= '0' && s[i] <= '9') {
                i = parseNum(s, i, r);
            } else {
                continue;
            }
        }
        l = funcMap[op](l, r);
        return l;
    }
};

int main() {
    Solution s;
    string exp = "    99  ";
    cout << s.calculate(exp) << endl;

}
