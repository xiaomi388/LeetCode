class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def dfs(end, invalid):
            if end == -1: return 0
            ans = 0
            if all([len(set(arr[end])) == len(arr[end])] + [c not in invalid for c in arr[end]]):
                ans = dfs(end-1, invalid.union(arr[end])) + len(arr[end])
            ans = max(dfs(end-1, invalid), ans)
            return ans
        return dfs(len(arr)-1, set())

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for a in arr:
            if len(set(a)) < len(a): continue
            a = set(a)
            for c in dp[:]:
                if a & c: continue
                dp.append(a | c)
        print(dp)
        return max(len(a) for a in dp)