// trajan算法
// https://leetcode.com/problems/critical-connections-in-a-network/discuss/382638/DFS-detailed-explanation-O(orEor)-solution


class Solution {
public:
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        unordered_map<int, vector<int>> graph;
        for (auto& edge : connections) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        unordered_map<int, int> rankOf;
        for (int i = 0; i < n; ++i) rankOf[i] = -1;

        vector<vector<int>> ret;
        dfs(0, -1, 0, ret, rankOf, graph);

        return ret;
    }

    void dfs(int v, int par, int lvl, vector<vector<int>> &ret,
             unordered_map<int,int> &rankOf, unordered_map<int, vector<int>>& graph) {
        rankOf[v] = lvl;
        for (auto child : graph[v]) {
            if (child == par) continue ;
            if (rankOf[child] == -1) dfs(child, v, lvl+1, ret, rankOf, graph);
            rankOf[v] = min(rankOf[v], rankOf[child]);
        }

        if (v != 0 && rankOf[v] == lvl) {
            ret.push_back({par, v});
        }
        return ;
    }
};
