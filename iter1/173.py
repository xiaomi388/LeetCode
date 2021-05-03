# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.st = []
        while root:
            self.st.append(root)
            root = root.left

    def next(self) -> int:
        node = self.st.pop()
        cur = node.right
        while cur:
            self.st.append(cur)
            cur = cur.left
        return node.val

    def hasNext(self) -> bool:
        return True if self.st else False


from itertools import chain

class BSTIterator:

    def __init__(self, root: TreeNode):
        def gen(root): yield from chain(gen(root.left), [root.val], gen(root.right)) if root else ()
        self.iter, self.len = gen(root), 0
        for _ in gen(root): self.len += 1

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.len -= 1
        return next(self.iter)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return bool(self.len)

