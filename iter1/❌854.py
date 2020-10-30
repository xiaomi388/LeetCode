# So that in each round we will repair the first unordered character and as a result move
# forward at least 1 step.
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        def nei(x):
            i = 0
            while x[i] == B[i]: i+=1
            for j in range(i+1, len(x)):
                if x[j] == B[i] and x[j] != B[j]: yield x[:i]+x[j]+x[i+1:j]+x[i]+x[j+1:]
        q, seen = [(A,0)], {A}
        for x, d in q:
            if x == B: return d
            for y in nei(x):
                if y not in seen:
                    seen.add(y), q.append((y,d+1))

class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        if A == B: return 0
        seen = set()
        que = collections.deque([(A, 0)])
        while len(que):
            s, k = que.popleft()
            i = 0
            while s[i] == B[i]: i += 1
            for q in range(i+1, len(s)):
                if s[q] == B[q] or s[q] != B[i]: continue
                next_s = s[:i] + s[q] + s[i+1:q] + s[i] + s[q+1:]
                if next_s == B: return k+1
                if next_s in seen: continue
                seen.add(next_s)
                que.append((next_s, k+1))
        return float('inf')