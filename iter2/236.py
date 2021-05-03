# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        paths = []
        def dfs(node, target, path):
            if not node:
                return
            if node == target:
                paths.append(path)
                return
            dfs(node.left, target, path + [node.left])
            dfs(node.right, target, path + [node.right])
        dfs(root, p, [root])
        dfs(root, q, [root])
        for i in range(min(len(paths[0]), len(paths[1]))):
            if paths[0][i] != paths[1][i]:
                return paths[0][i-1]
        return paths[0][-1] if len(paths[0]) < len(paths[1]) else paths[1][-1]
