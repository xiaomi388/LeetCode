//
// Created by 陈语梵 on 2020/8/19.
//

#include <iostream>
#include <vector>

using namespace std;

void insertionSort(vector<int>& nums) {
    for (int i = 1; i < nums.size(); ++i) {
        for (int j = i; j > 0; --j) {
            if (nums[j] < nums[j-1]) swap(nums[j], nums[j-1]);
            else break;
        }
    }
}

int main() {
    vector<int> a{1, 10, 5, 9, 3, 0};
    insertionSort(a);
    for (auto i : a) cout << i << " "; cout << endl;
}


