# BFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        in_degrees = [0] * numCourses
        for x, y in prerequisites:
            graph[y].add(x)
            in_degrees[x] += 1
        q = collections.deque([x for x in range(numCourses) if in_degrees[x] == 0])
        ans = []
        while len(q):
            x = q.popleft()
            ans.append(x)
            for y in graph[x]:
                in_degrees[y] -= 1
                if in_degrees[y] == 0:
                    q.append(y)
        return ans if len(ans) == numCourses else []

# DFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        in_degrees = [0] * numCourses
        seen = set()
        for x, y in prerequisites:
            graph[y].add(x)
            in_degrees[x] += 1
        ans = []
        for x in range(numCourses):
            if x in seen: continue
            def dfs(x, path):
                seen.add(x)
                for y in graph[x]:
                    if y in path:
                        raise
                    if not y in seen:
                        path.add(x)
                        dfs(y, path)
                        path.discard(x)
                ans.append(x)
            if in_degrees[x] == 0:
                try:
                    dfs(x, set())
                except:
                    return []
        return ans[::-1] if len(ans) == numCourses else []





