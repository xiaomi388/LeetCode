#include <string>
#include <unordered_set>
#include <iostream>

using namespace std;

class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        for (int i = 1; i < s.length(); ++i) {
            if (_repeatedSubstringPattern(s, i)) return true;
        }
        return false;
    }

    bool _repeatedSubstringPattern(string& s, int l) {
        if (l >= s.size()) return true;
        string sub = s.substr(0, l);

        int i = l;
        while (i < s.length()) {
            if (s.length() - i < l) return false;
            string nextSub = s.substr(i, l);
            if (nextSub != sub) return false;
            i += l;
        }
        return true;
    }
};

int main() {
    Solution s;
    auto res = s.repeatedSubstringPattern("abcabcabcabc");
    cout << res << endl;

}