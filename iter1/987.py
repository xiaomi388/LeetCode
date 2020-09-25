# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from sortedcontainers import SortedList, SortedDict

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        d = SortedDict()
        def dfs(node, x, y):
            if node is None: return
            if x not in d: d[x] = SortedDict()
            if y not in d[x]: d[x][y] = SortedList()
            d[x][y].append(node.val)
            dfs(node.left, x-1, y+1)
            dfs(node.right, x+1, y+1)
        dfs(root, 0, 0)
        return [[a for a in d[x][y] for y in d[x]] for x in d]





