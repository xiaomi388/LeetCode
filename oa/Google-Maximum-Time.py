# https://leetcode.com/discuss/interview-question/396769/google-oa-2019-maximum-time

class Solution:
    def MaximumTime(self, timePoint):
        ret = ""
        if timePoint[0] == "?":
            ret += "1" if "4" <= timePoint[1] < "?" else "2"
        else:
            ret += timePoint[0]
        if timePoint[1] == "?":
            ret += "3" if ret[0] == "2" else "9"
        else:
            ret += timePoint[1]
        ret += ":"
        ret += timePoint[3] if timePoint[3] != "?" else "5"
        ret += timePoint[4] if timePoint[4] != "?" else "9"
        return ret


s = Solution()
inputs = ["?4:5?", "23:5?", "2?:22", "0?:??", "??:??"]

for i in inputs:
    print(s.MaximumTime(i))
