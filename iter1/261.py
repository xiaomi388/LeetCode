class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        graph = collections.defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def dfs(vex, par):
            if vex in visited:
                return False
            visited.add(vex)

            for next_vex in graph[vex]:
                if next_vex == par:
                    continue
                if not dfs(next_vex, vex):
                    return False
            return True

        if dfs(0, -1) and len(visited) == n:
            return True
        return False
