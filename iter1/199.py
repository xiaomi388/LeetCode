# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#     1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
#  /
# 6
#
# 1, 3, 4, 6

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        max_level = -1
        def dfs(node, level):
            if not node: return
            if level > max_level:
                ans.append(node.val)
                max_level = level
            dfs(node.right, level+1)
            dfs(node.left, level+1)
        dfs(root, 0)
        return ans