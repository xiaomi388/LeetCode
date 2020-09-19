# 相关问题：76
# 问题总结：https://leetcode-cn.com/problems/minimum-window-subsequence/solution/hua-dong-chuang-kou-ti-mu-hui-zong-by-miaomiao-2-2/

# brute force: 遍历S,遍历到T的最后一个字母后，再往前遍历找到第一个字母，取该串。
# 然后从第一个字母后面开始继续遍历。

# 方法一：前缀递归：dp[i][q]的含义是若S的第i位对应T的第q位，那么第i-1位对应的位置是哪里
# O(NK)
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        cur = [i if x == T[0] else None for i, x in enumerate(S)]

        for j in range(1, len(T)):
            last = None
            new = [None] * len(S)
            for i, u in enumerate(S):
                if last is not None and u == T[j]: new[i] = last
                if cur[i] is not None: last = cur[i]
            cur = new
        ans = 0, len(S)
        for e, s in enumerate(cur):
            if s is not None and e - s < ans[1] - ans[0]:
                ans = s, e
        return S[ans[0]: ans[1]+1] if ans[1] < len(S) else ""














