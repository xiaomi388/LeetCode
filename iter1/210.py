class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cnt = 0
        ret = []

        graph = collections.defaultdict(list)
        for edge in prerequisites:
            graph[edge[0]].append(edge[1])

        q = [(len(graph[i]), i) for i in numCourses]
        while len(q):
            



