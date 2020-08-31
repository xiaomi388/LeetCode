# 先转化成分钟制，然后将最早的时间+1440，排序后比较出间隔最小的即可

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440 or len(timePoints) == 0:
            return 0
        tvs = []
        for timePoint in timePoints:
            t = timePoint.split(":")
            tv = int(t[0])*60 + int(t[1])
            tvs.append(tv)
        tvs.sort()
        tvs.append(tvs[0]+1440)
        ret = float('inf')
        for i in range(len(tvs)-1):
            ret = min(ret, tvs[i+1]-tvs[i])
        return ret






