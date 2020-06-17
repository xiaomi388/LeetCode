// 滑动窗口法。比较是否相同的方法是建立两个数组（桶），然后看string桶里元素 == pattern桶
//

#include <vector>
#include <string>
#include <bitset>

using namespace std;

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> pv(26), sv(26);
        vector<int> ret;
        for (int i = 0; i < p.size(); ++i) {
            ++pv[p[i]-'a'];
            ++sv[s[i]-'a'];
        }
        if (pv == sv) ret.push_back(0);
        for (int i = p.size(); i < s.size(); ++i) {
            ++sv[s[i]-'a'];
            --sv[s[i-p.size()]-'a'];
            if (pv == sv) ret.push_back(i-p.size()+1);
        }
        return ret;
    }
};