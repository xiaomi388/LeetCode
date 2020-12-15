# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from functools import lru_cache

# slow
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        @lru_cache(None)
        def find(root, sum):
            if not root: return 0
            ans = 0
            if root.val == sum: ans += 1
            ans += find(root.left, sum-root.val) + find(root.right, sum-root.val)
            return ans

        ans = 0
        def dfs(root):
            if not root: return
            nonlocal ans
            ans += find(root, sum)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ans


# fast
# prefix sum
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        lookup = {0: 1}
        count = 0

        def dfs(root, acc_sum):
            nonlocal count
            if not root: return 0
            acc_sum += root.val
            if acc_sum - sum in lookup:
                count += lookup[acc_sum-sum]
            lookup[acc_sum] = 1 if acc_sum not in lookup else lookup[acc_sum] + 1
            dfs(root.left,  acc_sum, lookup)
            dfs(root.right, acc_sum, lookup)
            lookup[acc_sum] -= 1
        dfs(root, 0)
        return self.count
