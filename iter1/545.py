# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root: return []
        boundary = [root.val]

        def dfs(root, isleft, isright):
            if root:
                if (not root.left and not root.right) or isleft:
                    boundary.append(root.val)
                if root.left and root.right:
                    dfs(root.left, isleft, False)
                    dfs(root.left, False, isright)
                else:
                    dfs(root.left, isleft, isright)
                    dfs(root.right, isleft, isright)
            if (root.left or root.right) and isright:
                boundary.append(root.val)
        dfs(root.left, True, False)
        dfs(root.right, False, True)
        return boundary




