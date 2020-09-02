# BFS....

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        minx, maxx = float('inf'), -float('inf')
        ret = collections.defaultdict(list)
        q = collections.deque([(root, 0)])
        while len(q):
            n = len(q)
            node, x = q.popleft()
            ret[x].append(node.val)
            minx, maxx = min(minx, x), max(maxx, x)
            if node.left: q.append((node.left, x-1))
            if node.right: q.append((node.right, x+1))
        return [ret[i] for i in range(minx, maxx+1)]


