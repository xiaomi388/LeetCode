class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        q = collections.deque([(-1, 0)])
        ret = 0
        for i, height in enumerate(heights):
            while height < q[-1][1]:
                mid = q.pop()
                ret = max(ret, (i-q[-1][0]-1) * mid[1])
            q.append((i, height))
        last = q.popleft()
        while len(q):
            ret = max(ret, (q[-1][0]-last[0]) * q[0][1])
            last = q.popleft()
        return ret

