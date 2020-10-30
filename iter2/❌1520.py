class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        d = collections.defaultdict(lambda : (float('inf'), float('-inf')))
        for i, c in enumerate(s):
            d[c] = (min(d[c][0], i), max(d[c][1], i))

        ans = []
        for i, c in enumerate(s):
            if i == d[s[i]][0]:

                right = d[s[i]][1]
                for q in range(d[c][0], d[c][1]+1):
                    if d[q][1] < i:
                        break
                    right = max(right, d[q][1])
                else:
                    ans.append(s[i:right+1])
        return ans







        intervals = set()
        for c in d:
            start, end = d[c]
            new_range = d[c]
            for i in range(start, end+1):
                new_range = (min(d[i][0], start), max(d[i][1], end))
            d[c] = new_range

        intervals = sorted(list(intervals), key=lambda x : (x[1], x[0]))

        ans, last_end = [], 0
        for start, end in intervals:
            if start >= last_end:
                ans.append(s[start:end+1])
                last_end = end
        return ans


