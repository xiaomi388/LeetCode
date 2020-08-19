// 思路：先找到所有<k的字母数量，以这些字母为分割点，分割成各个子串，然后对各个子串进行递归查找
//

class Solution {
public:
    int longestSubstring(string s, int k) {
        return _longestSubstring(s, 0, s.length(), k);
    }

    int _longestSubstring(string &s, int begin, int end, int k) {
        //cout << begin << " " << end << endl;
        if (begin >= end) return 0;

        vector<int> dict(26);
        for (int i = begin; i < end; ++i) dict[s[i]-'a']++;

        bool fullString = true;
        for (int i = 0; i < dict.size(); ++i) {
            if (dict[i] && dict[i] < k) {
                fullString = false;
                break;
            }
        }
        if (fullString) return end - begin;

        int res = 0;
        for (int i = begin; i < end; ++i) {
            //cout << i << begin << endl;
            if (dict[s[i]-'a'] && dict[s[i]-'a'] < k) {
                //cout << "split:" << begin << " " << i << endl;
                res = max(res, _longestSubstring(s, begin, i, k));
                begin = i+1;
            }
        }
        res = max(res, _longestSubstring(s, begin, end, k));
        return res;
    }
};

