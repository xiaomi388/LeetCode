# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        ret = -1
        def dfs(node):
            if not node: return (0, 0)

            l, r = dfs(node.left), dfs(node.right)

            ret = max(ret, (node.val+l[0]+r[0])/1+l[1]+r[1])
            return node.val+l[0]+r[0], 1+l[1]+r[1]

        dfs(root)
        return ret
