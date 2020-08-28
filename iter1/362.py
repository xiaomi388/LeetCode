class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = []
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.hits.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        def _binSearch(timestamp: int, lower: bool) -> int:
            lo = 0; hi = len(self.hits)
            while lo < hi:
                mid = int((lo + hi) / 2)
                if (self.hits[mid] < timestamp 
                        if lower else self.hits[mid] <= timestamp):
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        l = _binSearch(timestamp-299, True)
        r = _binSearch(timestamp, False)
        return r - l





# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
