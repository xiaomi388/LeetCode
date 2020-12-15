class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(remain, nums, i):
            if remain == 0:
                ans.append(nums)
                return
            if remain < 0: return
            if i >= len(candidates): return
            for q in range(0, (candidates[i] // remain)+1):
                dfs(remain-candidates[i]*q, nums+[candidates[i]]*q, i+1)
        dfs(target, [], 0)
        return ans


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        # pick zero or unlimited of candidates[i]
        def dfs(s, used, remain):
            for i in range(s, len(candidates)):
                c = candidates[i]
                if c == remain:
                    ans.append(used + [c])
                elif c < remain:
                    dfs(i, used+[c], remain-c)
                elif c > remain:
                    return
        dfs(0, [], target)
        # print(ans)
        return ans





