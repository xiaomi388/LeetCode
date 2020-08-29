class Solution:
    def trap(self, height: List[int]) -> int:
        q = collections.deque()
        cnt = 0
        for i in range(len(height)):
            while len(q) and height[q[-1]] < height[i]:
                j = q.pop()
                if len(q):
                    bound_height = min(height[q[-1]], height[i]) - height[j]
                    width = i-q[-1]-1
                    cnt += width * bound_height
            q.append(i)
        return cnt












