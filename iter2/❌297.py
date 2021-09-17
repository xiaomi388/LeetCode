# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        out = []
        def dfs(node):
            if node is None:
                out.append("#")
                return

            out.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ' '.join(out)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split()
        i = -1
        def dfs():
            nonlocal i
            i += 1
            if data[i] == "#":
                return None

            node = TreeNode(int(data[i]))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))