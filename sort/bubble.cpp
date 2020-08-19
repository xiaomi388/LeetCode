//
// Created by 陈语梵 on 2020/8/19.
//

#include <iostream>
#include <vector>

using namespace std;

void bubbleSort(vector<int>& nums) {
    for (int i = int(nums.size())-1; i > 0; --i) {
        for (int j = 0; j < i; ++j) {
            if (nums[j] > nums[j+1]) swap(nums[j], nums[j+1]);
        }
    }
}

int main() {
    vector<int> a{1, 1, 1};
    bubbleSort(a);
    for (auto i : a) cout << i << " "; cout << endl;
}

