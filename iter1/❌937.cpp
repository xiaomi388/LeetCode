//
// Created by 陈语梵 on 2020/8/18.
//
// 难点：要用stable_sort，才能保证数字log的顺序保持一致！
//comp - comparison function which returns ​true if the first argument is less than
// the second. The signature of the comparison function should be equivalent to the
// following: bool cmp(const Type1 &a, const Type2 &b);


bool comp(const string& a, const string &b) {
    int aPos = a.find(" "), bPos = b.find(" ");
    bool lf = a[aPos+1] < 'a', rf = b[bPos+1] < 'a';
    if (lf && rf) return false;
    else if (!lf && rf) return true;
    else if (lf && !rf) return false;

    int cmp = a.compare(aPos+1, -1, b, bPos+1, -1);
    if (cmp == 0) return a.compare(0, aPos, b, 0, bPos) < 0;
    return cmp < 0;
}

class Solution {
public:
    vector<string> reorderLogFiles(vector<string>& logs) {
        stable_sort(logs.begin(), logs.end(), comp);
        return logs;
    }
};



