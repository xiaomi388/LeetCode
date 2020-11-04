"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


# solution 1:
# 1. flatten intervals and sort them by start time.
# 2. scan the intervals, and check if there is gap between the start of the current interval
# and the previous interval which has the latest end time.
# 3. if there is a gap, add it into ret.
# time: O(nlogn), space: O(n)
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        schedules = sorted([int for em in schedule for int in em], key=lambda x: (x.start, x.end))
        #print([(int.start, int.end) for int in schedules])
        ret = []
        last = schedules[0]
        for i in range(1, len(schedules)):
            if schedules[i].start > last.end:
                ret.append(Interval(start=last.end, end=schedules[i].start))
                last = schedules[i]
            elif schedules[i].end > last.end:
                last = schedules[i]
        return ret

