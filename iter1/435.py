class Solution:
	def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
		intervals.sort(key=lambda x: x[0])
		ans = 0
		if not intervals:
			return ans
		last_end = intervals[0][1]
		for interval in intervals[1:]:
			if last_end > interval[0]:
				ans += 1
				if last_end > interval[1]:
					last_end = interval[1]
			else:
				last_end = interval[1]
		return ans
