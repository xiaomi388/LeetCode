class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        def dfs(state, r):
            if r == n:
                ans.append([f"{'.'*c}Q{'.'*(n-c-1)}" for c in state])
                return
            for c in range(n):
                for row, col in enumerate(state):
                    if col == c: break
                    if abs(row-r) == abs(col-c): break
                else:
                    dfs(state + [c], r+1)
        dfs([], 0)
        return ans

