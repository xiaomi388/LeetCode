class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, prefix = 0, []
        for i in range(len(intervals)):
            if newInterval[1] >= intervals[i][1] >= newInterval[0] >= intervals[i][0]:
                newInterval = (intervals[i][0], newInterval[1])
            elif intervals[i][1] >= newInterval[1] >= intervals[i][0] >= newInterval[0]:
                newInterval = (newInterval[0], intervals[i][1])
            elif newInterval[1] >= intervals[i][1] >= intervals[i][0] >= newInterval[0]:
                continue
            elif intervals[i][1] >= newInterval[1] >= newInterval[0] >= intervals[i][0]:
                newInterval = intervals[i]
            elif newInterval[1] >= newInterval[0] >= intervals[i][1] >= intervals[i][0]:
                prefix.append(intervals[i])
            elif intervals[i][1] >= intervals[i][0] >= newInterval[1] >= newInterval[0]:
                break
        else:
            i += 1
        return prefix + [newInterval] + intervals[i:]
