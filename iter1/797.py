from functools import lru_cache
import copy

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def dfs(v, path):
            if v == len(graph)-1:
                ans.append(copy.copy(path))
                return

            for nbr in graph[v]:
                path.append(nbr)
                dfs(path)
                path.pop()

        return dfs(0, [])








