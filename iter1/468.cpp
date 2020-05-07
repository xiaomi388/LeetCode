//
// Created by chenyufan on 2020/5/7.
//

#include <string>
#include <iostream>
#include <unordered_set>

using namespace std;

class Solution {
public:
    string validIPAddress(string IP) {
        string res;
        if ((res = _validIP4Address(IP)) == "Neither") {
            res = _validIP6Address(IP);
        }
        return res;
    }

    string _validIP4Address(string IP) {
        IP.append(".");
        int dotCnt = 0;
        int lastPos = -1;
        int pos;
        while ((pos = IP.find('.', lastPos+1)) != -1) {
            string numStr = IP.substr(lastPos+1, pos - lastPos - 1);
//            cout << numStr << endl;
            if (numStr.length() > 3 || numStr.length() <= 0) return "Neither";
            if (!(numStr.length() == 1 && IP[lastPos+1] == '0')) {
                bool headIsZero = true;
                for (int i = lastPos+1; i < pos; ++i) {
                    if (IP[i] > '0' && IP[i] <= '9') headIsZero = false;
                    else if (IP[i] == '0' && headIsZero) return "Neither";
                    else if (IP[i] < '0' || IP[i] > '9') return "Neither";
                }
            }
            if (stoi(numStr) > 255) return "Neither";
            dotCnt++;
            lastPos = pos;
        }
        if (dotCnt != 4) return "Neither";
        return "IPv4";
    }

    string _validIP6Address(string IP) {
        IP.append(":");
        int dotCnt = 0;
        int lastPos = -1;
        int pos;
        while ((pos = IP.find(':', lastPos+1)) != -1) {
            if ((pos - lastPos - 1 > 4) || (pos == lastPos + 1)) return "Neither";
//            cout << IP.substr(lastPos+1, pos - lastPos - 1) << endl;
            for (int i = lastPos+1; i < pos; ++i) {
                if (
                    (IP[i] >= '0' && IP[i] <= '9') || (IP[i] >= 'a' && IP[i] <= 'f') ||\
                    (IP[i] >= 'A' && IP[i] <= 'F')
                ) continue;
                else return "Neither";
            }
            dotCnt++;
            lastPos = pos;
        }
        if (dotCnt != 8) return "Neither";
        return "IPv6";
    }
};

int main() {
    Solution s;
    cout << s.validIPAddress("192.0.0.1") << endl;

}
