class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> task2cnt;
        priority_queue<pair<int, char>> cnt2task;
        unordered_map<int, vector<char>> checker;

        for (auto t : tasks) task2cnt[t]++;
        for (auto p : task2cnt) cnt2task.push({p.second, p.first});

        int ts = 0;
        while (!task2cnt.empty()) {
            ++ts;
            // cout << "cur time: " << ts << endl;


            // add tasks back from checker
            // cout << "checking frozened tasks: ";
            for (auto task : checker[ts]) {
                if (task2cnt[task] != 0) {
                    //cout << "unfreeze task" << task << " ";
                    cnt2task.push({task2cnt[task], task});
                } else {
                    task2cnt.erase(task);
                }
            }
            //cout << endl;
            checker[ts].clear();

            if (cnt2task.empty()) continue;

            // do one task
            auto ct = cnt2task.top();
            cnt2task.pop();

            char task = ct.second;
            //cout << "choose & freeze task" << task << endl;
            --task2cnt[task];
            if (task2cnt[task] == 0) task2cnt.erase(task);
            checker[ts+n+1].push_back(task);



            //for (auto p : task2cnt) cout << "task" << p.first << ":" << p.second << " ";
            //cout << endl;
            //cout << "----------" << endl;
        }
        return ts;
    }
};


// 巧妙方法：拿最长的任务组，以冷却时间为间隔为一组任务组
// https://www.youtube.com/watch?v=YCD_iYxyXoo
// 特殊case：当tasks类数 > 冷却间隔，即说明无需idle，那么时间就是总数目。
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char,int>mp;
        int count = 0;
        for(auto e : tasks)
        {
            mp[e]++;
            count = max(count, mp[e]);
        }

        int ans = (count-1)*(n+1);
        for(auto e : mp) if(e.second == count) ans++;
        return max((int)tasks.size(), ans);
    }
};