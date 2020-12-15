class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def dfs(i, remain, nums):
            if remain == 0: ans.append(nums)
            elif remain < 0 or i >= len(candidates): return
            else:
                # count how many identical elements we have
                end = i
                while end < len(candidates) and candidates[end] == candidates[i]: end+=1
                # 1 1 1 1: i = 0, end = 3
                cnt = end-i+1
                # dfs from 0 to cnt
                for q in range(0, min(cnt, remain//candidates[i])+1):
                    dfs(end+1, remain-candidates[i]*q, nums + [candidates[i]]*q)
        dfs(0, target,[])



