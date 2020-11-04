"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        def _serialize(node):
            if not node: return
            js = {
                "val": node.val,
                "children": [_serialize(c) for c in node.children]
            }
            return js
        return json.dumps(_serialize(root))


    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        def _deserialize(js):
            if not js: return
            root = Node(val=js["val"])
            root.children = [_deserialize(c) for c in js["children"]]
            return root
        js = json.loads(data)
        return _deserialize(js)



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))