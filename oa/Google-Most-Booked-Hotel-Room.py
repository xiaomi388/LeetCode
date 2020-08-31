# https://leetcode.com/discuss/interview-question/421787/
from collections import Counter

class Solution:
    def MostBookedHetelRoom(self, events):
        return sorted(Counter(events).most_common(), key=lambda x: (-x[1], x[0]))[0][0][1:]

s = Solution()
print(s.MostBookedHetelRoom(["+3E", "+1A", "-1A", "+4F", "+1A", "-3E", "+3E"]))

