# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        head = TreeNode()
        tail = head
        def dfs(node):
            nonlocal head, tail
            if not node: return
            l, r = node.left, node.right
            tail.right = node
            tail = node
            dfs(l)
            dfs(r)
            node.left = None
        dfs(root)
        return head.right

