from functools import lru_cache
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        @lru_cache(None)
        def height(node):
            if not node: return 0
            return max(height(node.left), height(node.right), 0) + node.val

        @lru_cache(None)
        def max_path_starting_from(node):
            if not node: return 0
            return max(height(node.left), 0) + max(height(node.right), 0) + node.val

        ans = float('-inf')
        def dfs(node):
            nonlocal ans
            if not node: return
            ans = max(ans, max_path_starting_from(node))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ans


# Path: the path from one node to the other node
# Height(x): the maximum path starting from x. By saying starting, we are saying the node x is the highest node in the path, and the node x is in one end of the path
# MaxPathStartingFrom(x): the maximum path containing x, and x is the highest node in the path.
# MaxPathStartingFrom(x) = Height(x.left) + Height(x.right) + x.val
# MaxPath = max([MaxPathStartingFrom(x) for x in everyNodeInTheTree])