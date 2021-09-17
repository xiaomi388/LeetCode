'''
1. build the sorted array [1, 2, 3, 4] => inorder dfs
2. rebuild a balanced tree
 0  1  2  3
[1, 2, 3, 4]
          L
          R
       M


                   2
                  / \
                 1   3
                      \
                       4
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        a = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            a.append(node.val)
            inorder(node.right)

        def build(l, r):
            if r < l: return None

            m = (l + r) // 2
            node = TreeNode(a[m])
            node.left = build(l, m-1)
            node.right = build(m+1, r)
            return node

        inorder(root)
        return build(0, len(a)-1)
