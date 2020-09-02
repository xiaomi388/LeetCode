# 线段树

from dataclasses import dataclass
@dataclass
class SegmentTreeNode:
    start : int
    end : int
    mid : int
    sum : int
    left : "SegmentTreeNode"
    right : "SegmentTreeNode"

class NumArray:

    def __init__(self, nums: List[int]):
        def buildTree(lo, hi):
            if lo > hi:
                return None
            if lo == hi:
                return SegmentTreeNode(lo, lo, lo, nums[lo], None, None)
            mid = (lo + hi) // 2
            left = buildTree(lo, mid)
            right = buildTree(mid+1, hi)
            return SegmentTreeNode(lo, hi, mid, left.sum+right.sum, left, right)

        self.tree = buildTree(0, len(nums)-1)

    def update(self, i: int, val: int) -> None:
        def _update(node):
            if node.start == node.end == i:
                node.sum = val
                return
            _update(node.left) if node.mid >= i else _update(node.right)
            node.sum = node.left.sum + node.right.sum
        _update(self.tree)


    def sumRange(self, i: int, j: int) -> int:
        def _query(node, lo, hi):
            if node.start == lo and node.end == hi:
                return node.sum

            if lo <= hi <= node.mid:
                return _query(node.left, lo, hi)
            elif hi >= lo >= node.mid+1:
                return _query(node.right, lo, hi)
            else:
                return _query(node.left, lo, node.mid) + _query(node.right, node.mid+1, hi)
        return _query(self.tree, i, j)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

