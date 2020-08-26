//
// Created by 陈语梵 on 2020/8/23.
//

class Solution {
public:
    int twoSumLessThanK(vector<int>& A, int K) {
        sort(A.begin(), A.end());
        int i = 0, j = A.size()-1;
        int ret = -1;
        while (i < j) {
            if (A[i] + A[j] < K) {
                ret = max(ret, A[i] + A[j]);
                i++;
            } else {
                j--;
            }
        }
        return ret;
    }
};
