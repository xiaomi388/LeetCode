# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ret = []
        def dfs(node, path):
            if root.left is None and root.right is None:
                ret.append(path + [root.val])
                return
            dfs(node.left, node.val)
            dfs(node.right, node.val)
        dfs(root, [])
        return ret


