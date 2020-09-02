class Solution:
    def nextClosestTime(self, time: str) -> str:
        def isValid(self, time):
            return 0 <= int(time[:2]) < 24 and 0 <= int(time[3:]) < 60

        nums = [n for n in time if n != ":"]
        ret = "99:99"
        for i in nums:
            for q in nums:
                for x in nums:
                    for y in nums:
                        nextTime = "{}{}:{}{}".format(i, q, x, y)
                        if not isValid(nums): continue
                        if ret > nextTime > time: ret = nextTime
                        elif ret < time and nextTime > time: ret = nextTime
                        elif nextTime < ret < time: ret = nextTime
        return ret


