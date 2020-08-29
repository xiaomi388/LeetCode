class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        q = collections.deque()
        ret = [0] * len(T)
        for i in range(len(T)):
            while len(q) and T[q[-1]] < T[i]:
                ret[q[-1]] = i-q[-1]
                q.pop()
            q.append(i)
        return ret
