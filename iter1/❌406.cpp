class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), [](const vector<int>& a, const vector<int>& b){
            if (a[0] < b[0]) return true;
            return a[1] < b[1];
        });
        people[0].push_back(0);
        for (int i = 1; i < people.size(); ++i) {
            if (people[i][0] == people[i-1][0]) people[i].push_back(people[i-1][2]+1);
            else people[i].push_back(0);
        }

        vector<vector<int>> res(people.size());
        int cur = 0;
        for (int i = 0; i < people.size(); ++i) {
            if (people[i][1] == people[i][2]) {
                res[cur] = {people[i][0], people[i][1]};
                do ++cur; while (!res[cur].empty());
            } else {
                int cnt = people[i][1]-people[i][2];
                int idx = cur;
                while (cnt) {
                    ++idx;
                    if (res[idx].empty()) --cnt;
                }
                res[idx] = {people[i][0], people[i][1]};
            }
        }
        return res;
    }
};


// 思路：先从大到小排，然后进行插入。插入时可确保插入的元素一定都比之前插入的小。
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        auto comp = [](const vector<int>& p1, const vector<int>& p2)
        { return p1[0] > p2[0] || (p1[0] == p2[0] && p1[1] < p2[1]); };
        sort(people.begin(), people.end(), comp);
        vector<vector<int>> res;
        for (auto &p : people) {
            cout << p[0] << "," << p[1] << " ";
        }
        cout << endl;
        for (auto& p : people)
            res.insert(res.begin() + p[1], p);
        return res;
    }
};


