class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = collections.defaultdict(int)
        for t in time: d[t] += 1
        ans = 0
        for t, cnt in d.items():
            for complement in range((60-t%60)%60, 501, 60):
                if complement == t:
                    ans += (cnt-1)*cnt
                elif complement in d:
                    ans += cnt*d[complement]
        return ans // 2




