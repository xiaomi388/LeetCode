# BFS
#

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur = head = root
        while head and head.val != None:
            next_head = next_tail = Node(None)
            while cur:
                if cur.left:
                    next_tail.next, next_tail = cur.left, cur.left
                if cur.right:
                    next_tail.next, next_tail = cur.right, cur.right
                cur = cur.next
            cur, head = next_head.next, next_head.next
        return root


