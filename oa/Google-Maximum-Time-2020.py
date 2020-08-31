class Solution:
    def MaximumTime(self, timePoint):
        def isValid(timePoint):
            if 0 <= int(timePoint[:2]) < 24 and 0 <= int(timePoint[3:]) < 60:
                return True
            return False
        for i in range(9, -1, -1):
            ret = timePoint.replace("?", str(i))
            if isValid(ret):
                return ret

s = Solution()
inputs = ["??:??", "1?:?2", "0?:2?"]
for i in inputs:
    print(s.MaximumTime(i))

