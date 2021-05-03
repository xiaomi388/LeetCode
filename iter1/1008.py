# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def dfs(right_parent, i):
            if i >= len(preorder): return None, i
            node = TreeNode(preorder[i])
            q = i + 1
            if q < len(preorder) and preorder[q] < node.val:
                node.left, q = dfs(node, q)
            if q < len(preorder) and (right_parent.val > preorder[q]):
                node.right, q = dfs(right_parent, q)
            return node, q
        return dfs(TreeNode(float('inf')), 0)[0]

# a better solution: use stack
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not len(preorder): return None
        root = TreeNode(preorder[0])
        st = [root]
        for val in preorder[1:]:
            node, child = st[-1], TreeNode(val)
            while st and st[-1].val < val:
                node = st.pop()
            if node.val < child.val:
                node.right = child
            else:
                node.left = child
            st.append(child)
        return root





