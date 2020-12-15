class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def dfs(remain, i, nums):
            if remain == 0 and len(nums) == k: ans.append(nums)
            elif len(nums) >= k or remain < 0 or i >= 10: return
            else:
                dfs(remain, i+1, nums)
                nums.append(i)
                dfs(remain-i, i+1, nums)
                nums.pop()
        dfs(n, 1, [])
        return ans
