# https://leetcode.com/discuss/interview-question/350233/Google-or-Summer-Intern-OA-2019-or-Decreasing-Subsequences

class Solution:
    def DecreasingSubsequences(self, nums):
        tails = []
        for num in nums:
            i = bisect.bisect(tails, num)
            if i == len(tails):
                tails.append(num)
            else:
                tails[i] = num
        return len(tails)





