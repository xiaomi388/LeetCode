# dp: dp[i][j] means the minimum cost of j jobs in i days
# dp[i][q] = min([dp[i][q], dp[i-1][q-x] + max(jobDifficulty[q-x+1:q+1]) for x in range(1, q+1)])

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty): return -1
        dp = [[float('inf') for _ in range(len(jobDifficulty))] for _ in range(d+1)]
        dp[1][0] = jobDifficulty[0]
        for i in range(1, len(jobDifficulty)):
            dp[1][i] = max(dp[1][i-1], jobDifficulty[i])

        for i in range(1, d+1):
            for q in range(len(jobDifficulty)):
                if i > q+1:
                    dp[i][q] = float('inf')
                else:
                    _m = jobDifficulty[q]
                    for x in range(1, q+1):
                        if dp[i-1][q-x] == float('inf'):
                            break
                        _m = max(_m, jobDifficulty[q-x+1])
                        dp[i][q] = min(dp[i][q], dp[i-1][q-x] + _m)
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        jc = len(jobDifficulty)
        if d > jc: return -1
        dp = [[-1 for i in range(jc+1)] for i in range(d+1)]
        dp[1][1] = jobDifficulty[0]

        for i in range(2, jc+1):
            dp[1][i] = max(dp[1][i-1], jobDifficulty[i-1])

        for i in range(2, d+1):
            for j in range(i, jc+1):
                dp[i][j] = dp[i-1][j-1] + jobDifficulty[j-1]
                work = jobDifficulty[j-1]
                for k in range(j-2, i-2, -1):
                    work = max(jobDifficulty[k], work)
                    if dp[i-1][k] + work < dp[i][j]:
                        dp[i][j] = dp[i-1][k] + work
        return dp[d][jc]


