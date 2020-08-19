//
// Created by 陈语梵 on 2020/8/19.
//

#include <iostream>
#include <vector>

using namespace std;

void selectionSort(vector<int>& nums) {
    for (int i = 0; i < nums.size(); ++i) {
        int minPos = i;
        for (int j = i + 1; j < nums.size(); ++j) {
            if (nums[j] < nums[minPos]) {
                minPos = j;
            }
        }
        swap(nums[i], nums[minPos]);
    }
}

int main() {
    vector<int> a{1, 1, 1, 8, 5, 10, 9, 4};
    selectionSort(a);
    for (auto i : a) cout << i << " "; cout << endl;
}

