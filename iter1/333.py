# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:

        ans = 0
        # return (is_bst, min, max, size)
        def dfs(node):
            nonlocal ans
            if not node: return True, float('inf'), -float('inf'), 0
            is_left_bst, left_min, left_max, left_size = dfs(node.left)
            is_right_bst, right_min, right_max, right_size = dfs(node.right)
            if not is_left_bst or not is_right_bst: return False, None, None, 0
            if left_max < node.val < right_min:
                size = left_size+right_size+1
                ans = max(ans, size)
                return True, min(left_min, node.val), max(right_max, node.val), size
            return False, None, None, 0
        dfs(root)
        return ans


