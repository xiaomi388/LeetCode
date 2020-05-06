//
// Created by chenyufan on 2020/4/21.
//

#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

class NumArray {
    vector<vector<int>> tree;
    int size;

public:
    NumArray(vector<int>& nums) {
        size = nums.size();
        tree.push_back(nums);

        int l = 1;
        while (tree[l-1].size()) {
            if (tree.size() <= l) tree.push_back(vector<int>(nums.));
            int idx = 0;
            for (int i = 0; i < tree[l-1].size() / 2; ++i) {
                tree[l][idx] = tree[l-1][idx*2];
                if (idx*2 + 1 < tree[l-1].size()) tree[l][idx] += tree[l-1][idx*2+1];
            }
            l++;
        }
    }

    void update(int i, int val) {
        int l = 0, idx = i;
        do {
            tree[l][idx] += val - tree[l][idx];
            l++;
            idx /= 2;
        } while(idx > 0);
    }

    int sumRange(int i, int j) {
        // get common ancestor
        int l = 0, lidx = i, ridx = j;
        while (lidx != ridx) {
            l++;
            lidx /= 2;
            ridx /= 2;
        }
        int res = tree[l][lidx];
        if (i%2 && i-1>=0) {
            res -= tree[0][i-1];
        }
        if (j%2 == 0 && j+1 < tree[0].size()) {
            res -= tree[0][j+1];
        }
        return res;
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(i,val);
 * int param_2 = obj->sumRange(i,j);
 */

int main() {
    vector<int> v{1,3,5};
    NumArray *obj = new NumArray(v);
    cout << obj->sumRange(0, 2) << endl;
    obj->update(1, 2);
    cout << obj->sumRange(0, 2) << endl;
}
