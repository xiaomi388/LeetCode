"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# BFS
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        q = collections.deque([root])
        while len(q):
            n = len(q)
            for i in range(n):
                node = q.popleft()
                node.next = q[0] if len(q) and i != n-1 else None
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return root

# DFS
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        def dfs(node, right):
            if not node: return

            if node.left and node.right:
                node.left.next = node.right
