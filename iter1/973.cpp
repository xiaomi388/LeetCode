//
// Created by 陈语梵 on 2020/8/19.
//

#define distOf(A) A[0]*A[0]+A[1]*A[1]

class Solution {
public:
    int partition(vector<vector<int>>& points, int lo, int hi) {
        int pivot = distOf(points[lo]);
        int i = lo, j = hi;
        while (i < j) {
            do ++i; while (i < hi && distOf(points[i]) <= pivot);
            do --j; while (j > lo && distOf(points[j]) > pivot);
            if (i < j) swap(points[i], points[j]);
        }
        swap(points[lo], points[j]);
        return j;
    }

    void qksort(vector<vector<int>>& points, int K, int lo, int hi) {
        if (K <= 0) return ;
        int mid = partition(points, lo, hi);
        if (K > mid-lo+1) qksort(points, K-(mid-lo+1), mid+1, hi);
        else if (K < mid-lo+1) qksort(points, K, lo, mid);
    }

    vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
        qksort(points, K, 0, points.size());
        return vector<vector<int>>(points.begin(), points.begin()+K);
    }
};

