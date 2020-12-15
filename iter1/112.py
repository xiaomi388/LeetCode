# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        def dfs(node, cur_sum):
            if not node.left and not node.right:
                return sum == cur_sum + node.val
            flag = False
            if node.left:
                flag = flag or dfs(node.left, cur_sum+node.val)
            if node.right:
                flag = flag or dfs(node.right, cur_sum+node.val)
            return flag
        return dfs(root, 0)

