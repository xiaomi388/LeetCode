// 算前后间隔时，要遵循左闭右开原则

#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <cstdlib>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<int, int> char2pos;
        int maxLen = 0;
        int left = 0;
        int i = 0;
        for (; i < s.length(); ++i) {
            maxLen = max(maxLen, i - left);

            if (char2pos.find(s[i]) != char2pos.end()) {
                left = max(char2pos[s[i]]+1, left);
            }
            char2pos[s[i]] = i;
        }


        return max(maxLen, i - left);
    }
};

int main() {
    Solution s;
    cout << s.lengthOfLongestSubstring("abcabcbb") << endl;

}