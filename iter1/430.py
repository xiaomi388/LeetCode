"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return head
        last = Node()
        def dfs(node):
            nonlocal last
            if not node: return
            n = node.next
            last.next = node
            node.prev = last
            last = node
            dfs(node.child)
            dfs(n)
            node.child = None
        dfs(head)
        head.prev = None
        return head
