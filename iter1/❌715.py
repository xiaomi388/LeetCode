# hard!!!
# add: O(n + logn)


import bisect
class RangeModule:

    def __init__(self):
        self.ranges = []

    def getBound(self, left, right):
       i = bisect.bisect_right(self.ranges, (left, float('inf')))
       j = bisect.bisect_right(self.ranges, (right, float('inf')))
       if i-1 >= 0 and self.ranges[i-1][1] >= left:
           i -= 1
       return i, j

    def addRange(self, left, right):
        i, j = self.getBound(left, right)
        begin = min(left, self.ranges[i][0] if i < len(self.ranges) else float('inf'))
        end = max(right, self.ranges[j-1][1] if j-1 >= 0 else 0)
        del self.ranges[i:j]
        self.ranges.insert(i, (begin, end))

    def removeRange(self, left, right):
        i, j = self.getBound(left, right)
        begin = min(left, self.ranges[i][0] if i < len(self.ranges) else float('inf'))
        end = max(right, self.ranges[j-1][1] if j-1 >= 0 else 0)
        del self.ranges[i:j]
        if end > right:
            self.ranges.insert(i, (right, end))
        if begin < left:
            self.ranges.insert(i, (begin, left))


    def queryRange(self, left, right):
        i = bisect.bisect_right(self.ranges, (left, float('inf'))) - 1
        if i >= 0 and self.ranges[i][0] <= left <= right <= self.ranges[i][1]:
            return True
        return False



# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

s = RangeModule()
s.addRange(1, 100)
s.addRange(101, 200)
s.addRange(100, 101)
print(s.ranges)
print(s.queryRange(10, 20))
print(s.queryRange(199, 200))
