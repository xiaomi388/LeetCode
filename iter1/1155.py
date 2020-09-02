# dp即可。套路：观察d f t的数量级，可以发现三层循环不会超时
# 注意点是dp数组的创建方式，内层表示列数，外层表示行数

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0] * (target+1) for i in range(d+1)]

        for i in range(1, target+1):
            dp[1][i] = 1 if i <= f else 0

        for i in range(2, d+1):
            for q in range(2, target+1):
                for x in range(1, f+1):
                    if q-x > 0:
                        dp[i][q] += dp[i-1][q-x]
        return dp[d][target] % (pow(10, 9) + 7)







