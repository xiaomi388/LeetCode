# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node, num_str):
            nonlocal ans
            if not node.left and not node.right:
                ans += int(num_str+str(node.val))
                return
            next_num_str = num_str + str(node.val)
            if node.left: dfs(node.left, next_num_str)
            if node.right: dfs(node.right, next_num_str)
        if not root: return 0
        dfs(root, "")
        return ans

