class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited = set()
        def dfs(i):
            if not 0 <= i < len(M) or i in visited:
                return
            visited.add(i)

            for q in range(len(M)):
                if M[i][q]:
                    dfs(q)

        cnt = 0
        for i in range(len(M)):
            if i in visited:
                continue
            cnt += 1
            dfs(i)
        return cnt
