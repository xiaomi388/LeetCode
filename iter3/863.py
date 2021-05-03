# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        ans = []
        def search_down(node, dist):
            if not node: return
            if dist == 0:
                ans.append(node.val)
                return
            search_down(node.left, dist-1)
            search_down(node.right, dist-1)

        def dfs(node):
            if not node: return -1
            if node == target: return 0

            dist = dfs(node.left)
            if dist != -1:
                if dist == K - 1:
                    ans.append(node.val)
                elif dist < K - 1:
                    search_down(node.right, K-dist-2)
                return dist+1
            else:
                dist = dfs(node.right)
                if dist != -1:
                    if dist == K - 1:
                        ans.append(node.val)
                    elif dist < K - 1:
                        search_down(node.left, K-dist-2)
                    return dist+1
                return -1
        dfs(root)
        search_down(target, K)
        return ans
