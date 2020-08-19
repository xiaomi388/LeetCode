//
// Created by 陈语梵 on 2020/8/19.
//

#include <vector>
#include <iostream>

using namespace std;

int partition(vector<int> &nums, int lo, int hi) {
    int pivot = nums[lo];
    int i = lo, j = hi;
    while (i < j) {
        do ++i; while (i < hi && nums[i] <= pivot);
        do --j; while (j > lo && nums[j] > pivot);
        if (i < j) swap(nums[i], nums[j]);
    }
    swap(nums[lo], nums[j]);
    return j;
}

void quickSort(vector<int> &nums, int lo, int hi) {
    if (lo < hi) {
        int mid = partition(nums, lo, hi);
        quickSort(nums, lo, mid);
        quickSort(nums, mid+1, hi);
    }
}

int main() {
    vector<int> a{10,8, 1,3, 5, 0};
    quickSort(a, 0, a.size());
    for (auto i : a) cout << i << " ";
    cout << endl;
}

