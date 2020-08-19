//
// Created by 陈语梵 on 2020/7/30.
//

class Solution {
public:
    void reverseString(vector<char>& s) {
        int l = 0, r = s.length()-1;
        while (l < r) swap(s[l++], s[r--]);
    }
};