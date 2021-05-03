class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        pre_sum, suf_sum = [0], [0]
        for i in range(len(cardPoints)):
            pre_sum.append(pre_sum[-1]+cardPoints[i])
            suf_sum.append(suf_sum[-1]+cardPoints[len(cardPoints)-i-1])
        max_ = 0
        for i in range(k+1):
            max_ = max(max_, pre_sum[i] + suf_sum[k-i])
        return max_

