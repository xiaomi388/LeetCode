//
// Created by 陈语梵 on 2020/8/19.
//

#include <iostream>
#include <vector>

using namespace std;

void merge(vector<int> &left, vector<int> &right, vector<int>& nums) {
    int i = 0, j = 0, p = 0;
    while (i < left.size() && j < right.size()) {
        nums[p++] = left[i] < right[j] ? left[i++] : right[j++];
    }
    while (i < left.size()) nums[p++] = left[i++];
    while (j < right.size()) nums[p++] = right[j++];
}


void mergeSort(vector<int>& nums) {
    if (nums.size() < 2) return ;
    int mid = nums.size() / 2;
    vector<int> left(nums.begin(), nums.begin()+mid);
    vector<int> right(nums.begin()+mid, nums.end());
    mergeSort(left); mergeSort(right);
    merge(left, right, nums);
}

int main() {
//    vector<int> a{1, 1, 1, 8, 5, 10, 9, 4};
    vector<int> a{1};
    mergeSort(a);
    for (auto i : a) cout << i << " "; cout << endl;
}


