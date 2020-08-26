# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 方法一：算出target的层级，然后再分别向上向下找
class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """

        ret = []
        def dfs(root, level):
            if not root:
                return
            if level == K:
                ret.append(root.val)
                return
            dfs(root.left, level+1)
            dfs(root.right, level+1)

        def findTarget(root):
            if not root:
                return -1
            if root == target:
                dfs(root, 0)
                return 0
            else:
                foundFromLeft = True
                l = findTarget(root.left)
                if l == -1:
                    foundFromLeft = False
                    l = findTarget(root.right)
                if l == -1:
                    return -1
                elif l+1 == K:
                    ret.append(root.val)
                else:
                    dfs(root.right if foundFromLeft else root.left, l+2)
                return l+1
        findTarget(root)
        return ret


# 方法二：记录父亲节点


class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        ret = []
        def dfs(root, level):
            if not root:
                return
            if getattr(root, 'isVisited', False):
                return
            root.isVisited = True
            if level == K:
                ret.append(root.val)
                return
            if getattr(root, 'parent', False):
                dfs(root.parent, level+1)
            dfs(root.left, level+1)
            dfs(root.right, level+1)

        def findTarget(root, parent):
            if not root:
                return None
            root.parent = parent
            if root == target:
                return root
            l = findTarget(root.left, root)
            if l: return l
            r = findTarget(root.right, root)
            if r : return r
            return None

        node = findTarget(root, None)
        dfs(node, 0)
        return ret

