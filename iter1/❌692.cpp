// TopK题解法：维护一个总长度为k的小根堆，然后按顺序插入元素。当元素超过k时，把最小那个弹出即可。
// heap的插入: logk; 弹出: logk 所以最后的复杂度是nlogk


unordered_map<string, cnt> dict;
struct cmp {
    operator () (const string& a, const string &b) {
        return dict[a] != dict[b] ? dict[a] < dict[b] : a > b;
    }
};

class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        for (auto &word : words) dict[word]++;
        priority_queue<string, vector<string>, cmp> q;
        for (auto &word : words) {
            q.push(word);
            if (q.size() > k) q.pop();
        }
        vector<string> ret(q.size());
        for (int i = q.size()-1; i >= 0; --i) {
            ret[i] = q.top();
            q.pop();
        }
        return ret;
    }
};

