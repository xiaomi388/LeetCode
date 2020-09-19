# 暴力记忆化搜索
# 1. lru_cache 的返回值最好不要是指针，是的话得确保返回值不会被篡改
# 2. min max可以指定key，简化代码
# 3. 注意命名不要重叠，命名重复时debug很难，所以命名要规范
from functools import lru_cache
class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str],
                    targetPath: List[str]) -> List[int]:
        m = {it[0]: it[1] for it in enumerate(names)}
        d = collections.defaultdict(list)
        for road in roads:
            d[road[0]].append(road[1])
            d[road[1]].append(road[0])

        @lru_cache(None)
        def dfs(i, node):
            if i == len(targetPath)-1:
                return 1 if m[node] != targetPath[i] else 0, [node]
            next, path = min([dfs(i+1, child) for child in d[node]],
                             key=lambda x : x[0])
            if path is None:
                return next, path
            return next + (1 if m[node] != targetPath[i] else 0), list([node]+path)
        return min([dfs(0, i) for i in range(len(names))], key=lambda x : x[0])[1]


