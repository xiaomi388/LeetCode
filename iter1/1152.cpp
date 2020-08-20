//
// Created by 陈语梵 on 2020/8/19.
//


struct LogEntry {
    string *username;
    int *timestamp;
    string *website;
};

class Solution {
public:
    vector<string> mostVisitedPattern(vector<string>& username, vector<int>& timestamp, vector<string>& website) {
        // username to logs
        unordered_map<string, vector<LogEntry>> logEntries;

        for (int i = 0; i < username.size(); ++i) {
            logEntries[username[i]].push_back(LogEntry{
                    .username = &username[i],
                    .timestamp = &timestamp[i],
                    .website = &website[i]
            });
        }

        for (auto &p : logEntries) {
            sort(p.second.begin(), p.second.end(), [](LogEntry& a, LogEntry &b) {
                return *a.timestamp < *b.timestamp;
            });
        }

        map<vector<string>, int> cnt;
        for (auto &p : logEntries) {
            auto &username = p.first;
            auto &entries = p.second;

            set<vector<string>> picked;
            for (int i = 0; i < entries.size(); ++i) {
                for (int q = i+1; q < entries.size(); ++q) {
                    for (int j = q+1; j < entries.size(); ++j) {
                        if (picked.find({*entries[i].website, *entries[q].website, *entries[j].website})) continue;
                        picked.insert({*entries[i].website, *entries[q].website, *entries[j].website});
                        cnt[{*entries[i].website, *entries[q].website, *entries[j].website}]++;
                    }
                }
            }
        }

        auto maxIt = cnt.begin();
        for (auto it = cnt.begin(); it != cnt.end(); ++it) {
            if ((*maxIt).second < (*it).second) maxIt = it;
        }
        return (*maxIt).first;
    }
};


