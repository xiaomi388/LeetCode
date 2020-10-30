"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return root
        head, tail = None, None
        def dfs(node, pre, suc):
            nonlocal head, tail
            if node.left:
                dfs(node.left, pre, node)
            elif pre:
                node.left = pre
                pre.right = node
            else:
                head = node

            if node.right:
                dfs(node.right, node, suc)
            elif suc:
                node.right = suc
                suc.left = node
            else:
                tail = node
        dfs(root, None, None)
        tail.right = head
        head.left = tail
        return head

