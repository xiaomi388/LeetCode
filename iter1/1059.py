class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
        print(graph)

        def dfs(cur, path):
            # check if has loop
            if cur in path: return False
            path.add(cur)

            # check if cur node has outgoing edge
            if cur not in graph and cur != destination:
                return False

            for child in graph[cur]:
                if not dfs(child, path): return False
            path.discard(cur)
            return True

        return dfs(source, set())

