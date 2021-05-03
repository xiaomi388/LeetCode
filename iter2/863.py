# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        ans = []
        def search(node, dist):
            if not node: return
            if dist == K:
                ans.append(node.val)
            else:
                search(node.left, dist+1)
                search(node.right, dist+1)

        def dfs(node):
            """

            :param node: TreeNode
            :return: the distance to the target node. If not found return -1
            """

            if not node: return -1
            if node == target:
                search(node, 0)
                return 0

            dist = dfs(node.left)
            if dist != -1:
                dist += 1
                if dist == K:
                    ans.append(node.val)
                elif dist < K:
                    search(node.right, dist+1)
                return dist

            dist = dfs(node.right)
            if dist != -1:
                dist += 1
                if dist == K:
                    ans.append(node.val)
                elif dist < K:
                    search(node.left, dist+1)
                return dist
            return -1
        dfs(root)
        return ans

