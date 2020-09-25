from contextlib import ExitStack

class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        p = []
        def dfs(node, i):
            with ExitStack() as stack:
                p.append(node.val)
                stack.callback(lambda : p.pop())
                if node.val != arr[i]: return False
                if node.left is None and node.right is None and i == len(arr)-1:
                    return True
                elif i == len(arr)-1 or (node.left is None and node.right) is None: return False
                if node.left and dfs(node.left, i+1): return True
                if node.right and dfs(node.right, i+1): return True
                return False
        return dfs(root, 0)


