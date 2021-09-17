'''

Approach 1: dfs + backtrack, O(3^n*n), O(n)
    input: n = 2
    AA...

Approach 2: dp1, dp2, dp3
    dp[i][j][k] = possible number of valid i records that has j A and ends with k L
        j < 2, k < 3

    dp[1][0][0] = P = 1
    dp[1][1][0] = A = 1
    dp[1][0][1] = L = 1
    dp[1][..][..] = 0

    dp[2][0][0] = dp[1][0][0|1|2] * "P"
    dp[2][0][1] = dp[1][0][0] * "L"
    dp[2][0][2] = dp[1][0][1] * "L"

    dp[2][1][0] = (dp[1][0][0|1|2] * "A") + (dp[1][1][0|1|2] * "P")
    dp[2][1][1] = dp[1][1][0] * "L"
    dp[2][1][2] = dp[1][1][1] * "L"
'''

class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 1: return 3

        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n)]
        dp[0][0][0] = 1
        dp[0][1][0] = 1
        dp[0][0][1] = 1

        for i in range(1, n):
            dp[i][0][0] = (dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][0][2]) % (10**9+7)
            dp[i][0][1] = dp[i-1][0][0]
            dp[i][0][2] = dp[i-1][0][1]
            dp[i][1][0] = (dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][0][2] + dp[i-1][1][0] + dp[i-1][1][1] + dp[i-1][1][2]) % (10**9+7)
            dp[i][1][1] = dp[i-1][1][0]
            dp[i][1][2] = dp[i-1][1][1]
        return (dp[n-1][0][0] + dp[n-1][1][0] + dp[n-1][1][1] + dp[n-1][1][2] + dp[n-1][0][1] + dp[n-1][0][2]) % (10**9 + 7)
