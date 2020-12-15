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
        q = collections.deque([root])
        while len(q):
            last = None
            for _ in range(len(q)):
                node = q.pop()
                if last: last.next = node
                last = node
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return root

# 拉拉链解法
# Node* connect(Node* root) {
#     if (!root) return root;
#     Node * left = root->left;
#     Node * right = root->right;
#     while(left) {
#     left->next = right;
#     left = left->right;
#     right = right->left;
#     }
#     connect(root->left);
#     connect(root->right);
#     return root;
# }







