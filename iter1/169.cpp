// 有更好的做法：其实我们只要知道谁最大就好了
// 摩尔投票法 https://www.zhihu.com/question/49973163/answer/235921864
// 核心就是对拼消耗。玩一个诸侯争霸的游戏，假设你方人口超过总人口一半以上，并且能保证每个人口出去干仗都能一对一同归于尽。
// 最后还有人活下来的国家就是胜利。那就大混战呗，最差所有人都联合起来对付你（对应你每次选择作为计数器的数都是众数），
// 或者其他国家也会相互攻击（会选择其他数作为计数器的数），但是只要你们不要内斗，最后肯定你赢。最后能剩下的必定是自己人。
//

#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> num_cnt;
        pair<int, int> max_num_cnt;
        for (int & num : nums) {
            auto it = num_cnt.find(num);
            if (it == num_cnt.end()) num_cnt[num] = 0;
            num_cnt[num]++;
            if (num_cnt[num] > max_num_cnt.second) {
                max_num_cnt = {num, num_cnt[num]};
            }
        }
        return max_num_cnt.first;
    }
};

int main() {
    Solution s;
    vector<int> nums{3,2,3};
    cout << s.majorityElement(nums) << endl;

}
