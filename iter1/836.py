class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # if the left side of the first rectangle is on the right side of
        # the second one or if the right side of the first rectangle is on
        # the left side of the rectangle or top/bottom, then we can conclude
        # that these two rects are not overlap. vice versa.
        return not any([
            rec1[0] >= rec2[2],
            ret1[1] <= rec2[3],
            ret1[2] <= rec2[0],
            ret1[3] <= rec2[1],
        ])

