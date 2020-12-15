class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def dfs(picked, left):
            if not left:
                ans.add(tuple(picked))
                return
            for i in range(len(left)):
                # optimization
                if i > 0 and left[i-1] == left[i]: continue
                dfs(picked + [left[i]], left[:i]+left[i+1:])

        # optimization
        nums.sort()

        dfs(list(), nums)
        return list(ans)

