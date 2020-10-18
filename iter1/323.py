class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        p = [i for i in range(n)]
        def union(x, y):
            p[find(y)] = p[find(x)]

        def find(x):
            if p[x] == x: return x
            p[x] = find(p[x])
            return p[x]

        for x, y in edges: union(x, y)
        return sum([1 for i, v in enumerate(p) if i == v])
